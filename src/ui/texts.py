from typing import Final

__all__ = (
    'ACCEPT',
    'REJECT',
    'format_accept_text',
    'format_reject_text',
    'NO_ANY_STAFF',
    'BACK',
)

ACCEPT: Final[str] = '✅ Подтвердить'
REJECT: Final[str] = '❌ Отклонить'
ACCEPTED: Final[str] = '✅ Подтверждено'
REJECTED: Final[str] = '❌ Отклонено'
NO_ANY_STAFF: Final[str] = '😔 Нет сотрудников'
BACK: Final[str] = '🔙 Назад'


def format_accept_text(existing_text: str) -> str:
    return f'{existing_text}\n\n<i>{ACCEPTED}</i>'


def format_reject_text(existing_text: str) -> str:
    return f'{existing_text}\n\n<i>{REJECTED}</i>'
