foshes = (
    "khar",
    "gav",
    "ahmagh",
    "hoi",
    "hoy",
    "bishur",
    "bishor",
    "bishoor",
    "nafahm",
    "khafe sho",
    "khafesho",
    "sag",
    "jende",
    "sex",
    "fuck",
    "jish",
    "goh",
    "bemir",
    "lajan",
    "ashghal",
    "kheng",
    "boz",
    "khol",
    "ablah",
    "khari",
    "ahmaghi",
    "nafahmi",
    "gavi",
    "avazi",
)

def isFosh(fosh, data):
    if " " + fosh + " " in data or " " + fosh + "\r\n" in data or ":" + fosh + " " in data or ":" + fosh + "\r\n" in data:
        return True
    return False
