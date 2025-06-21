from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ 𝑷𝒆𝒎𝒃𝒆𝒓𝒊𝒕𝒂𝒉𝒖𝒂𝒏</b>
<b>├ 𝑨𝒌𝒖𝒏:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ 𝑰𝑫:</b> <code>{X.me.id}</code>
<b>╰ 𝑴𝒂𝒔𝒂 𝒂𝒌𝒕𝒊𝒇 𝒕𝒆𝒍𝒂𝒉 𝒉𝒂𝒃𝒊𝒔</b></blockquote>
"""

    def START(message):
        return f"""
<b>Halo 👋🏻  <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a></b>❕
<blockquote><b>📚 {bot.me.mention} adalah Bot multi client yang dapat membuat userbot dengan sangat mudah.</b>

<b>✨ Bot ini di kembangkan oleh: @iRayneone, Bot ini di rancang untuk memudahkan pengguna telegram untuk mengirim pesan group&user telegram dengan instant, Dan memiliki banyak fitur yang berguna lainnya.</b></blockquote>
<b>👉 Silahkan pilih salah satu tombol di bawah ini❗</b>
<b>- Jika ada kendala silahkan hubungi pengembang.</b>"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 𝑺𝒊𝒍𝒂𝒉𝒌𝒂𝒏 𝒎𝒆𝒍𝒂𝒌𝒖𝒌𝒂𝒏 𝒑𝒆𝒎𝒃𝒂𝒚𝒂𝒓𝒂𝒏 𝒕𝒆𝒓𝒍𝒆𝒃𝒊𝒉 𝒅𝒂𝒉𝒖𝒍𝒖</b>

<b>𝙽𝙾𝙿𝙴 𝙶𝙾-𝙿𝙰𝚈 : 082136836348</b>
<b>𝚀𝚁𝙸𝚂 𝙰𝙻𝙻 𝙿𝙰𝚈 : https://files.catbox.moe/ku1888.jpg</b>

<b>⌭ 𝑲𝒍𝒊𝒌 𝒕𝒐𝒎𝒃𝒐𝒍 𝒌𝒐𝒏𝒇𝒊𝒓𝒎𝒂𝒔𝒊 𝒖𝒏𝒕𝒖𝒌 𝒌𝒊𝒓𝒊𝒎 𝒃𝒖𝒌𝒕𝒊 𝒑𝒆𝒎𝒃𝒂𝒚𝒂𝒓𝒂𝒏 𝒂𝒏𝒅𝒂</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>⌬ 𝑼𝒔𝒆𝒓𝒃𝒐𝒕 𝒌𝒆</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ 𝑨𝒌𝒖𝒏:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ╰ 𝑰𝑫:</b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """
𝑷𝒆𝒏𝒈𝒈𝒖𝒏𝒂𝒂𝒏 𝒖𝒔𝒆𝒓𝒃𝒐𝒕 𝒚𝒂𝒏𝒈 𝒂𝒎𝒂𝒏 𝒅𝒊𝒂𝒏𝒋𝒖𝒓𝒌𝒂𝒏 𝒅𝒊𝒑𝒂𝒔𝒂𝒏𝒈 𝒅𝒊 𝒂𝒌𝒖𝒏 𝑰𝑫 𝒂𝒘𝒂𝒍𝒂𝒏 1–5
𝒔𝒆𝒎𝒖𝒂 𝒑𝒆𝒏𝒈𝒈𝒖𝒏𝒂 𝒅𝒂𝒓𝒊 𝑰𝑫 𝒕𝒆𝒓𝒔𝒆𝒃𝒖𝒕 𝒔𝒖𝒅𝒂𝒉 𝒕𝒆𝒓𝒃𝒊𝒍𝒂𝒏𝒈 𝒂𝒎𝒂𝒏, 𝒕𝒂𝒑𝒊 𝒔𝒆𝒎𝒖𝒂 𝒕𝒆𝒓𝒈𝒂𝒏𝒕𝒖𝒏𝒈 𝒑𝒆𝒎𝒂𝒌𝒂𝒊𝒂𝒏 𝒌𝒂𝒍𝒊𝒂𝒏
⚠️ 𝑼𝒏𝒕𝒖𝒌 𝒑𝒆𝒏𝒈𝒈𝒖𝒏𝒂 𝒖𝒔𝒆𝒓𝒃𝒐𝒕 𝒕𝒊𝒅𝒂𝒌 𝒅𝒊𝒔𝒂𝒓𝒂𝒏𝒌𝒂𝒏 𝒎𝒆𝒎𝒂𝒌𝒂𝒊 𝑰𝑫 𝒂𝒘𝒂𝒍𝒂𝒏 𝟼–𝟽 𝒌𝒂𝒓𝒆𝒏𝒂 𝒔𝒂𝒏𝒈𝒂𝒕 𝒓𝒂𝒘𝒂𝒏 𝒋𝒊𝒌𝒂 𝒅𝒊𝒑𝒂𝒔𝒂𝒏𝒈 𝒖𝒔𝒆𝒓𝒃𝒐𝒕
"""
