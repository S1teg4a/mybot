# updates by @hiyaok on telegram
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone
from PyroUbot.config import OWNER_ID
from PyroUbot import *

@PY.UBOT("prem")
async def _(client, message):
    user = message.from_user 
    pt_id = await get_list_from_vars(bot.me.id, "PT_USERS")
    admin_id = await get_list_from_vars(bot.me.id, "ADMIN_USERS")
    seller_id = await get_list_from_vars(bot.me.id, "SELER_USERS")
    if user.id not in pt_id and user.id not in admin_id and user.id not in seller_id and user.id != OWNER_ID:
        return
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

    prem_users = await get_list_from_vars(bot.me.id, "PREM_USERS")

    if user.id in prem_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ꜱᴜᴅᴀʜ ᴘʀᴇᴍɪᴜᴍ</b>
<b>ᴇxᴘɪʀᴇᴅ: {get_bulan} ʙᴜʟᴀɴ</b></blockquote>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(bot.me.id, "PREM_USERS", user.id)
        await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴇxᴘɪʀᴇᴅ: {get_bulan} ʙᴜʟᴀɴ</b>
<b>ꜱɪʟᴀʜᴋᴀɴ ʙᴜᴋᴀ @{bot.me.username} ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ</b></blockquote>

<blockquote>✮ᴄᴀʀᴀ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ :
- sɪʟᴀʜᴋᴀɴ /start ᴅᴜʟᴜ ʙᴏᴛ @gaasubot
- ᴋᴀʟᴀᴜ sᴜᴅᴀʜ sᴛᴀʀᴛ ʙᴏᴛ ᴀʙɪsᴛᴜ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 
- ɴᴀʜ ɴᴀɴᴛɪ ᴀᴅᴀ ᴀʀᴀʜᴀɴ ᴅᴀʀɪ ʙᴏᴛ ɴʏᴀ ɪᴛᴜ ɪᴋᴜᴛɪɴ</blockquote>
<blockquote><b>ɴᴏᴛᴇ : ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ʙᴀᴄᴀ ᴀʀᴀʜᴀɴ ᴅᴀʀɪ ʙᴏᴛ ɴʏᴀ</b></blockquote>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"• ɪᴅ-ꜱᴇʟʟᴇʀ: `{message.from_user.id}`\n\n• ɪᴅ-ᴄᴜꜱᴛᴏᴍᴇʀ: `{user_id}`",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "⁉️ ꜱᴇʟʟᴇʀ",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "ᴄᴜꜱᴛᴏᴍᴇʀ ⁉️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unprem")
async def _(client, message):
    msg = await message.reply("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(bot.me.id, "PREM_USERS")

    if user.id not in prem_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴀꜰᴛᴀʀ</b></blockquote>
"""
        )
    try:
        await remove_from_vars(bot.me.id, "PREM_USERS", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.UBOT("getprem")
async def _(client, message):
    text = ""
    count = 0
    user = message.from_user
    pt_id = await get_list_from_vars(bot.me.id, "PT_USERS")
    admin_id = await get_list_from_vars(bot.me.id, "ADMIN_USERS")
    seller_id = await get_list_from_vars(bot.me.id, "SELER_USERS")
    if user.id not in pt_id and user.id not in admin_id and user.id not in seller_id and user.id != OWNER_ID:
        return
    prem = await get_list_from_vars(bot.me.id, "PREM_USERS")
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


@PY.UBOT("seles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    msg = await message.reply("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ꜱᴜᴅᴀʜ ʀᴇꜱᴇʟʟᴇʀ</b></blockquote>
"""
        )

    try:
        await add_to_vars(bot.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ʀᴇꜱᴇʟʟᴇʀ</b>
<b>ꜱɪʟᴀʜᴋᴀɴ ʙᴜᴋᴀ @{bot.me.username}</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unseles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    msg = await message.reply("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    seles_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if user.id not in seles_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴀꜰᴛᴀʀ</b></blockquote>
"""
        )

    try:
        await remove_from_vars(bot.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getseles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply("ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    seles_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if not seles_users:
        return await Sh.edit("ᴅᴀꜰᴛᴀʀ ꜱᴇʟʟᴇʀ ᴋᴏꜱᴏɴɢ")

    seles_list = []
    for user_id in seles_users:
        try:
            user = await client.get_users(int(user_id))
            seles_list.append(
                f"<blockquote>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | `{user.id}`</blockquote>"
            )
        except:
            continue

    if seles_list:
        response = (
            "📋 ᴅᴀꜰᴛᴀʀ ʀᴇꜱᴇʟʟᴇʀ:\n\n"
            + "\n".join(seles_list)
            + f"\n\n• ᴛᴏᴛᴀʟ ʀᴇꜱᴇʟʟᴇʀ: {len(seles_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀꜰᴛᴀʀ ꜱᴇʟʟᴇʀ")


@PY.UBOT("time")
async def _(client, message):
    user = message.from_user
    pt_id = await get_list_from_vars(bot.me.id, "PT_USERS")
    if user.id not in pt_id and user.id != OWNER_ID:
        return
    Tm = await message.reply("processing . . .")
    bajingan = message.command
    if len(bajingan) != 3:
        return await Tm.edit(f"Gunakan .time user_id hari")
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
    await Tm.edit(f"""<blockquote><b><emoji id=5215538577496090960>💬</emoji> INFORMATION
 ɴᴀᴍᴇ: {user.mention}
 ɪᴅ: {get_id}
 aktifkan_selama: {get_day} hari</b></blockquote>
"""
    )


@PY.UBOT("cek")
async def _(client, message):
    user = message.from_user
    pt_id = await get_list_from_vars(bot.me.id, "PT_USERS")
    if user.id not in pt_id and user.id != OWNER_ID:
        return
    Sh = await message.reply("ᴘʀᴏᴄᴇꜱꜱɪɴɢ . . .")
    user_id = await extract_user(message)
    if not user_id:
        return await Sh.edit("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴛᴇᴍᴜᴋᴀɴ")
    try:
        get_exp = await get_expired_date(user_id)
        sh = await client.get_users(user_id)
    except Exception as error:
        return await Sh.edit(error)
    if get_exp is None:
        await Sh.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: {sh.mention}</b>
<b>ɪᴅ: `{user_id}`</b>
<b>ᴘʟᴀɴ : ɴᴏɴᴇ</b>
<b>ᴘʀᴇꜰɪx : .</b>
<b>ᴇxᴘɪʀᴇᴅ : ɴᴏɴᴀᴋᴛɪꜰ</b></blockquote>
""")
    else:
        SH = await ubot.get_prefix(user_id)
        exp = get_exp.strftime("%d-%m-%Y")
        if user_id in await get_list_from_vars(bot.me.id, "ULTRA_PREM"):
            status = "SuperUltra"
        elif user_id in await get_list_from_vars(bot.me.id, "PREM_USERS"):
            status = "Premium"
        elif user_id in await get_list_from_vars(bot.me.id, "SELER_USERS"):
            status = "Seller"
        elif user_id in await get_list_from_vars(bot.me.id, "ADMIN_USERS"):
            status = "Admin"
        elif user_id in await get_list_from_vars(bot.me.id, "PT_USERS"):
            status = "PT"
        await Sh.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: {sh.mention}</b>
<b>ɪᴅ: `{user_id}`</b>
<b>ᴘʟᴀɴ : {status}</b>
<b>ᴘʀᴇꜰɪx : {' '.join(SH)}</b>
<b>ᴇxᴘɪʀᴇᴅ : {exp}</b></blockquote>
""")

@PY.UBOT("addpt")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    pt_users = await get_list_from_vars(bot.me.id, "PT_USERS")

    if user.id in pt_users:
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ</b></blockquote>
"""
        )

    try:
        await add_to_vars(bot.me.id, "PT_USERS", user.id)
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴘᴛ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unpt")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    pt_users = await get_list_from_vars(bot.me.id, "PT_USERS")

    if user.id not in pt_users:
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ</b></blockquote>
""")

    try:
        await remove_from_vars(bot.me.id, "PT_USERS", user.id)
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴜɴᴘᴛ</b></blockquote>
""")
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getpt")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply("sedang memproses...")
    pt_users = await get_list_from_vars(bot.me.id, "PT_USERS")

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
            "📋 ᴅᴀғᴛᴀʀ ᴘᴛ :\n\n"
            + "\n".join(pt_list)
            + f"\n\n⚜️ ᴛᴏᴛᴀʟ ᴘᴛ: {len(pt_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("tidak dapat mengambil daftar pt")
        
