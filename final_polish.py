import os

repo_dir = '/home/bohka/.gemini/antigravity/scratch/lounge'

# 1. Update engine.rs:
# Change Row title "Your apps" to "Ваши приложения" in build_row
# Change "All apps" and "apps" subtitle to Russian in all_apps_tile
engine_path = os.path.join(repo_dir, 'core/lounge-core/src/engine.rs')
with open(engine_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('title: "Your apps".to_string()', 'title: "Ваши приложения".to_string()')
c = c.replace('title: "All apps".to_string()', 'title: "Все приложения".to_string()')
c = c.replace('subtitle: Some(counted(count, "app", "apps", "Nothing yet"))', 
              'subtitle: Some(format!("{} {}", count, if count % 10 == 1 && count % 100 != 11 { "приложение" } else if count % 10 >= 2 && count % 10 <= 4 && (count % 100 < 10 || count % 100 >= 20) { "приложения" } else { "приложений" }))')

with open(engine_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 2. Update Themes.kt:
# Translate all theme titles and taglines to beautiful Russian
themes_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Themes.kt')
with open(themes_path, 'r', encoding='utf-8') as f:
    c = f.read()

themes_map = """
val Prefs.Theme.title: String
    get() = when (this) {
        Prefs.Theme.Dusk -> "Сумерки (Dusk)"
        Prefs.Theme.House -> "Уют (House)"
        Prefs.Theme.Hearth -> "Очаг (Hearth)"
        Prefs.Theme.Opera -> "Опера (Opera)"
        Prefs.Theme.Marquee -> "Огни рампы (Marquee)"
        Prefs.Theme.GreenRoom -> "Гримерная (Green room)"
        Prefs.Theme.Moonlight -> "Лунный свет (Moonlight)"
        Prefs.Theme.Graphite -> "Графит (Graphite)"
        Prefs.Theme.Cabaret -> "Кабаре (Cabaret)"
        Prefs.Theme.Aquarium -> "Аквариум (Aquarium)"
        Prefs.Theme.Absinthe -> "Полынь (Absinthe)"
        Prefs.Theme.Ultraviolet -> "Ультрафиолет (Ultraviolet)"
        Prefs.Theme.Blackout -> "Черный OLED (Blackout)"
        Prefs.Theme.HighContrast -> "Контрастная (High contrast)"
    }
"""

tagline_map = """
val Prefs.Theme.tagline: String
    get() = when (this) {
        Prefs.Theme.Dusk -> "Индиго и коралловый свет"
        Prefs.Theme.House -> "Теплая слива и ламповый свет"
        Prefs.Theme.Hearth -> "Умбра и огонь камина"
        Prefs.Theme.Opera -> "Красный бархат и золото"
        Prefs.Theme.Marquee -> "Морской синий и яркие огни"
        Prefs.Theme.GreenRoom -> "Глубокий изумруд и латунь"
        Prefs.Theme.Moonlight -> "Холодный сланец и лунный свет"
        Prefs.Theme.Graphite -> "Монохром и мягкий белый"
        Prefs.Theme.Cabaret -> "Фиолетовый и розовый неон"
        Prefs.Theme.Aquarium -> "Глубокий бирюзовый аквариум"
        Prefs.Theme.Absinthe -> "Оливковый и зелено-золотой"
        Prefs.Theme.Ultraviolet -> "Темный ультрафиолет"
        Prefs.Theme.Blackout -> "Абсолютно черный для OLED экранов"
        Prefs.Theme.HighContrast -> "Четкий текст и яркие границы"
    }
"""

import re
c = re.sub(r'val Prefs\.Theme\.title: String\s+get\(\) = when \(this\) \{[\s\S]*?\}', themes_map.strip(), c)
c = re.sub(r'val Prefs\.Theme\.tagline: String\s+get\(\) = when \(this\) \{[\s\S]*?\}', tagline_map.strip(), c)

with open(themes_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 3. Update Sheets.kt:
# Clean up theme/backdrop references
sheets_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Sheets.kt')
with open(sheets_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('value = theme.title.replace("Absinthe", "Полынь").replace("Blackout", "Черный").replace("High contrast", "Контрастная")', 'value = theme.title')
c = c.replace('val scenes = listOf(Triple(Prefs.STILL_BACKDROP, "Still", "The room\'s own light"))',
              'val scenes = listOf(Triple(Prefs.STILL_BACKDROP, "Статичный", "Естественный свет комнаты"))')
c = c.replace('value = scenes[sceneAt].second.replace("Still", "Статичный")', 'value = scenes[sceneAt].second')
c = c.replace('"Still while Lite mode or Reduce motion is on"', '"Статичный, пока включен режим Lite или отключены анимации"')

with open(sheets_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 4. Check Tiles.kt for "All apps" tile fallback
tiles_path = os.path.join(repo_dir, 'android/feature/home/src/main/kotlin/tv/lounge/feature/home/Tiles.kt')
with open(tiles_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('Text(tile.title, style = LoungeTheme.typography.title', 
              'Text(if (tile.id == "control:allapps") "Все приложения" else tile.title, style = LoungeTheme.typography.title')

with open(tiles_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Final polish applied successfully!")
