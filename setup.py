from setuptools import setup

APP = ['TradingViewMonitor.py']
DATA_FILES = ['icon.icns']
OPTIONS = {
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleName': "TradingView Monitor",
        'CFBundleDisplayName': "TradingView Monitor",
        'CFBundleIdentifier': "com.yourcompany.TradingViewMonitor",
        'NSHumanReadableCopyright': "Copyright © 2025 Lusticon",
        'NSPrincipalClass': 'NSApplication',
        'LSUIElement': True,
    },
    'includes': [
        'WebKit',
        'Quartz',
        'Cocoa',
        'objc',
        'os',
        'json',
        'sys'
        'PyObjCTools',
    'PyObjCTools.AppKit',  # Добавьте это
    'PyObjCTools.CoreFoundation'
    ],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)