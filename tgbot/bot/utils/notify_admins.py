import logging
from aiogram import Bot
from django.conf import settings


async def on_startup_notify(bot: Bot):
    for admin in settings.ADMINS:
        try:
            bot_properties = await bot.me()
            message = ["<b>Bot ishga tushdi.</b>\n",
                       f"<b>Bot ID:</b> {bot_properties.id}",
                       f"<b>Bot Username:</b> @{bot_properties.username}"]
            await bot.send_message(int(admin), "\n".join(message))
        except Exception as err:
            logging.exception(err)
