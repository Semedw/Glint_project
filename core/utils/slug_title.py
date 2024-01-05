words = {
    'ǝ': 'e',
    'Ə': 'E',
    'I': 'i',
    'İ': 'I',
    'Ö': '0',
    'Ö': '0',
    'Ü': 'u',
    'Ü': 'U',
    'ğ': 'g',
    'Ğ': 'G',
    'ş': 's',
    'Ş': 'S',
    'ç': 'c',
    'Ç': 'C',
    ' ': '-',
    ',': '',
    '.': '',
    ':': '',
    ';': '',
    '!': '',
    '?': '',
    '(': '',
    ')': '',
    '[': '',
    ']': '',
    '{': '',
    '}': '',
    "'": '',
    '"': '',
    '|': '',
}


def generate_slug(title):
    for key, value in words.items():
        title = title.replace(key, value)

    return title.lower()