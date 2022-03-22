from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
**ʀʏᴛʜᴍx ʟᴏɢ**

**ᴄʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
**ᴜsᴇʀ:** {message.from_user.mention}
**ᴜsᴇʀɴᴀᴍᴇ:** @{message.from_user.username}
**ɪᴅ:** `{message.from_user.id}`
**ʟɪɴᴋ:** {chatusername}

**ǫᴜᴇʀʏ:** {message.text}

**ᴛʏᴩᴇ:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
