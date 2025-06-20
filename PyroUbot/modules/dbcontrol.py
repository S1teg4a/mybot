from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone


from PyroUbot import *

__MODULE__ = "ᴅʙ ᴄᴏɴᴛʀᴏʟ"
__HELP__ = """
<blockquote><b>Bantuan Untuk DB Control</blockquote></b>

<blockquote><b>perintah : <code>{0}time</code>
    Untuk Menambah - Mengurangi Masa Aktif User</blockquote></b>

<blockquote><b>perintah : <code>{0}cek</code>
    Untuk Melihat Masa Aktif User</blockquote></b>

<blockquote><b>perintah : <code>{0}addadmin</code> - <code>{0}unadmin</code> - <code>{0}getadmin</code></blockquote></b>

<blockquote><b>perintah : <code>{0}seles</code> - <code>{0}unseles</code> - <code>{0}getseles</code></blockquote></b>
"""

@PY.BOT("prem")
@PY.SELLER
@PY.ADMIN
@PY.OWNER
@PY.PT
async def _(client, message):
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply("memproses...")
    if not user_id:
        return await msg.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʙᴜʟᴀɴ</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id in prem_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ꜱᴜᴅᴀʜ ᴘʀᴇᴍɪᴜᴍ</ci></b>
<b>ᴇxᴘɪʀᴇᴅ: {get_bulan} ʙᴜʟᴀɴ</b></blockquote>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(client.me.id, "PREM_USERS", user.id)
        await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴇxᴘɪʀᴇᴅ: {get_bulan} ʙᴜʟᴀɴ</b>
<b>ꜱɪʟᴀʜᴋᴀɴ ʙᴜᴋᴀ @{client.me.username} ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ</blockquote></b>

<blockquote>ᴄᴀʀᴀ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ :
- sɪʟᴀʜᴋᴀɴ /start ᴅᴜʟᴜ ʙᴏᴛ @Gaasubot
- ᴋᴀʟᴀᴜ sᴜᴅᴀʜ sᴛᴀʀᴛ ʙᴏᴛ ᴀʙɪsᴛᴜ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 
- ɴᴀʜ ɴᴀɴᴛɪ ᴀᴅᴀ ᴀʀᴀʜᴀɴ ᴅᴀʀɪ ʙᴏᴛ ɴʏᴀ ɪᴛᴜ ɪᴋᴜᴛɪɴ</blockquote>
<blockquote><b>ɴᴏᴛᴇ : ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ʙᴀᴄᴀ ᴀʀᴀʜᴀɴ ᴅᴀʀɪ ʙᴏᴛ ɴʏᴀ</b></blockquote>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"🆔 id-seller: {message.from_user.id}\n\n🆔 id-customer: {user_id}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 seller",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "customer ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unprem")
@PY.SELLER
@PY.ADMIN
@PY.OWNER
@PY.PT
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id not in prem_users:
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>ɪᴅ: {user.id}</b>
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀr</b></blockquote>
 """
        )
    try:
        await remove_from_vars(client.me.id, "PREM_USERS", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>ɪᴅ: {user.id}</b>
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴜɴᴘʀᴇᴍɪᴜᴍ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.BOT("getprem")
@PY.SELLER
@PY.ADMIN
@PY.OWNER
@PY.PT
async def _(client, message):
    text = ""
    count = 0
    prem = await get_list_from_vars(client.me.id, "PREM_USERS")
    prem_users = []

    for user_id in prem:
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"<blockquote><b>{userlist}\n</blockquote></b>"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)


@PY.BOT("seles")
@PY.ADMIN
@PY.OWNER
@PY.PT
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>ɪᴅ: {user.id}</b>
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: sᴜᴅᴀʜ sᴇʟʟᴇʀ</b></blockquote>
"""
        )

    try:
        await add_to_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 <b>ɪᴅ: {user.id}</b>
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: sᴇʟʟᴇʀ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unseles")
@PY.ADMIN
@PY.OWNER
@PY.PT
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} user_id/username</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id not in seles_users:
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 </b>ɪᴅ: {user.id}</b>
 </b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ</b></blockquote>
