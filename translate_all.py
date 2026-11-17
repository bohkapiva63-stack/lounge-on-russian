import os, re

repo_dir = '/home/bohka/.gemini/antigravity/scratch/lounge'

# 1. Sheets.kt - Settings and options
sheets_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Sheets.kt')
with open(sheets_path, 'r', encoding='utf-8') as f:
    c = f.read()

replacements_sheets = [
    ('SheetHeading("Settings")', 'SheetHeading("Настройки")'),
    ('SheetGroup("Home screen")', 'SheetGroup("Главный экран")'),
    ('title = "Rows",', 'title = "Ряды",'),
    ('subtitle = "Show, hide and move rows",', 'subtitle = "Показ, скрытие и перемещение рядов",'),
    ('subtitle = "Pinned apps, then recent ones",', 'subtitle = "Закрепленные приложения, затем недавние",'),
    ('"Pinned only"', '"Только закрепленные"'),
    ('"$recentApps recent"', '"$recentApps недавних"'),
    ('title = "Phone apps in All apps",', 'title = "Телефонные приложения",'),
    ('subtitle = "Apps made for phones, which may not work well with a remote",', 'subtitle = "Приложения для телефонов (могут плохо управляться пультом)",'),
    ('title = "Channels from apps",', 'title = "Каналы приложений",'),
    ('subtitle = "Rows that apps on this TV publish",', 'subtitle = "Каналы и ленты, публикуемые приложениями",'),
    ('"None"', '"Нет"'),
    ('"$enabledChannels on"', '"Включено: $enabledChannels"'),
    ('title = "Plugins",', 'title = "Плагины",'),
    ('subtitle = "Rows, channels and guide data from your services",', 'subtitle = "Ряды, каналы и телепрограмма от ваших сервисов",'),
    ('"None on"', '"Выключены"'),
    ('"$enabledPlugins on"', '"Включено: $enabledPlugins"'),
    ('title = "Notifications",', 'title = "Уведомления",'),
    ('subtitle = "What apps want to tell you",', 'subtitle = "Сообщения и уведомления от приложений",'),
    ('"Not allowed"', '"Не разрешено"'),
    ('SheetGroup("Look and sound")', 'SheetGroup("Внешний вид и звук")'),
    ('title = "Theme",', 'title = "Тема оформления",'),
    ('title = "Background",', 'title = "Фон",'),
    ('title = "Screensaver",', 'title = "Заставка",'),
    ('title = "Sounds",', 'title = "Звуки",'),
    ('title = "Lite mode",', 'title = "Легкий режим (Lite)",'),
    ('title = "Reduce motion",', 'title = "Уменьшение анимаций",'),
    ('"Follow system"', '"Как в системе"'),
    ('when (lite) { null -> "Automatic"; true -> "On"; false -> "Off" }', 'when (lite) { null -> "Автоматически"; true -> "Вкл"; false -> "Выкл" }'),
    ('"Automatic"', '"Автоматически"'),
    ('SheetGroup("Access")', 'SheetGroup("Доступ и разрешения")'),
    ('SheetGroup("This TV")', 'SheetGroup("Этот телевизор")'),
    ('title = "Default home screen",', 'title = "Домашний экран по умолчанию",'),
    ('subtitle = "What the Home button opens",', 'subtitle = "Что открывает кнопка Home на пульте",'),
    ('"Set up"', '"Настроить"'),
    ('title = "Power Setup",', 'title = "Расширенные права (Power Setup)",'),
    ('subtitle = "Lets Lounge do what an app can\'t on its own",', 'subtitle = "Позволяет Lounge управлять системными функциями ТВ",'),
    ('"Connected"', '"Подключено"'),
    ('"Waiting for you"', '"Ожидает подтверждения"'),
    ('"Not connected"', '"Не подключено"'),
    ('title = "Phone companion",', 'title = "Управление с телефона",'),
    ('title = "Updates",', 'title = "Обновления",'),
    ('title = "Diagnostics",', 'title = "Диагностика",'),
    ('subtitle = "Numbers to include when you report a problem",', 'subtitle = "Сведения об устройстве и системе",'),
    ('title = "Run the setup steps again",', 'title = "Пройти первоначальную настройку заново",'),
    ('SheetFootnote("Left and Right change a value. Back closes.")', 'SheetFootnote("Влево / Вправо — изменить. Назад — закрыть.")'),
    ('SheetHeading("Backdrop")', 'SheetHeading("Фон рабочего стола")'),
    ('SheetHeading("Sounds")', 'SheetHeading("Системные звуки")'),
    ('SheetHeading("Rows")', 'SheetHeading("Ряды")'),
    ('SheetHeading("Channels")', 'SheetHeading("Каналы")'),
    ('SheetHeading("Plugins")', 'SheetHeading("Плагины")'),
    ('SheetHeading("Notifications")', 'SheetHeading("Уведомления")'),
]

