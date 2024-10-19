from aiogram import Router

from . import menu

__all__ = ('router',)

router = Router(name=__name__)
router.include_router(menu.router)
