import os

repo_dir = '/home/bohka/.gemini/antigravity/scratch/lounge'

# 1. TopBar.kt
topbar_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/TopBar.kt')
with open(topbar_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('"TV guide"', '"Телегид"')
c = c.replace('"TV controls"', '"Управление ТВ"')

with open(topbar_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 2. Notifications.kt
notif_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Notifications.kt')
with open(notif_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('fun count(n: Int): String = Words.counted(n, "notification", "notifications")', 
              'fun count(n: Int): String = "$n " + if (n % 10 == 1 && n % 100 != 11) "уведомление" else if (n % 10 in 2..4 && (n % 100 < 10 || n % 100 >= 20)) "уведомления" else "уведомлений"')

with open(notif_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 3. Sheets.kt
sheets_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Sheets.kt')
with open(sheets_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('title = "Your apps"', 'title = "Ваши приложения"')
c = c.replace('value = theme.title', 'value = theme.title.replace("Absinthe", "Полынь").replace("Blackout", "Черный").replace("High contrast", "Контрастная")')
c = c.replace('value = scenes[sceneAt].second', 'value = scenes[sceneAt].second.replace("Still", "Статичный")')

with open(sheets_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 4. Guide.kt
guide_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Guide.kt')
with open(guide_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('"TV guide"', '"Телегид"')

with open(guide_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 5. TileMenu.kt
tilemenu_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/TileMenu.kt')
with open(tilemenu_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('items += MenuItem("TV guide"', 'items += MenuItem("Телегид"')

with open(tilemenu_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated TopBar and Notifications successfully!")
