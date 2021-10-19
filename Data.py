from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hi {}

I am Image To Text Converter Bot

I can help you to extract text from images using ocr technology.

Made With 💕 By @Tellybots_4u
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @StarkBots.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Source Code : [Click Here](https://github.com/StarkBotsIndustries/OCRBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
