from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from Tianabot import pbot, START_IMG, SUPPORT_CHAT, BOT_NAME, OWNER_USERNAME


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""✨ **Hey I'm** {BOT_NAME}

**Owner : [Click Here](https://t.me/{OWNER_USERNAME})**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

**Click on Button Bellow For More**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="࿈𝑴𝒐𝒓𝒆 𝑩𝒐𝒕𝒔", url="https://t.me/NightVission"), 
                    InlineKeyboardButton(
                        "࿈𝑺𝒖𝒑𝒑𝒐𝒓𝒕", url=f"https://t.me/{SUPPORT_CHAT}")
                ]
            ]
        )
    )
