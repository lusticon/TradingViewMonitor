import objc
import Quartz
from Cocoa import *
from WebKit import WKWebView, WKWebViewConfiguration
import os
import json

STATE_FILE = os.path.expanduser("monitor_state.json")
ICON_PATH = "icon.icns"
DEFAULT_TV_ID = "t1CESWPv"

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        screen_size = NSScreen.mainScreen().frame().size

        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    state = json.load(f)
                    x, y = state.get("x", 100), state.get("y", 100)
                    width = state.get("width", 800)
                    height = state.get("height", 600)
                    self.tv_chart_id = state.get("chart_id", DEFAULT_TV_ID)
                    self.tv_liq_id = state.get("liq_id", "BYBIT")
                    self.tv_instr_id = state.get("instr_id", "BTCUSDT.P")
                    self.tv_interval_id = state.get("interval_id", "5")
            except:
                x, y, width, height = 100, 100, 800, 600
                self.tv_chart_id = DEFAULT_TV_ID
                self.tv_liq_id = "BYBIT"
                self.tv_instr_id = "BTCUSDT.P"
                self.tv_interval_id = "5"
        else:
            width, height = 800, 600
            x = (screen_size.width - width) / 2
            y = (screen_size.height - height) / 2
            self.tv_chart_id = DEFAULT_TV_ID
            self.tv_liq_id = "BYBIT"
            self.tv_instr_id = "BTCUSDT.P"
            self.tv_interval_id = "5"

        self.window_style = NSWindowStyleMaskTitled | NSWindowStyleMaskClosable | NSWindowStyleMaskResizable

        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(x, y, width, height),
            self.window_style,
            NSBackingStoreBuffered,
            False
        )

        self.window.setTitle_("TradingView Monitor")
        self.window.setTitleVisibility_(0)
        self.window.setTitlebarAppearsTransparent_(True)
        self.window.setMovableByWindowBackground_(True)
        self.window.setLevel_(NSFloatingWindowLevel)
        self.window.setOpaque_(False)
        self.window.setAlphaValue_(0.0)

        if os.path.exists(ICON_PATH):
            icon = NSImage.alloc().initWithContentsOfFile_(ICON_PATH)
            NSApp.setApplicationIconImage_(icon)

        self.window.contentView().setWantsLayer_(True)
        self.layer = self.window.contentView().layer()
        self.layer.setCornerRadius_(15.0)
        self.layer.setMasksToBounds_(True)

        blur_view = NSVisualEffectView.alloc().initWithFrame_(self.window.contentView().bounds())
        blur_view.setAutoresizingMask_(NSViewWidthSizable | NSViewHeightSizable)
        blur_view.setBlendingMode_(NSVisualEffectBlendingModeBehindWindow)
        blur_view.setMaterial_(NSVisualEffectMaterialSidebar)
        blur_view.setState_(1)

        content_frame = self.window.contentView().frame()
        config = WKWebViewConfiguration.alloc().init()
        self.web_view = WKWebView.alloc().initWithFrame_configuration_(content_frame, config)
        self.web_view.setAutoresizingMask_(NSViewWidthSizable | NSViewHeightSizable)

        url_str = f"https://ru.tradingview.com/chart/{self.tv_chart_id}/?symbol={self.tv_liq_id}%3A{self.tv_instr_id}&interval={self.tv_interval_id}"
        url = objc.lookUpClass("NSURL").URLWithString_(url_str)
        request = objc.lookUpClass("NSURLRequest").requestWithURL_(url)
        self.web_view.loadRequest_(request)

        blur_view.addSubview_(self.web_view)

        self.button_container = NSView.alloc().initWithFrame_(NSMakeRect((content_frame.size.width - 160) / 2, 10, 160, 28))
        self.button_container.setAutoresizingMask_(NSViewMinXMargin | NSViewMinYMargin)
        self.button_container.setHidden_(True)

        def style_button(btn):
            btn.setBezelStyle_(1)
            btn.setFont_(NSFont.systemFontOfSize_(12))
            btn.setBordered_(False)
            btn.setWantsLayer_(True)
            btn.layer().setBackgroundColor_(NSColor.blackColor().colorWithAlphaComponent_(0.8).CGColor())
            btn.layer().setCornerRadius_(6.0)
            btn.setLineBreakMode_(NSLineBreakByTruncatingTail)

        # Close Button
        self.close_button = NSButton.alloc().initWithFrame_(NSMakeRect(0, 0, 24, 24))
        self.close_button.setTitle_("×")
        self.close_button.setTarget_(self)
        self.close_button.setAction_("closeApp:")
        style_button(self.close_button)
        self.button_container.addSubview_(self.close_button)

        # Topmost Button
        self.top_button = NSButton.alloc().initWithFrame_(NSMakeRect(34, 0, 24, 24))
        self.top_button.setTitle_("⊕")
        self.top_button.setTarget_(self)
        self.top_button.setAction_("toggleTop:")
        style_button(self.top_button)
        self.button_container.addSubview_(self.top_button)

        # Titlebar Button
        self.titlebar_button = NSButton.alloc().initWithFrame_(NSMakeRect(68, 0, 24, 24))
        self.titlebar_button.setTitle_("︼")
        self.titlebar_button.setTarget_(self)
        self.titlebar_button.setAction_("toggleTitlebar:")
        style_button(self.titlebar_button)
        self.button_container.addSubview_(self.titlebar_button)

        # Settings Button
        self.url_button = NSButton.alloc().initWithFrame_(NSMakeRect(102, 0, 24, 24))
        self.url_button.setTitle_("⌘")
        self.url_button.setTarget_(self)
        self.url_button.setAction_("changeChartID:")
        style_button(self.url_button)
        self.button_container.addSubview_(self.url_button)

        # Auto Reload Button
        self.auto_button = NSButton.alloc().initWithFrame_(NSMakeRect(136, 0, 24, 24))
        self.auto_button.setTitle_("⏱")
        self.auto_button.setTarget_(self)
        self.auto_button.setAction_("toggleAutoReload:")
        style_button(self.auto_button)
        self.button_container.addSubview_(self.auto_button)

        blur_view.addSubview_(self.button_container)
        self.window.setContentView_(blur_view)

        self.always_on_top = True
        self.titlebar_hidden = False
        self.auto_reload_enabled = False
        self.reload_timer = None

        self.window.makeKeyAndOrderFront_(None)
        NSRunningApplication.currentApplication().activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

        NSAnimationContext.beginGrouping()
        NSAnimationContext.currentContext().setDuration_(0.4)
        self.window.animator().setAlphaValue_(1.0)
        NSAnimationContext.endGrouping()

        self.register_hotkeys()
        self.tracking_area = None
        self.add_tracking_area()

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self, "windowDidResize:", "NSWindowDidResizeNotification", self.window
        )

    def changeChartID_(self, sender):
        alert = objc.lookUpClass("NSAlert").alloc().init()
        alert.setMessageText_("TradingView URL Settings")
        alert.addButtonWithTitle_("OK")
        alert.addButtonWithTitle_("Cancel")

        input_chart = objc.lookUpClass("NSTextField").alloc().initWithFrame_(NSMakeRect(0, 100, 250, 24))
        input_chart.setStringValue_(self.tv_chart_id)

        input_liq = objc.lookUpClass("NSTextField").alloc().initWithFrame_(NSMakeRect(0, 70, 250, 24))
        input_liq.setStringValue_(self.tv_liq_id)

        input_instr = objc.lookUpClass("NSTextField").alloc().initWithFrame_(NSMakeRect(0, 40, 250, 24))
        input_instr.setStringValue_(self.tv_instr_id)

        input_interval = objc.lookUpClass("NSTextField").alloc().initWithFrame_(NSMakeRect(0, 10, 250, 24))
        input_interval.setStringValue_(self.tv_interval_id)

        container = NSView.alloc().initWithFrame_(NSMakeRect(0, 0, 250, 130))
        container.addSubview_(input_chart)
        container.addSubview_(input_liq)
        container.addSubview_(input_instr)
        container.addSubview_(input_interval)

        alert.setAccessoryView_(container)

        response = alert.runModal()
        if response == 1000:
            self.tv_chart_id = input_chart.stringValue()
            self.tv_liq_id = input_liq.stringValue()
            self.tv_instr_id = input_instr.stringValue()
            self.tv_interval_id = input_interval.stringValue()

            url_str = f"https://ru.tradingview.com/chart/{self.tv_chart_id}/?symbol={self.tv_liq_id}%3A{self.tv_instr_id}&interval={self.tv_interval_id}"
            url = objc.lookUpClass("NSURL").URLWithString_(url_str)
            request = objc.lookUpClass("NSURLRequest").requestWithURL_(url)
            self.web_view.loadRequest_(request)

    def toggleAutoReload_(self, sender):
        self.auto_reload_enabled = not self.auto_reload_enabled
        if self.auto_reload_enabled:
            self.reload_timer = Quartz.NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
                60.0, self, "reloadPage:", None, True
            )
            self.auto_button.setTitle_("■")
        else:
            if self.reload_timer:
                self.reload_timer.invalidate()
                self.reload_timer = None
            self.auto_button.setTitle_("⏱")

    def reloadPage_(self, timer):
        self.web_view.reload()

    def toggleTitlebar_(self, sender):
        self.titlebar_hidden = not self.titlebar_hidden
        frame = self.window.frame()
        mask = self.window.styleMask()

        if self.titlebar_hidden:
            new_mask = mask & ~NSWindowStyleMaskTitled
            self.titlebar_button.setTitle_("︻")
            self.layer.setCornerRadius_(15.0)
        else:
            new_mask = mask | NSWindowStyleMaskTitled
            self.titlebar_button.setTitle_("︼")
            self.layer.setCornerRadius_(15.0)

        self.window.setStyleMask_(new_mask)
        self.window.setFrame_display_(frame, True)
        self.window.setMovableByWindowBackground_(True)
        self.window.setTitlebarAppearsTransparent_(True)

    def closeApp_(self, sender):
        frame = self.window.frame()
        state = {
            "x": frame.origin.x,
            "y": frame.origin.y,
            "width": frame.size.width,
            "height": frame.size.height,
            "chart_id": self.tv_chart_id,
            "liq_id": self.tv_liq_id,
            "instr_id": self.tv_instr_id,
            "interval_id": self.tv_interval_id
        }
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)
        NSApplication.sharedApplication().terminate_(None)

    def toggleTop_(self, sender):
        self.always_on_top = not self.always_on_top
        level = NSFloatingWindowLevel if self.always_on_top else NSNormalWindowLevel
        self.window.setLevel_(level)
        new_title = "⊕" if self.always_on_top else "⌽"
        self.top_button.setTitle_(new_title)

    def register_hotkeys(self):
        def hotkey_handler(event):
            chars = event.charactersIgnoringModifiers()
            flags = event.modifierFlags()
            if (flags & 1048576) and chars == "w":
                self.closeApp_(None)
            elif (flags & 1048576) and chars == "r":
                self.web_view.reload()
            return event

        NSEvent.addLocalMonitorForEventsMatchingMask_handler_(
            10485760,
            hotkey_handler
        )

    def add_tracking_area(self):
        if self.tracking_area:
            self.window.contentView().removeTrackingArea_(self.tracking_area)

        self.tracking_area = NSTrackingArea.alloc().initWithRect_options_owner_userInfo_(
            self.window.contentView().bounds(),
            NSTrackingMouseEnteredAndExited | NSTrackingActiveAlways,
            self,
            None
        )
        self.window.contentView().addTrackingArea_(self.tracking_area)

    def mouseEntered_(self, event):
        self.window.setTitleVisibility_(0)
        self.button_container.setHidden_(False)

    def mouseExited_(self, event):
        self.window.setTitleVisibility_(1)
        self.button_container.setHidden_(True)

    def windowDidResize_(self, notification):
        frame = self.window.contentView().frame()
        self.button_container.setFrameOrigin_(((frame.size.width - 160) / 2, 10))
        self.add_tracking_area()

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyRegular)

    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)

    NSApp.activateIgnoringOtherApps_(True)
    app.run()