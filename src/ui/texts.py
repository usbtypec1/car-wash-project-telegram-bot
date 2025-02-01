from typing import Final

__all__ = (
    'CONFIRM',
    'REJECT',
    'format_confirm_text',
    'format_reject_text',
    'NO_ANY_STAFF',
    'BACK',
)

CONFIRM: Final[str] = '✅ Подтвердить'
REJECT: Final[str] = '❌ Отклонить'
CONFIRMED: Final[str] = '✅ Подтверждено'
REJECTED: Final[str] = '❌ Отклонено'
NO_ANY_STAFF: Final[str] = '😔 Нет сотрудников'
BACK: Final[str] = '🔙 Назад'


def format_confirm_text(existing_text: str) -> str:
    return f'{existing_text}\n\n<i>{CONFIRMED}</i>'


def format_reject_text(existing_text: str) -> str:
    return f'{existing_text}\n\n<i>{REJECTED}</i>'
