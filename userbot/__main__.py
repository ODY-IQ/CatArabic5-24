#from telethon.tl.functions.messages import GetMessagesViewsRequest
#import sys, asyncio

import contextlib
import sys
import userbot
#from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

#from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import catub
#from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    mybot,
    saves,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)
LOGS = logging.getLogger("CatArabic")
print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)
cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info("بدأ تنزيل ملفات اليوزربوت")
    catub.loop.run_until_complete(setup_bot())
    LOGS.info("اكتمل تنزيل ملفات اليوزربوت")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()
    
try:
    LOGS.info("يتم تفعيل وضع حمايه الحساب من الاختراق")
    catub.loop.create_task(saves())
    LOGS.info("تم تفعيل وضع حمايه الحساب من الاختراق")
except Exception as bb:
    LOGS.error(f"- {bb}")
    sys.exit()


try:
    LOGS.info("يتم تفعيل وضع الانلاين")
    catub.loop.run_until_complete(mybot())
    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")
except Exception as meo:
    LOGS.error(f"- {meo}")
    sys.exit()


async def startup_process():
    if catub.uid in blacklisted_users:
        LOGS.info("انت لا يمكنك تنصيب سورس جمثون عزيزي دي")
        return
    if not gvarstatus("TNSEEB"):
        try:
            await verifyLoggerGroup()
            await load_plugins("plugins")
            await load_plugins("assistant")
            LOGS.info("============================================================")
            LOGS.info("تم انتهاء عملية التنصيب بنجاح")
            LOGS.info(
                f"لمعرفة اوامر السورس ارسل {cmdhr}الاوامر\
                \nمجموعة قناة السورس  https://t.me/jmthon_support"
            )
            LOGS.info("============================================================")
            await verifyLoggerGroup()
            await add_bot_to_logger_group(BOTLOG_CHATID)
            if PM_LOGGER_GROUP_ID != -100:
                await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
            await startupmessage()
            return
        except Exception as e:
            LOGS.info(str(e))
            return
    else:
        LOGS.info("انت لا يمكنك تنصيب سورس جمثون عزيزي دي")
        LOGS.info("انت لا يمكنك تنصيب سورس جمثون عزيزي دي")
        LOGS.info("انت لا يمكنك تنصيب سورس جمثون عزيزي دي")



catub.loop.run_until_complete(startup_process())


if len(sys.argv) not in (1, 3, 4):
   with contextlib.suppress(ConnectionError):
        catub.run_until_disconnected()
else:
    catub.disconnect()
