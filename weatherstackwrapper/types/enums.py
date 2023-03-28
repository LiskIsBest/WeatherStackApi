from enum import Enum


class Units(Enum):
    """https://weatherstack.com/documentation#units_parameter"""

    METRIC = "m"
    SCIENTIFIC = "s"
    FAHRENHEIT = "f"


class Language(Enum):
    """https://weatherstack.com/documentation#language_parameter"""

    ARABIC = "ar"
    BENGALI = "bn"
    BULGARIAN = "bg"
    CHINESE_SIMPLIFIED = "zh"
    CHINESE_TRADITIONAL = "zh_tw"
    CZECH = "cs"
    DANISH = "da"
    DUTCH = "nl"
    FINNISH = "fi"
    FRENCH = "fr"
    GERMAN = "de"
    GREEK = "el"
    HINDI = "hi"
    HUNGARIAN = "hu"
    ITALIAN = "it"
    JAPANESE = "ja"
    JAVANESE = "jv"
    KOREAN = "ko"
    MANDARIN = "zh_cmn"
    MARATHI = "mr"
    POLISH = "pl"
    PORTUGUES = "pt"
    PUNJABI = "pa"
    ROMANIAN = "ro"
    RUSSIAN = "ru"
    SERBIAN = "sr"
    SINHALESE = "si"
    SLOVAK = "sk"
    SPANISH = "es"
    SWEDISH = "sv"
    TAMIL = "ta"
    TELUGU = "te"
    TURKISH = "tr"
    UKRAINIAN = "uk"
    URDU = "ur"
    VIETNAMESE = "vi"
    WU = "zh_wuu"
    XIANG = "zh_hsn"
    YUE = "zh_yue"
    ZULU = "zu"
