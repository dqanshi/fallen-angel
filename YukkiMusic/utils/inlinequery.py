from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ð¥± á´á´á´sá´ ð¥±",
            description=f"Pause the current playing song on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ð Êá´sá´á´á´ ð",
            description=f"Resume the current playing song on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ð á´á´á´á´ ð",
            description=f"Mute the Assistant on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="ð á´É´á´á´á´á´ ð",
            description=f"Unmute the Assistant on VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="ð¤¨ sá´Éªá´ ð¤¨",
            description=f"Skip to next song in queue. | For skipping to a track in queue : /skip [number] ",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ð¥º á´É´á´ ð¥º",
            description="Clears the queue and leave VC.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="ð sÊá´ê°ê°Êá´ ð",
            description="Shuffle between the tracks in queue.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="ð´ sá´á´á´ ð´",
            description="Seek the ongoing stream to a specific duration.",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="ð¤¯ Êá´á´á´ ð¤¯",
            description="Loop the current playing music. | Example : /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/abed92d9b3ff409793324.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
