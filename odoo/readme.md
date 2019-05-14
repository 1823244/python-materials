## Odoo 12 installation on Windows 10

Как я устанавливал Odoo 12 Community edition.  

Установочный пакет можно скачать здесь : https://www.odoo.com/page/download  
В процессе установки сразу ставится Postgres, правда версия там 9.5 (при том, что уже 11.1 есть).  
Однако, свежеустановленное приложение не запускается по причине:  
```
windows could not start odoo 12 services on local computer. The services did not return any error. This could be an internal windows error, if problem persists then contact your system administrator site:www.odoo.com
```

Служба остается в состоянии "paused".  


### Попытка №1. Поменять пользователя, от которого запускается служба.  
Не помогло.  

### Попытка №2. Установить пакеты из зависимостей \server\requirements.txt:  
pip install -r requirements.txt  

Вроде что-то началось устанавливаться, но потом выдало ошибку  
```
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
```
Пришлось скачать Build Tools.  
Ссылка https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019

Оттуда качается Visual Studio Installer  
В разделе Tools for Visual Studio 2019 находим секцию Build Tools for Visual Studio 2019 и нажимаем синюю кнопку Download.  
(или прямая ссылка https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)  
Файл называется ```vs_buildtools__1525085075.1551777586```  
В инсталлере выбираем компоненты. Нам потребуется только "сборка приложений C++".  
Объем для скачивания - примерно 6 ГБ.
Добавил на вкладке "Отдельные компоненты" - MSCV 140 - C++ 14.0  
Помогло, но теперь другая ошибка  
```
LINK : fatal error LNK1158: не удается запустить "rc.exe
```
Похоже, надо ставить Windows Kits:
https://developer.microsoft.com/ru-ru/windows/downloads/windows-10-sdk  
Да, это помогло, rc.exe появился.  
Скопировал файлы rc.exe и rcdll.dll из каталога  
```
c:\Program Files (x86)\Windows Kits\10\bin\10.0.18362.0\x64\
```
в каталог  
```
c:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\
```
После этого компиляция пакетов прошла неуспешно:(  

надо читать  
Ветка на форуме  
http://odoo-russia.ru/forum/topic/590/  



Здесь еще одна инструкция по установке билд тулс  
http://qaru.site/questions/202909/microsoft-visual-c-140-is-required-unable-to-find-vcvarsallbat  
Поиск по фразе "Убедитесь, что вы установили эти требуемые пакеты. Отлично сработало в моем случае, так как я установил проверенные пакеты", там картинка с набором компонент. (хотя я делал не по ней)  



### Бинарники для питона

https://www.lfd.uci.edu/~gohlke/pythonlibs/  



## Инструкция по запуску Odoo из исходников:  
https://www.odoo.com/documentation/12.0/setup/install.html#running-odoo  




