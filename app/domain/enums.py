from enum import StrEnum


class MatchingStatus(StrEnum):
    MATCHED = "сопоставлено"
    MANUAL_REVIEW = "требуется ручная проверка"
    NOT_FOUND = "не найдено"
    NO_COST = "отсутствует себестоимость"
