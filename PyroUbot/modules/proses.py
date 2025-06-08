import asyncio
from PyroUbot import *

__MODULE__ = "ᴘʀᴏꜱᴇꜱ"
__HELP__ = """
<b>🜲 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜱᴇꜱ</b>
<b>Penjelasan : Proses Transaksi.</b>

<blockquote>⎆ <b>Perintah</b> : <code>{0}proses</code> <b>[name item],[testi]</b></blockquote>
"""

@PY.UBOT("proses")
async def done_command(client, message):
    izzy_ganteng = await message.reply("<blockquote>🚀 Memproses</blockquote>")
    await asyncio.sleep(5)
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2 or "," not in args[1]:
            await message.reply_text("<blockquote>📚 Penggunaan: .proses [name item],[testi]</blockquote>")
            return

        parts = args[1].split(",", 1) 
        if len(parts) < 2: 
            await message.reply_text("<blockquote>📚 Penggunaan: .proses [name item],[testi]</blockquote>")
            return

        name_item = parts[0].strip()
        testi = parts[1].strip()
        response = (
            f"<b>✅️ Pesanan Diproses</b>\n"
            f"<blockquote>📦 <b>Barang : {name_item}</b>\n"
            f"👉 <b>Testimoni : {testi}</b></blockquote>\n\n"
            f"<b>Kami Sedang Mengerjakan Pesanan Anda, Mohon Tidak Spam Owner supaya Pesanan Lebih Cepat Diproses, Terima Kasih</b>\n"
            f"<blockquote><b>Userbot By @Sitegaax5</b></blockquote>\n\n"
        )
        await izzy_ganteng.edit(response)

    except Exception as e:
        await izzy_ganteng.edit(f"error: {e}")
