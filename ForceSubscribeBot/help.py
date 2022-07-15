from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.HELP,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
