from aiogram import Router

from . import (
    start,
    menu,
    cars_to_wash,
    errors,
    statistics,
    change_car_wash,
    finish,
    apply,
    schedule_self,
    extra_shift,
    direct,
)

__all__ = ('router',)

router = Router(name=__name__)
router.include_routers(
    apply.router,
    start.router,
    menu.router,
    cars_to_wash.router,
    errors.router,
    statistics.router,
    change_car_wash.router,
    finish.router,
    schedule_self.router,
    extra_shift.router,
    direct.router,
)
