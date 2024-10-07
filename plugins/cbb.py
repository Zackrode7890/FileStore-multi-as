#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ɪɴᴛʀᴏᴠᴇʀᴛ</a>\n○ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Animes_Station'>Aɴɪᴍᴇ Sᴛᴀᴛɪᴏɴ</a>\n○ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/ongoing_anime_station'>Oɴɢᴏɪɴɢ AS</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/Anime_talk_station'>AS Cʜᴀᴛ</a>\n○ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ : <a href='https://t.me/AS_Networks'>AS Nᴇᴛᴡᴏʀᴋ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ɪɴᴅᴇx', url='https://t.me/Anime_Station_Index')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
