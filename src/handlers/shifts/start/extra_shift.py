import datetime

from aiogram import Bot, F, Router
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message
from fast_depends import inject

from callback_data import (
    ExtraShiftCreateAcceptCallbackData,
    ExtraShiftCreateRejectCallbackData,
)
from config import Config
from dependencies.repositories import (
    StaffRepositoryDependency,
)
from filters import admins_filter, staff_filter
from services.notifications import SpecificChatsNotificationService
from ui.views import (
    ButtonText, edit_as_rejected, ExtraShiftScheduleNotificationView,
    ExtraShiftScheduleWebAppView,
    MainMenuView, send_text_view, ShiftExtraStartRequestConfirmedView,
    ShiftExtraStartRequestSentView,
)
from ui.views.base import answer_view, edit_as_accepted
from ui.views.shifts.start import ShiftExtraStartRequestRejectedView


__all__ = ('router',)

router = Router(name=__name__)


@router.callback_query(
    ExtraShiftCreateAcceptCallbackData.filter(),
    admins_filter,
    StateFilter('*'),
)
@inject
async def on_extra_shift_create_accept(
        callback_query: CallbackQuery,
        callback_data: ExtraShiftCreateAcceptCallbackData,
        bot: Bot,
        staff_repository: StaffRepositoryDependency,
) -> None:
    staff = await staff_repository.get_by_id(callback_data.staff_id)
    view = ShiftExtraStartRequestConfirmedView(
        staff_full_name=staff.full_name,
        shift_date=datetime.date.fromisoformat(callback_data.date),
    )
    sent_messages = await send_text_view(bot, view, callback_data.staff_id)
    if sent_messages[0] is None:
        await callback_query.answer(
            text='❌ Не удалось отправить сообщение сотруднику',
            show_alert=True,
        )
    else:
        await edit_as_accepted(callback_query.message)


@router.callback_query(
    ExtraShiftCreateRejectCallbackData.filter(),
    admins_filter,
    StateFilter('*'),
)
async def on_extra_shift_create_reject(
        callback_query: CallbackQuery,
        callback_data: ExtraShiftCreateRejectCallbackData,
        bot: Bot,
) -> None:
    shift_date = datetime.date.fromisoformat(callback_data.date)
    view = ShiftExtraStartRequestRejectedView(shift_date=shift_date)
    await send_text_view(bot, view, callback_data.staff_id)
    await edit_as_rejected(callback_query.message)


@router.message(
    F.web_app_data.button_text == ButtonText.EXTRA_SHIFT_CALENDAR,
    staff_filter,
    StateFilter('*'),
)
@inject
async def on_extra_shift_calendar(
        message: Message,
        config: Config,
        admin_user_ids: set[int],
        bot: Bot,
        staff_repository: StaffRepositoryDependency,
) -> None:
    admins_notification_service = SpecificChatsNotificationService(
        bot=bot,
        chat_ids=admin_user_ids,
    )
    shift_date = datetime.date.fromisoformat(message.web_app_data.data)
    staff = await staff_repository.get_by_id(message.from_user.id)
    view = ExtraShiftScheduleNotificationView(
        staff_id=staff.id,
        staff_full_name=staff.full_name,
        shift_date=shift_date,
    )
    await admins_notification_service.send_view(view)
    view = ShiftExtraStartRequestSentView(shift_date)
    await answer_view(message, view)
    view = MainMenuView(
        staff_id=message.from_user.id,
        web_app_base_url=config.web_app_base_url,
    )
    await answer_view(message, view)


@router.message(
    F.text == ButtonText.SHIFT_START_EXTRA,
    staff_filter,
    StateFilter('*'),
)
async def on_start_extra_shift(message, config: Config):
    view = ExtraShiftScheduleWebAppView(config.web_app_base_url)
    await answer_view(message, view)