for old, new in replacements_sheets:
    c = c.replace(old, new)

with open(sheets_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 2. RowsSheet.kt - Rows management
rows_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/RowsSheet.kt')
with open(rows_path, 'r', encoding='utf-8') as f:
    c = f.read()

replacements_rows = [
    ('SheetHeading("Rows")', 'SheetHeading("Настройка рядов")'),
    ('SheetGroup("Hidden from every row")', 'SheetGroup("Скрытые приложения")'),
    ('SheetGroup("Continue watching comes from")', 'SheetGroup("Источники Продолжить просмотр")'),
    ('"Hold OK to move a row. Left and Right hide or show."', '"Удерживайте OK для перемещения. Влево / Вправо — скрыть или показать."'),
]
for old, new in replacements_rows:
    c = c.replace(old, new)

with open(rows_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 3. Notifications.kt
notif_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Notifications.kt')
with open(notif_path, 'r', encoding='utf-8') as f:
    c = f.read()

replacements_notif = [
    ('SheetHeading("Notifications")', 'SheetHeading("Уведомления")'),
    ('SheetGroup("Hidden apps")', 'SheetGroup("Скрытые приложения")'),
    ('"No notifications"', '"Нет новых уведомлений"'),
    ('"Clear all"', '"Очистить все"'),
]
for old, new in replacements_notif:
    c = c.replace(old, new)

with open(notif_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 4. TopBar.kt & Stage.kt
topbar_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/TopBar.kt')
if os.path.exists(topbar_path):
    with open(topbar_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('"Search"', '"Поиск"')
    c = c.replace('"Settings"', '"Настройки"')
    with open(topbar_path, 'w', encoding='utf-8') as f:
        f.write(c)

# 5. Themes.kt
themes_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Themes.kt')
if os.path.exists(themes_path):
    with open(themes_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('"Blackout"', '"Глубокий черный (Blackout)"')
    c = c.replace('"High contrast"', '"Высокая контрастность"')
    with open(themes_path, 'w', encoding='utf-8') as f:
        f.write(c)

# 6. Plugins.kt
plugins_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Plugins.kt')
if os.path.exists(plugins_path):
    with open(plugins_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('SheetHeading("Plugins")', 'SheetHeading("Плагины")')
    c = c.replace('"No plugins installed"', '"Плагины не установлены"')
    with open(plugins_path, 'w', encoding='utf-8') as f:
        f.write(c)

# 7. Updates.kt
updates_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Updates.kt')
if os.path.exists(updates_path):
    with open(updates_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('SheetHeading("Updates")', 'SheetHeading("Обновления")')
    c = c.replace('"Up to date"', '"У вас новейшая версия"')
    c = c.replace('"Check for updates"', '"Проверить обновления"')
    with open(updates_path, 'w', encoding='utf-8') as f:
        f.write(c)

print('Deep translation script finished successfully!')
