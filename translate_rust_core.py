import os

repo_dir = '/home/bohka/.gemini/antigravity/scratch/lounge'
engine_path = os.path.join(repo_dir, 'core/lounge-core/src/engine.rs')

with open(engine_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace CORE_ROWS
c = c.replace('("apps", "Your apps")', '("apps", "Ваши приложения")')
c = c.replace('("games", "Games")', '("games", "Игры")')
c = c.replace('("live", "Live now")', '("live", "В эфире")')
c = c.replace('("tvcontrols", "TV controls")', '("tvcontrols", "Управление ТВ")')
c = c.replace('"Inputs".to_string()', '"Входы".to_string()')
c = c.replace('"TV controls".to_string()', '"Управление ТВ".to_string()')
c = c.replace('title: "Live now".to_string()', 'title: "В эфире".to_string()')

# Replace Spotlight actions & categories
c = c.replace('ItemKind::Channel => ("Live now", "Watch")', 'ItemKind::Channel => ("В эфире", "Смотреть")')
c = c.replace('ItemKind::Game => ("Games", "Play")', 'ItemKind::Game => ("Игры", "Играть")')
c = c.replace('ItemKind::Wallpaper => ("Pictures", "Open")', 'ItemKind::Wallpaper => ("Галерея", "Открыть")')
c = c.replace('ItemKind::Input | ItemKind::Device => ("Inputs", "Switch")', 'ItemKind::Input | ItemKind::Device => ("Входы", "Переключить")')
c = c.replace('("New for you", "Watch")', '("Новинки для вас", "Смотреть")')
c = c.replace('("Up next", "Watch")', '("Следующее к просмотру", "Смотреть")')
c = c.replace('("Tonight", "Watch")', '("Сегодня вечером", "Смотреть")')
c = c.replace('("Games", "Play")', '("Игры", "Играть")')
c = c.replace('("Jump back in", "Open")', '("Вернуться", "Открыть")')
c = c.replace('("Your apps", "Open")', '("Ваши приложения", "Открыть")')

with open(engine_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated engine.rs successfully!")