@PY.UBOT("addadmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ</b></blockquote>
"""
        )

    try:
        await add_to_vars(bot.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴀᴅᴍɪɴ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unadmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ</b></blockquote>
""")

    try:
        await remove_from_vars(bot.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
💬 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 :
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: {user.id}</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴜɴᴀᴅᴍɪɴ</b></blockquote>
""")
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getadmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply("sedang memproses...")
    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

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
            "📋 ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ :\n\n"
            + "\n".join(admin_list)
            + f"\n\n⚜️ ᴛᴏᴛᴀʟ ᴀᴅᴍɪɴ: {len(admin_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("tidak dapat mengambil daftar admin")

@PY.UBOT("addultra")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return await message.reply_text(f"{ggl}mau ngapain kamu ?")
    msg = await message.reply(f"{prs}sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl}{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    ultra_users = await get_list_from_vars(bot.me.id, "ULTRA_PREM")

    if user.id in ultra_users:
        return await msg.edit(f"{ggl}sudah menjadi superultra!")

    try:
        await add_to_vars(bot.me.id, "ULTRA_PREM", user.id)
        return await msg.edit(f"{brhsl}berhasil menjadi superultra")
    except Exception as error:
        return await msg.edit(error)

@PY.UBOT("cekvars")
async def _(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ Khusus OWNER.")

    msg = await message.reply("🔍 Mengambil data vars...")
    try:
        pt = await get_list_from_vars(bot.me.id, "PT_USERS") or []
        admin = await get_list_from_vars(bot.me.id, "ADMIN_USERS") or []
        seller = await get_list_from_vars(bot.me.id, "SELER_USERS") or []
        prem = await get_list_from_vars(bot.me.id, "PREM_USERS") or []

        return await msg.edit(f"""
<b>📦 VARS SAAT INI:</b>

👤 <b>PT USERS:</b> <code>{pt}</code>
👮 <b>ADMIN USERS:</b> <code>{admin}</code>
💰 <b>SELER USERS:</b> <code>{seller}</code>
🌟 <b>PREM USERS:</b> <code>{prem}</code>
""")
    except Exception as e:
        return await msg.edit(f"❌ Error saat mengambil vars:\n<code>{e}</code>")

@PY.UBOT("rmultra")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return await message.reply_text(f"{ggl}mau ngapain kamu ?")
    msg = await message.reply(f"{prs}sedang memproses...")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl}{message.text} user_id/username"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    ultra_users = await get_list_from_vars(bot.me.id, "ULTRA_PREM")

    if user.id not in ultra_users:
        return await msg.edit(f"{ggl}tidak ada di dalam database superultra")

    try:
        await remove_from_vars(bot.me.id, "ULTRA_PREM", user.id)
        return await msg.edit(f"{brhsl}berhasil di hapus dari daftar superultra")
    except Exception as error:
        return await msg.edit(error)
