import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ᴄʟᴏɴᴇ ᴜsᴇʀɴᴀᴍᴇ"
__HELP__ = """
<blockquote><b>📚 Folder Untuk Clone Username

🚦 Perintah : {0}clone @username
🦠 Penjelasan : Untuk MenClone Seseorang User.
🚦 Perintah : {0}clone restore 
🦠 Penjelasan : Untuk Mengembalikan Kamu Ke Identitas Sebelumnya.</b></blockquote>
"""

STORAGE = {}

@PY.UBOT("clone")
async def impostor(client: Client, message: Message):
    user_id = message.from_user.id  
    inputArgs = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""
    WannX2 = ["@Sitegaax"]

    if inputArgs in WannX2:
        await message.edit("<blockquote><b>❌ [Kontol] - Tidak dapat menyamar sebagai Developer Sitegaa😡</b></blockquote>")
        await client.send_message("<blockquote><b> @Spubotme", "Maaf Telah MengClone Sitegaa 🥺</b></blockquote>")
        return

    xx = await message.edit("<blockquote><b>⏰ Memproses...</b></blockquote>")

    if "restore" in inputArgs:
        if user_id not in STORAGE:
            return await xx.edit("<blockquote><b>📑 Anda harus meng-clone seseorang dulu sebelum mengembalikan identitas!</b></blockquote>")

        await message.edit("<blockquote><b>⏰ Mengembalikan Identitas Asli...</b></blockquote>")
        await update_profile(client, STORAGE[user_id], restore=True)
        del STORAGE[user_id]
        return await xx.edit("<blockquote><b>📑 Berhasil mengembalikan akun Anda!</b></blockquote>")

    if inputArgs:
        try:
            user = await client.get_users(inputArgs)
        except:
            return await xx.edit("<blockquote><b>❌ Nama pengguna/ID tidak valid.</b></blockquote>")
        userObj = await client.get_chat(user.id)
    elif message.reply_to_message:
        reply_user = message.reply_to_message.from_user
        if not reply_user:
            return await xx.edit("<blockquote><b>❌ Tidak dapat menyamar sebagai admin anonim 🥺</b></blockquote>")
        userObj = await client.get_chat(reply_user.id)
    else:
        return await xx.edit("<blockquote><b>❌ Gunakan .clone @username atau reply pesan pengguna.</b></blockquote>")

    if user_id not in STORAGE:
        my_profile = await client.get_chat("me")
        my_photos = [p async for p in client.get_chat_photos("me")]
        STORAGE[user_id] = {"profile": my_profile, "photos": my_photos}

    await xx.edit("<blockquote><b>Mencuri Identitas Si Goblok...</b></blockquote>")
    await update_profile(client, userObj)
    await xx.edit("<blockquote><b>Aowkaowkw Gw Jadi Lu Ni, Lu Clone Gw Ya🥴</b></blockquote>")


async def update_profile(client: Client, userObj, restore=False):
    if restore:
        profile_data = userObj["profile"]
        photos = userObj["photos"]

        await client.update_profile(
            first_name=profile_data.first_name or "Deleted Account",
            last_name=profile_data.last_name or "",
            bio=profile_data.bio or ""
        )

        if photos:
            try:
                pfp = await client.download_media(photos[0].file_id)
                await client.set_profile_photo(photo=pfp)
            except:
                pass
        return

    first_name = userObj.first_name or "Deleted Account"
    last_name = userObj.last_name or ""
    
    user_info = await client.get_users(userObj.id)
    is_premium = user_info.is_premium if hasattr(user_info, "is_premium") else False

    bio = userObj.bio if is_premium else (userObj.bio[:70] if userObj.bio else "")

    try:
        photos = [p async for p in client.get_chat_photos(userObj.id)]
        if photos:
            pfp = await client.download_media(photos[0].file_id)
            await client.set_profile_photo(photo=pfp)
    except:
        pass

    await client.update_profile(first_name=first_name, last_name=last_name, bio=bio)
