from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
Thanks for using {}
I can help you in many things regarding to fixed games. Am smart but you can still contact the **UFM administration** for farther help.
ADMIN [HERE](t.me/talktotegs)
**So now can I know your need ?**
Use below buttons for simplicity!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("DIRECT TO ADMIN", url="https://t.me/talktotegs")],
         [
            InlineKeyboardButton("BOOK NOW", callback_data="help"),
            InlineKeyboardButton("ABOUT US", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="t.me/+q1sRemgkxDJhMmRk")],  ]

    # Help Message
    HELP = """
**PLEASE CONTACT**

[ADMIN HERE](t.me/talktotegs)  💬

Order for fixed matches which are 100% secure with no chance of loosing.
    """

    # About Message
    ABOUT = """
**About This Bot** 

THS IS AN OFFICIAL UFM ASSISTANT BOT

It was developed for UFM clients who inbox UFM admins when offline. It replies instantly.
Guides you through aquiring fixed matches and free matches.

SUPPOSED BY : UFM MANAGEMENT
Main channel : [Click Here](t.me/ugfixedmatches)

Group : [Click Here](t.me/UFMfreematches)

Language : [ADMIN1](t.me/talktotegs) [ADMIN2](t.me/talktotegs2)

Developer : UFM MANAGEMENT
Version : 0.1.3.1
    """
