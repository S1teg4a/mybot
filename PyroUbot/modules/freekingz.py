import random
import re
import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from PyroUbot import *

@PY.BOT("freedewa")
@PY.PRIVATE
async def _(client, message):
    buttons = BTN.PROMODEK(message)
    sh = await message.reply("""<u><b>𝗙𝗜𝗧𝗨𝗥 𝗙𝗥𝗘𝗘 SITEGAA 𝗨𝗦𝗘𝗥𝗕𝗢𝗧!</b></u>
<blockquote><b>/ai -  ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴍᴜ</b>
<b>/joko - ᴊᴏᴋᴏ ᴀɪ ʏᴀɪᴛᴜ ᴀɪ ʏᴀɴɢ ʙᴇʀʙᴀʜᴀsᴀ ᴊᴀᴡᴀ</b>
<b>/brat - ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇxᴛ ᴜɴᴛᴜᴋ ᴅɪ ᴊᴀᴅɪᴋᴀɴ ғᴏᴛᴏ</b>
<b>/adzan - ᴍᴀsᴜᴋᴋᴀɴ ᴋᴏᴛᴀ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴊᴀᴅᴡᴀʟ ᴀᴅᴢᴀɴ</b>
<b>/tourl - ʀᴇᴘʟʏ ғᴏᴛᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪ ᴊᴀᴅɪᴋᴀɴ ʟɪɴᴋ</b>
<b>/gempa - ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɪɴғᴏʀᴍᴀsɪ ɢᴇᴍᴘᴀ ᴛᴇʀᴋɪɴɪ ᴅɪ ɪɴᴅᴏɴᴇsɪᴀ</b>
<b>/tiktok - ʙᴇʀɪᴋᴀɴ ʟɪɴᴋ ᴠᴛ/ʟɪɴᴋ ғɪᴅɪᴏ ᴛɪᴋᴛᴏᴋ ᴜɴᴛᴜᴋ ᴅɪ ᴅᴏᴡɴʟᴏᴀᴅ</b></blockquote>

<blockquote><b>ᴏᴡɴᴇʀ ᴜsᴇʀʙᴏᴛ ᴅɪ ʙᴀᴡᴀʜ sɪɴɪʜ</b>
<b>ᴏᴡɴᴇʀ ᴜsᴇʀʙᴏᴛ: <a href=https://t.me/sitegaax>OWNER SITEGAA</a></b></blockquote>""", reply_markup=InlineKeyboardMarkup(buttons))
