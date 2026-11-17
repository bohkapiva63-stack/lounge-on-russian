package tv.lounge.feature.home

import tv.lounge.design.LoungeColors
import tv.lounge.design.LoungeThemeVariant
import tv.lounge.design.colors
import tv.lounge.platform.Prefs

/** The rooms (DESIGN.md §3.1), as Settings and onboarding name them. */
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

fun Prefs.Theme.variant(): LoungeThemeVariant = LoungeThemeVariant.valueOf(name)

fun Prefs.Theme.palette(): LoungeColors = variant().colors()
