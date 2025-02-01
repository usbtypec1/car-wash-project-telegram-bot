from collections.abc import Iterable

from aiogram.types import ForceReply, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import ui
from callback_data import SurchargeCreateChooseStaffCallbackData
from callback_data.prefixes import CallbackDataPrefix
from models import Staff, Surcharge
from ui.markups import create_confirm_reject_markup
from ui.views.base import TextView

__all__ = (
    'SurchargeCreateChooseStaffView',
    'SurchargeCreateInputReasonView',
    'SurchargeCreateConfirmView',
    'SurchargeCreateSuccessView',
    'SurchargeCreateInputAmountView',
)


class SurchargeCreateChooseStaffView(TextView):

    def __init__(self, staff_list: Iterable[Staff]):
        self.__staff_list = tuple(staff_list)

    def get_text(self) -> str:
        if not self.__staff_list:
            return ui.texts.NO_ANY_STAFF
        return 'Выберите Сотрудника'

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardBuilder()
        keyboard.max_width = 1

        for staff in self.__staff_list:
            keyboard.button(
                text=staff.full_name,
                callback_data=SurchargeCreateChooseStaffCallbackData(
                    staff_id=staff.id,
                ),
            )

        return keyboard.as_markup()


class SurchargeCreateInputReasonView(TextView):
    text = '📝 За что доплата?'
    reply_markup = ForceReply(input_field_placeholder='Причина доплаты')


class SurchargeCreateInputAmountView(TextView):
    text = '💰 Укажите размер доплаты'
    reply_markup = ForceReply(input_field_placeholder='Размер доплаты')


class SurchargeCreateConfirmView(TextView):
    reply_markup = create_confirm_reject_markup(
        confirm_callback_data=CallbackDataPrefix.SURCHARGE_CREATE_ACCEPT,
        reject_callback_data=CallbackDataPrefix.SURCHARGE_CREATE_REJECT,
    )

    def __init__(self, staff: Staff, reason: str, amount: int):
        self.__staff = staff
        self.__reason = reason
        self.__amount = amount

    def get_text(self) -> str:
        return (
            '❗️ Вы действительно хотите сделать доплату'
            f' сотруднику {self.__staff.full_name}'
            f' по причине <i>{self.__reason}</i>'
            f' в размере <b>{self.__amount}</b>?'
        )


class SurchargeCreateSuccessView(TextView):

    def __init__(self, surcharge: Surcharge, staff: Staff):
        self.__surcharge = surcharge
        self.__staff = staff

    def get_text(self) -> str:
        return (
            f'❗️ Сотруднику {self.__staff.full_name}'
            f' доплачено <b>{self.__surcharge.amount}</b>'
            f' по причине <i>{self.__surcharge.reason}</i>\n'
        )
