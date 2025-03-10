from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message
from fast_depends import Depends, inject

from callback_data import ShiftCarWashUpdateCallbackData
from config import Config
from dependencies.repositories import (
    get_car_wash_repository,
    get_shift_repository,
)
from exceptions import CarWashSameAsCurrentError
from filters import staff_filter
from repositories import CarWashRepository, ShiftRepository
from ui.views import (
    answer_text_view, ButtonText, ShiftCarWashUpdateView,
    ShiftMenuView,
)


__all__ = ('router',)

router = Router(name=__name__)


@router.callback_query(
    ShiftCarWashUpdateCallbackData.filter(),
    staff_filter,
    StateFilter('*'),
)
@inject
async def on_shift_car_wash_update(
        callback_query: CallbackQuery,
        callback_data: ShiftCarWashUpdateCallbackData,
        config: Config,
        shift_repository: ShiftRepository = Depends(
            dependency=get_shift_repository,
            use_cache=False,
        ),
) -> None:
    try:
        car_wash = await shift_repository.update_current_shift_car_wash(
            staff_id=callback_query.from_user.id,
            car_wash_id=callback_data.car_wash_id,
        )
    except CarWashSameAsCurrentError:
        await callback_query.answer(
            text='❌ Вы уже работаете на этой мойке',
            show_alert=True,
        )
        return
    await callback_query.message.edit_text(
        text=f'✅ Вы начали работу на мойке {car_wash.name}',
    )
    view = ShiftMenuView(
        staff_id=callback_query.from_user.id,
        web_app_base_url=config.web_app_base_url,
    )
    await answer_text_view(callback_query.message, view)


@router.message(
    F.text == ButtonText.SHIFT_CHANGE_CAR_WASH,
    staff_filter,
    StateFilter('*'),
)
@inject
async def on_show_car_washes_list(
        message: Message,
        car_wash_repository: CarWashRepository = Depends(
            dependency=get_car_wash_repository,
            use_cache=False,
        )
) -> None:
    car_washes = await car_wash_repository.get_all()
    view = ShiftCarWashUpdateView(car_washes)
    await answer_text_view(message, view)
