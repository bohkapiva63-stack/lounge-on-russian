import os, glob

repo = '/home/bohka/.gemini/antigravity/scratch/lounge'

translations = {
    # AllAppsScreen.kt
    "Apps appear here once they are installed.": "Приложения появятся здесь после установки.",
    "Apps starting with a number or symbol": "Приложения на цифру или символ",
    "Change the order": "Изменить порядок",
    "Hold OK on an app to pin it to Your apps. Up to search or sort, Left for the alphabet.": "Удерживайте OK для закрепления. Вверх — поиск/сортировка, Влево — алфавит.",
    "Hold OK on an app to pin it to Your apps. Up to search or sort.": "Удерживайте OK для закрепления в Ваших приложениях. Вверх — поиск и сортировка.",
    "most recently opened first": "сначала недавно открытые",
    "newest first": "сначала новые",
    "Nothing matches": "Ничего не найдено",
    
    # Ambient.kt (Заставка)
    "Any key brings you back": "Любая клавиша для возврата",
    "Artwork from your home screen": "Обложки с вашего главного экрана",
    "Preview it now": "Предпросмотр",
    "Show your artwork or a slow abstract scene with a clock when the TV idles.": "Показ обложек или плавной анимации с часами во время простоя ТВ.",
    "The TV's own": "Системная заставка ТВ",
    "Pictures": "Обложки",
    "Switching…": "Переключение…",
    "Off": "Выкл",
    "On": "Вкл",
    "The room's own light": "Естественный свет",
    
    # Guide.kt (Телепрограмма)
    "Channels show here once a TV app or a plugin lists what is on.": "Каналы появятся здесь, как только приложение или плагин загрузит программу.",
    "No channels yet": "Каналов пока нет",
    "No programme information": "Нет информации о передаче",
    "Reading the guide": "Загрузка телегида...",
    
    # HomeScreen.kt
    "All shown": "Все отображаются",
    "No apps or channels yet": "Нет приложений или каналов",
    "Hold OK on a tile to pin or hide it": "Удерживайте OK на карточке для закрепления или скрытия",
    
    # SearchScreen.kt
    "Search apps and media": "Поиск приложений и фильмов",
    "Type to search": "Введите для поиска",
    "Clear": "Очистить",
    
    # TopBar.kt
    "Search": "Поиск",
    "Settings": "Настройки",
    
    # Notifications.kt
    "Clear all": "Очистить все",
    "No notifications": "Нет новых уведомлений",
    "Dismiss": "Закрыть",
    "Open": "Открыть",
    "Hide everything from this app": "Скрыть все уведомления от этого приложения",
    
    # Plugins.kt
    "Installed": "Установлено",
    "Available": "Доступно",
    "Configure": "Настроить",
    "Enable": "Включить",
    "Disable": "Отключить",
    "Uninstall": "Удалить",
    "Install": "Установить",
    "No plugins installed": "Плагины пока не установлены",
    "Get more plugins": "Загрузить плагины",
    
    # Updates.kt
    "Up to date": "Установлена актуальная версия",
    "Check for updates": "Проверить обновления",
    "Checking for updates…": "Проверка обновлений…",
    "Download and install": "Скачать и установить",
    "Update available": "Доступно обновление",
    "What's new": "Что нового",
    
    # Onboarding.kt
    "Welcome to Lounge": "Добро пожаловать в Lounge",
    "Get started": "Начать",
    "Skip": "Пропустить",
    "Next": "Далее",
    "Done": "Готово",
    "Finish": "Завершить",
    
    # Power.kt / Backends.kt
    "Power Setup": "Расширенные системные права",
    "Connected": "Подключено",
    "Not connected": "Не подключено",
    "Waiting for you": "Ожидание действия",
}

kt_files = glob.glob(f'{repo}/android/**/*.kt', recursive=True)
count = 0
for f in kt_files:
    if '/test/' in f: continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    orig = content
    for eng, ru in translations.items():
        if f'"{eng}"' in content:
            content = content.replace(f'"{eng}"', f'"{ru}"')
            count += 1
            
    if content != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)

print(f"Applied {count} UI string replacements across Kotlin code!")
