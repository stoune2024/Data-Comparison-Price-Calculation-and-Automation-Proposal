import re


def normalize(value: str) -> str:
    value = value.upper()

    value = re.sub(r"[^A-ZА-Я0-9]", "", value)

    return value
