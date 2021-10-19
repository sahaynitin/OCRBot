from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
<b>Hey </b> {}\n
<b>I am Image to text Converter Bot. </b>\n
<b>✪ Use Help Command to Know how to Use me.</b>\n
<b><b>✪ Made With 💕 By </b>@Tellybots_4u</b>\n
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
<b>✪ Send Me Any Image to get started .</b>\n
<b>✪ I Can Provide Text from the Image Using ocr.</b>\n
<b>✪ It can Support Multiple image at a time </b>\n
<b>✪ Made With 💕 By @Tellybots_4u</b>\n
    """

    # About Message
    ABOUT = """
**About This Bot** 

Source Code : [Click Here](https://github.com/StarkBotsIndustries/OCRBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
