import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ᴄʟᴏɴᴇ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʟᴏɴᴇ ⦫</b>
<blockquote>⎆ perintah :
ᚗ <code>{0}clone</code> @username
ᚗ <code>{0}clone</code> reply chat
⊶ Untuk MenClone Seorang User.

ᚗ <code>{0}clone restore</code>
⊶ Mengembalikan Profil asli.
</blockquote>
"""

# Penyimpanan identitas asli setiap user
STORAGE = {}

@PY.UBOT("clone")
async def impostor(client: Client, message: Message):
    user_id = message.from_user.id  
    inputArgs = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""
    moireX2 = ["@sitegaax", "@sitegaxx"]

    if inputArgs in moireX2:
        await message.edit("**[ᴋᴏɴᴛᴏʟ]** - Tidak dapat menyamar sebagai Developer😡")
        await client.send_message("@moire_logs", "**Maaf Telah MengClone Sitegaa 🥺**")
        return

    xx = await message.edit("`Memproses...`")

    # Jika perintah restore dijalankan
    if "restore" in inputArgs:
        if user_id not in STORAGE:
            return await xx.edit("**Anda harus meng-clone seseorang dulu sebelum mengembalikan identitas!**")

        await message.edit("**Mengembalikan Identitas Asli...**")
        await update_profile(client, STORAGE[user_id], restore=True)
        del STORAGE[user_id]
        return await xx.edit("**Berhasil mengembalikan akun Anda!**")

    # Mendapatkan userObj berdasarkan input atau reply
    if inputArgs:
        try:
            user = await client.get_users(inputArgs)
        except:
            return await xx.edit("**Nama pengguna/ID tidak valid.**")
        userObj = await client.get_chat(user.id)
    elif message.reply_to_message:
        reply_user = message.reply_to_message.from_user
        if not reply_user:
            return await xx.edit("**Tidak dapat menyamar sebagai admin anonim 🥺**")
        userObj = await client.get_chat(reply_user.id)
    else:
        return await xx.edit("**Gunakan .clone @username atau reply pesan pengguna.**")

    # Simpan identitas asli jika belum ada
    if user_id not in STORAGE:
        my_profile = await client.get_chat("me")
        my_photos = [p async for p in client.get_chat_photos("me")]
        STORAGE[user_id] = {"profile": my_profile, "photos": my_photos}

    await xx.edit("**Cloning Identitas...**")
    await update_profile(client, userObj)
    await xx.edit("**Cloning succes 😶‍🌫️**")

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
    
    # Cek apakah user premium
    user_info = await client.get_users(userObj.id)
    is_premium = user_info.is_premium if hasattr(user_info, "is_premium") else False

    # Batasi bio hanya untuk non-premium
    bio = userObj.bio if is_premium else (userObj.bio[:70] if userObj.bio else "")

    try:
        photos = [p async for p in client.get_chat_photos(userObj.id)]
        if photos:
            pfp = await client.download_media(photos[0].file_id)
            await client.set_profile_photo(photo=pfp)
    except:
        pass

    await client.update_profile(first_name=first_name, last_name=last_name, bio=bio)
