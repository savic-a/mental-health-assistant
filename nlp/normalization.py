import re


def normalize(text: str) -> str:
    text = text.lower()
    text = remove_punctuation(text)
    text = remove_extra_spaces(text)
    return text


def remove_punctuation(text: str) -> str:
    # ^ = not
    # \w = letter and numbers
    # \s = space
    return re.sub(r"[^\w\s]", "", text)


def remove_extra_spaces(text: str) -> str:
    # whitespace array replace with " "
    return re.sub(r"\s+", " ", text).strip()