"""
        )

    try:
        await remove_from_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 <blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
 </b>ɪᴅ: {user.id}</b>
 </b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴜɴsᴇʟʟᴇʀ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getseles")
@PY.ADMIN
@PY.OWNER
@PY.PT
async def _(client, message):
    Sh = await message.reply("sedang memproses...")
    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if not seles_users:
        return await Sh.edit("daftar seller kosong")

    seles_list = []
    for user_id in seles_users:
        try:
            user = await client.get_users(int(user_id))
            seles_list.append(
                f"<blockquote><b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code></blockquote></b>"
            )
        except:
            continue

    if seles_list:
        response = (
            "📋 ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ:\n\n"
            + "\n".join(seles_list)
            + f"\n\n<blockquote.⚜️ ᴛᴏᴛᴀʟ sᴇʟʟᴇʀ: {len(seles_list)}</blockquote>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("tidak dapat mengambil daftar seller")


@PY.BOT("time")
@PY.OWNER
@PY.PT
async def _(client, message):
    Tm = await message.reply("processing . . .")
    bajingan = message.command
    if len(bajingan) != 3:
        return await Tm.edit(f"🗿ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ /ᴛɪᴍᴇ ᴜsᴇʀ_ɪᴅ ʜᴀʀɪ")
    user_id = int(bajingan[1])
    get_day = int(bajingan[2])
    print(user_id , get_day)
    try:
        get_id = (await client.get_users(user_id)).id
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"""
 ɪɴғᴏʀᴍᴀᴛɪᴏɴ :
 ɴᴀᴍᴇ: {user.mention}
 ɪᴅ: {get_id}
 aktifkan_selama: {get_day} hari
"""
    )


@PY.BOT("cek")
@PY.OWNER
@PY.PT
async def _(client, message):
    Sh = await message.reply("processing . . .")
    user_id = await extract_user(message)
    if not user_id:
        return await Sh.edit("pengguna tidak temukan")
    try:
        get_exp = await get_expired_date(user_id)
        sh = await client.get_users(user_id)
    except Exception as error:
        return await Sh.ediit(error)
    if get_exp is None:
        await Sh.edit(f"""
INFORMATION
ɴᴀᴍᴇ : {sh.mention}
ᴘʟᴀɴ : none
ɪᴅ : {user_id}
ᴘʀᴇғɪx : .
ᴇxᴘɪʀᴇᴅ : Nonaktif
""")
    else:
        SH = await ubot.get_prefix(user_id)
        exp = get_exp.strftime("%d-%m-%Y")
        if user_id in await get_list_from_vars(client.me.id, "ULTRA_PREM"):
            status = "SuperUltra"
        elif user_id in await get_list_from_vars(client.me.id, "PREM_USERS"):
            status = "Premium"
        elif user_id in await get_list_from_vars(client.me.id, "SELER_USERS"):
            status = "Seller"
        elif user_id in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
            status = "Admin"
        elif user_id in await get_list_from_vars(client.me.id, "PT_USERS"):
            status = "PT"
        await Sh.edit(f"""
