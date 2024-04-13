from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder



# Create buttons template for will_play_kbd
will_play_kbd_buttons: list[list[KeyboardButton]] = [
    KeyboardButton(text="Let's play"),
    KeyboardButton(text="Do not want")
]

# Create will_play_kbd
will_play_kbd = ReplyKeyboardBuilder()
will_play_kbd.row(*will_play_kbd_buttons, width=2)


# Create buttons template for stone_scissors_paper_kbd
stone_scissors_paper_kbd_buttons: list[list[KeyboardButton]] = [
    KeyboardButton(text="Stone"),
    KeyboardButton(text="Scissors"),
    KeyboardButton(text="Paper")
]

# Create stone_scissors_paper_kbd
stone_scissors_paper_kbd = ReplyKeyboardBuilder()
stone_scissors_paper_kbd.row(*stone_scissors_paper_kbd_buttons, width=3)