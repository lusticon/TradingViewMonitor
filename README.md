<p align="center">
  <img width="120" height="120" src="https://i.ibb.co/0Rsx8WGM/Any-Conv-1-com-Group-2-512x512x32.png">
</p>

<p align="center">
TradingView Monitor
</p>
<br>

🇺🇸 A floating window for monitoring TradingView charts, which can be placed on top of all windows to keep track of the market. Version for MacOS Sequoia (not tested on other versions) ℹ️[[EN]Description...](#en-desc)

🇷🇺 Плавающее окно, для наблюдения за графиком TradingView, которое можно расположить поверх всех окон для наблюдения за рынком. Версия для MacOs Sequoia (на других версиях не тестировалось) ℹ️[[RU]Описание...](#ru-desc)


<br>
<br>

<a name="ru-desc"></a>
## 🇷🇺 Описание на Русском


### 🔸 Функционал:
**Наблюдаем за графиками, занимаясь своими делами. Кроме движения рынка отображается вся ваша разметка графика.**

![App Screenshot](https://i.ibb.co/zWrS3nvg/Untitled.gif)


#### Функции панели управления окном (расположена снизу):

- Кнопка выхода из программы
- Кнопка «Закрепить/Открепить» окно поверх всех окон
- Кнопка «Показать заголовок окна». За заголовок можно перетаскивать окно в нужное место, затем, открепив, окно останется неподвижным.
+ Кнопка «Настройки»: 
    - Поле ID графика. Берется из TradingView
    ![ID](https://i.ibb.co/n8ZhChDK/Untitled1.gif)
    - Поставщик ликвидности (OANDA/BYBIT/BINANCE и т.д.)
    - Инструмент (Forex/Crypto инструмент, который торгуете)
    - Таймфрейм (Таймфрейм за которым следите)
- Кнопка автообновления. Обновляет график раз в минуту. Нужна для обхода появления всплывающего окна (если не авторизованы)

### ‼️ Важно:

В мониторе можно авторизоваться только через почту, другие виды авторизации не работают. Если ваш основной аккаунт за которым вы следите создан через другие средства авторизации, то у вас два варианта:

- Создать пустой аккаунт TradingView и мониторить с него ваш основной график.
- Включить кнопку автообновления, авторизация не потребуется. Автообновление необходимо, чтобы у вас не появлялось всплывающее окно с призывом к регистрации.

<hr>

#### 🏀 Будет добавлено позднее:
- Кастомные стили CSS
- Горячие клавиши
- Будильники
- Световая индикация пробоя уровней

<hr>

## 📥 Скачать:

Последний релиз: ⬇️[TradingViewMonitor-v0.1 macos](https://github.com/lusticon/TradingViewMonitor/releases/tag/alpha)   

⚠️ Если при запуске вы видите ошибку "Приложение повреждено, и его не удается открыть. Переместите приложение в Корзину", откройте терминал и введите: 

```
sudo xattr -r -c /Applications/TradingView\ Monitor.app 
```


<hr>

### 🛠️ Техническая информация:

Приложение написано на python 3.8 и собрано с помощью py2app. Вы можете проделать это самостоятельно.

- Скачайте исходники с Git
  
- Убедитесь, что установлены все зависимости:
```
pip install pyobjc pyobjc-core pyobjc-framework-Cocoa pyobjc-framework-WebKit
```
- Соберите программу
```
python setup.py py2app
```
- Либо запустите скрипт
```
python TradingViewMonitor.py
```
<br>
<br>

<a name="en-desc"></a>
## 🇺🇸 English Description (AI Translated)


### 🔸 Features:

**Monitor charts while handling your tasks. In addition to market movement, all your chart markings are displayed.**

![App Screenshot](https://i.ibb.co/zWrS3nvg/Untitled.gif)


#### Window Control Panel Functions (Located at the Bottom):

- Exit Button: Closes the program.
- "Pin/Unpin" Button: Keeps the window on top of all other windows.
- "Show Window Title" Button: Allows dragging the window to the desired location. After unpinning, the window remains stationary.
+ "Settings" Button:
    - Chart ID Field: Retrieved from TradingView.
    ![ID](https://i.ibb.co/n8ZhChDK/Untitled1.gif)
    - Liquidity Provider: (OANDA/BYBIT/BINANCE, etc.)
    - Instrument: (Forex/Crypto instrument you are trading)
    - Timeframe: (Timeframe you are monitoring)
- Auto-Update Button: Updates the chart every minute. Required to bypass the pop-up window (if not authenticated).

### ‼️ Important:

Authentication in the monitor is only possible via email; other authentication methods do not work. If your primary account (which you are monitoring) was created using other authentication methods, you have two options:
 - Create an empty TradingView account and monitor your primary chart from there.
 - Enable the Auto-Update Button; authentication will not be required. Auto-update is necessary to prevent pop-up windows prompting you to register.

<hr>

#### 🏀 To Be Added Later:

- Custom CSS Styles
- Hotkeys
- Alarms
- Visual Level Breakthrough Indicators

<hr>

## 📥 Download:
Last Release here: ⬇️[TradingViewMonitor-v0.1 macos](https://github.com/lusticon/TradingViewMonitor/releases/tag/alpha)   

⚠️ If you see "App is damaged and can't be opened. You should move it to the Trash" error, open the terminal and enter: 

```
sudo xattr -r -c /Applications/TradingView\ Monitor.app 
```

<hr>

### 🛠️ Technical Information:

The application is written in Python 3.8 and built using py2app. You can do this yourself.

- Download the source code from GitHub
- Ensure all dependencies are installed:
```
pip install pyobjc pyobjc-core pyobjc-framework-Cocoa pyobjc-framework-WebKit
```
- Build the program:
```
python setup.py py2app
```
- Or run the script:
```
python TradingViewMonitor.py
```



  
  <br>
  <br>
  <br>
  © Lusticon, 2025