INFORMATION
ɴᴀᴍᴇ : {sh.mention}
ᴘʟᴀɴ : {status}
ɪᴅ : {user_id}
ᴘʀᴇғɪx : {' '.join(SH)}
ᴇxᴘɪʀᴇᴅ : {exp}
""")

@PY.BOT("addpt")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    pt_users = await get_list_from_vars(client.me.id, "PT_USERS")

    if user.id in pt_users:
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ
""")

    try:
        await add_to_vars(client.me.id, "{PT_USERS", user.id)
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴘᴛ
""")
    except Exception as error:
        return await msg.edit(error)

@PY.BOT("unpt")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    pt_users = await get_list_from_vars(client.me.id, "PT_USERS")

    if user.id not in pt_users:
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ
""")

    try:
        await remove_from_vars(client.me.id, "PT_USERS", user.id)
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴜɴᴘᴛ
""")
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getpt")
@PY.OWNER
async def _(client, message):
    Sh = await message.reply("sedang memproses...")
    pt_users = await get_list_from_vars(client.me.id, "PT_USERS")

    if not pt_users:
        return await Sh.edit("<s>ᴅᴀғᴛᴀʀ ᴘᴛ ᴋᴏsᴏɴɢ</s>")

    pt_list = []
    for user_id in pt_users:
        try:
            user = await client.get_users(int(user_id))
            pt_list.append(
                f"👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except:
            continue

    if pt_list:
        response = (
            "📋 ᴅᴀғᴛᴀʀ ᴘᴛ:\n\n"
            + "\n".join(pt_list)
            + f"\n\n⚜️ ᴛᴏᴛᴀʟ ᴘᴛ: {len(pt_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("tidak dapat mengambil daftar PT")

@PY.BOT("addadmin")
@PY.OWNER
@PY.PT
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ
""")

    try:
        await add_to_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴀᴅᴍɪɴ
""")
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unadmin")
@PY.OWNER
@PY.PT
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ
""")

    try:
        await remove_from_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
💬 INFORMATION
ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ: {user.id}
ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴜɴᴀᴅᴍɪɴ
""")
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getadmin")
@PY.OWNER
@PY.PT
async def _(client, message):
    Sh = await message.reply("sedang memproses...")
    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if not admin_users:
        return await Sh.edit("<s>ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ ᴋᴏsᴏɴɢ</s>")

    admin_list = []
    for user_id in admin_users:
        try:
            user = await client.get_users(int(user_id))
            admin_list.append(
                f"👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except:
            continue

    if admin_list:
        response = (
            "📋 ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ:\n\n"
            + "\n".join(admin_list)
            + f"\n\n⚜️ ᴛᴏᴛᴀʟ ᴀᴅᴍɪɴ: {len(admin_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("tidak dapat mengambil daftar admin")

@PY.BOT("superultra")
@PY.OWNER
async def _(client, message):
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply("memproses...")
    if not user_id:
        return await msg.edit(f"{message.text} user_id/username")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(client.me.id, "ULTRA_PREM")

    if user.id in prem_users:
        return await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> {user.id}
<b>keterangan: sudah</b> <code>[SuperUltra]</code>
<b>expired:</b> <code>{get_bulan}</code> <b>bulan</b>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(client.me.id, "ULTRA_PREM", user.id)
        await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> <code>{user.id}</code>
<b>expired:</b> <code>{get_bulan}</code> <b>bulan</b>
<b>ꜱilahkan buka</b> @{client.me.mention} <b>untuk membuat uꜱerbot</b>
<b>status : </b><code>[SuperUltra]</code>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"🆔 id-seller: {message.from_user.id}\n\n🆔 id-customer: {user_id}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 seller",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "customer ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)

@PY.BOT("rmultra")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(client.me.id, "ULTRA_PREM")

    if user.id not in prem_users:
        return await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> <code>{user.id}</code>
<b>keterangan: tidak dalam daftar</b>
"""
        )
    try:
        await remove_from_vars(client.me.id, "ULTRA_PREM", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
<b>name:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>id:</b> <code>{user.id}</code>
<b>keterangan: none superultra</b>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.BOT("getultra")
@PY.OWNER
async def _(client, message):
    prem = await get_list_from_vars(client.me.id, "ULTRA_PREM")
    prem_users = []

    for user_id in prem:
        try:
            user = await client.get_users(user_id)
            prem_users.append(
                f"👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except Exception as error:
            return await message.reply(str(error))

    total_prem_users = len(prem_users)
    if prem_users:
        prem_list_text = "\n".join(prem_users)
        return await message.reply(
            f"📋 daftar superultra:\n\n{prem_list_text}\n\n⚜️ total superultra: {total_prem_users}"
        )
    else:
        return await message.reply("tidak ada pengguna superultra saat ini")
