from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🥱 ᴘᴀᴜsᴇ 🥱",
            description=f"Pause the current playing song on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 ʀᴇsᴜᴍᴇ 😋",
            description=f"Resume the current playing song on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="😐 ᴍᴜᴛᴇ 😐",
            description=f"Mute the Assistant on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="😁 ᴜɴᴍᴜᴛᴇ 😁",
            description=f"Unmute the Assistant on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="🤨 sᴋɪᴘ 🤨",
            description=f"Skip to next song in queue. | For skipping to a track in queue : /skip [number] ",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 ᴇɴᴅ 🥺",
            description="Clears the queue and leave VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🙄 sʜᴜꜰꜰʟᴇ 🙄",
            description="Shuffle between the tracks in queue.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="😴 sᴇᴇᴋ 😴",
            description="Seek the ongoing stream to a specific duration.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="🤯 ʟᴏᴏᴘ 🤯",
            description="Loop the current playing music. | Example : /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
