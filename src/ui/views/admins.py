from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
)

from ui.views.base import TextView
from ui.views.button_texts import ButtonText

__all__ = ('AdminMenuView', 'AdminShiftsMenuView', 'AdminOtherMenuView')


class AdminMenuView(TextView):
    text = '📲 Меню старшего смены'

    def __init__(self, web_app_base_url: str):
        self.__web_app_base_url = web_app_base_url

    def get_reply_markup(self) -> ReplyKeyboardMarkup:
        staff_register_requests_button = KeyboardButton(
            text=ButtonText.STAFF_REGISTER_REQUESTS,
            web_app=WebAppInfo(
                url=f'{self.__web_app_base_url}/register-requests',
            ),
        )
        return ReplyKeyboardMarkup(
            is_persistent=True,
            resize_keyboard=True,
            keyboard=[
                [
                    KeyboardButton(text=ButtonText.STAFF_LIST),
                    staff_register_requests_button,
                ],
                [
                    KeyboardButton(
                        text=ButtonText.SHIFTS_FOR_SPECIFIC_DATE,
                        web_app=WebAppInfo(
                            url=f'{self.__web_app_base_url}/shifts/confirm',
                        ),
                    ),
                    KeyboardButton(text=ButtonText.SHIFTS_ADMIN_MENU),
                    KeyboardButton(
                        text=ButtonText.CAR_WASH_LIST,
                        web_app=WebAppInfo(
                            url=f'{self.__web_app_base_url}/car-washes',
                        ),
                    ),
                ],
                [
                    KeyboardButton(text=ButtonText.PENALTY_CREATE_MENU),
                    KeyboardButton(text=ButtonText.SURCHARGE_CREATE_MENU),
                ],
                [
                    KeyboardButton(text=ButtonText.SUPERVISION_MENU),
                    KeyboardButton(
                        text=ButtonText.SHIFT_CARS_WITHOUT_WINDSHIELD_WASHER,
                    ),
                ],
                [
                    KeyboardButton(text=ButtonText.MAILING),
                    KeyboardButton(text=ButtonText.OTHER),
                ],
            ]
        )


class AdminShiftsMenuView(TextView):
    text = '📆 Меню графиков'

    def __init__(self, web_app_base_url: str, shifts_table_url: str):
        self.__web_app_base_url = web_app_base_url
        self.__shifts_table_url = shifts_table_url

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        available_dates_button = InlineKeyboardButton(
            text='📅 Открыть запись на смены',
            web_app=WebAppInfo(
                url=f'{self.__web_app_base_url}/shifts/available-dates',
            ),
        )
        shifts_edit_button = InlineKeyboardButton(
            text='✏️ Редактировать смены',
            web_app=WebAppInfo(
                url=f'{self.__web_app_base_url}/shifts/schedules',
            ),
        )
        shifts_table_url = InlineKeyboardButton(
            text='📊 Таблица',
            url=self.__shifts_table_url,
        )
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [available_dates_button],
                [shifts_edit_button],
                [shifts_table_url],
            ]
        )


class AdminOtherMenuView(TextView):
    text = '🔧 Другое'

    def __init__(self, web_app_base_url: str):
        self.__web_app_base_url = web_app_base_url

    def get_reply_markup(self) -> ReplyKeyboardMarkup:
        direct_shift = KeyboardButton(
            text=ButtonText.TEST_SHIFT_REQUEST,
            web_app=WebAppInfo(
                url=f'{self.__web_app_base_url}/shifts/direct',
            ),
        )
        reports_button = KeyboardButton(text=ButtonText.REPORTS)
        main_menu_button = KeyboardButton(text=ButtonText.MAIN_MENU)
        return ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=[
                [direct_shift],
                [reports_button],
                [main_menu_button],
            ],
        )
