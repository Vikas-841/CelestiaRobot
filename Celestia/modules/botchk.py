import asyncio
from pyrogram import filters
from Celestia import Celestia, userbot
from config import SUDO_USERS

BOT_LIST = ["CelestiaXBot", "ZuliAiBot"]



@Celestia.on_message(filters.command("botschk") & filters.user(SUDO_USERS))
async def bots_chk(celestia, message):
    msg = await message.reply_photo(photo="https://telegra.ph/file/48578068b7574bb25a529.jpg", caption="**ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ...**")
    response = "**ʙᴏᴛs sᴛᴀᴛᴜs ᴅᴇᴀᴅ ᴏʀ ᴀʟɪᴠᴇ ᴄʜᴇᴄᴋᴇʀ**\n\n"
    for bot_username in BOT_LIST:
        try:
            bot = await userbot.get_users(bot_username)
            bot_id = bot.id
            await asyncio.sleep(0.5)
            bot_info = await userbot.send_message(bot_id, "/start")
            await asyncio.sleep(3)
            async for bot_message in userbot.get_chat_history(bot_id, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**\n\n"
                else:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴇʀʀᴏʀ ❌**\n"
    
    await msg.edit_text(response)




