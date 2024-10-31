from exceptions import StaffRegisterTextParseError
from models import StaffToRegisterWithId

__all__ = ('parse_staff_register_text',)


def parse_staff_register_text(text: str) -> StaffToRegisterWithId:
    try:
        (
            _,
            telegram_id_line,
            full_name_line,
            car_sharing_phone_number_line,
            console_phone_number_line,
        ) = text.split('\n')
    except ValueError:
        raise StaffRegisterTextParseError

    try:
        telegram_id = int(
            telegram_id_line
            .removeprefix('🆔 ID:')
            .strip()
        )
    except ValueError:
        raise StaffRegisterTextParseError

    full_name = full_name_line.removeprefix('👤 ФИО:').strip()
    car_sharing_phone_number = (
        car_sharing_phone_number_line
        .removeprefix('📲 Номер телефона в каршеринге:')
        .strip()
    )
    console_phone_number = (
        console_phone_number_line
        .removeprefix('📲 Номер телефона в компании Консоль:')
        .strip()
    )
    return StaffToRegisterWithId(
        id=telegram_id,
        full_name=full_name,
        car_sharing_phone_number=car_sharing_phone_number,
        console_phone_number=console_phone_number,
    )
