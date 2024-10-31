from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from callback_data.prefixes import CallbackDataPrefix
from models import StaffToRegister
from views.base import TextView
from views.button_texts import ButtonText
from views.menu import MainMenuView

__all__ = (
    'StaffRegisterNotificationView',
    'StaffRegisterView',
    'StaffRegisterAcceptedView',
)


class StaffRegisterView(TextView):
    text = 'Зарегистрируйтесь, чтобы начать работу'

    def __init__(self, web_app_base_url: str):
        self.__web_app_base_url = web_app_base_url

    def get_reply_markup(self) -> ReplyKeyboardMarkup:
        url = f'{self.__web_app_base_url}/register'
        button = KeyboardButton(
            text=ButtonText.REGISTER,
            web_app=WebAppInfo(
                url=url,
            )
        )
        return ReplyKeyboardMarkup(keyboard=[[button]])


class StaffRegisterNotificationView(TextView):

    def __init__(self, staff: StaffToRegister, staff_id: int):
        self.__staff = staff
        self.__staff_id = staff_id

    def get_text(self) -> str:
        return (
            'Новый пользователь хочет зарегистрироваться\n'
            f'<b>🆔 ID:</b> {self.__staff_id}\n'
            f'<b>👤 ФИО:</b> {self.__staff.full_name}\n'
            '<b>📲 Номер телефона в каршеринге:</b>'
            f' {self.__staff.car_sharing_phone_number}\n'
            '<b>📲 Номер телефона в компании Консоль:</b>'
            f' {self.__staff.console_phone_number}'
        )

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        accept_button = InlineKeyboardButton(
            text='✅ Зарегистрировать',
            callback_data=CallbackDataPrefix.STAFF_REGISTER_ACCEPT,
        )
        reject_button = InlineKeyboardButton(
            text='❌ Отклонить',
            callback_data=CallbackDataPrefix.STAFF_REGISTER_REJECT,
        )
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [reject_button, accept_button],
            ],
        )


class StaffRegisterAcceptedView(TextView):
    text = '✅ Ваша заявка на регистрацию принята'
    reply_markup = MainMenuView.reply_markup


class StaffRegisterRejectedView(TextView):
    text = '❌ Ваша заявка на регистрацию отклонена'
