from pathlib import Path

from aiogram.contrib.middlewares.i18n import I18nMiddleware

I18N_DOMAIN = '{{cookiecutter.bot_name}}'

BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'

from typing import Any, Tuple
from aiogram import types
from core.db import db
from core.misc import dp


TEMPLATES = {
    'en': {'name': 'English'},
    'ru': {'name': 'Русский'},
}


class ACLMiddleware(I18nMiddleware):
    """
    Modified i18n middleware
    """

    async def get_user_locale(self, action: str, args: Tuple[Any]):
        """
        Load user from DB
        :param action:
        :param args:
        :return:
        """
        tg_user = types.User.get_current()
        if tg_user:
            user = (await db.accounts.find_one({'user_id': tg_user.id})) or {}
            if not user:
                if tg_user.language_code:
                    for lang in TEMPLATES:
                        if lang in tg_user.language_code:
                            return lang
        else:
            user = {}
        return user.get('lang', 'en')


i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
_ = i18n.gettext
__ = i18n.gettext  # ngettext

dp.middleware.setup(i18n)
