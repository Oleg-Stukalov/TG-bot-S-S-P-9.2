from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_en import LEXICON_EN
from keyboards.keyboard_utils import will_play_kbd, stone_scissors_paper_kbd
from random import randint


# Initialize module router
router = Router()

# Handler for /start command
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_EN['/start'],
                         reply_markup=will_play_kbd.as_markup(
                             resize_keyboard=True))


# Handler for /help command
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['/help'])


# Handler for button "Let's play"
@router.message(F.text == "Let's play")
async def process_lets_play_btn(message: Message):
    await message.answer(text="Good! Select your object!",
                         reply_markup=stone_scissors_paper_kbd.as_markup(
                             resize_keyboard=True))


# Handler for button "Do not want"
@router.message(F.text == "Do not want")
async def process_do_not_want_btn(message: Message):
    await message.answer(text="Ok. When you will want to play - open the "
                         "keyboard and click 'Let's play'",
                         reply_markup=will_play_kbd.as_markup(
                             resize_keyboard=True))


def _generate_stone_scissors_paper_random_answer() -> str:
    answers: list[str] = ['Stone', 'Scissors', 'Paper']
    return answers[randint(0, 2)]


def _game_result(arg1: str, arg2: str) -> str:
    if arg1 == "Stone":
        if arg2 == "Stone":
            return 'draw'
        elif arg2 == "Scissors":
            return 'player_1'
        elif arg2 == "Paper":
            return 'player_2'
    elif arg1 == "Scissors":
        if arg2 == "Stone":
            return 'player_2'
        elif arg2 == "Scissors":
            return 'draw'
        elif arg2 == "Paper":
            return 'player_1'
    elif arg1 == "Paper":
        if arg2 == "Stone":
            return 'player_1'
        elif arg2 == "Scissors":
            return 'player_2'
        elif arg2 == "Paper":
            return 'draw'


# Handler for button "Stone"
@router.message(F.text == "Stone")
async def process_stone_btn(message: Message):
    result = _game_result("Stone",
                          _generate_stone_scissors_paper_random_answer())
    answer = None
    if result == 'player_1':
        answer = 'Congratulation! You are the winner!'
    elif result == 'player_2':
        answer = 'Bot is the winner.'
    else:
        answer = 'The draw.'
    await message.answer(text=answer)
    await process_lets_play_btn(message) # Game restart


# Handler for button "Scissors"
@router.message(F.text == "Scissors")
async def process_scissors_btn(message: Message):
    result = _game_result("Scissors",
                          _generate_stone_scissors_paper_random_answer())
    answer = None
    if result == 'player_1':
        answer = 'Congratulation! You are the winner!'
    elif result == 'player_2':
        answer = 'Bot is the winner.'
    else:
        answer = 'The draw.'
    await message.answer(text=answer)
    await process_lets_play_btn(message) # Game restart


# Handler for button "Paper"
@router.message(F.text == "Paper")
async def process_paper_btn(message: Message):
    result = _game_result("Paper",
                          _generate_stone_scissors_paper_random_answer())
    answer = None
    if result == 'player_1':
        answer = 'Congratulation! You are the winner!'
    elif result == 'player_2':
        answer = 'Bot is the winner.'
    else:
        answer = 'The draw.'
    await message.answer(text=answer)
    await process_lets_play_btn(message) # Game restart


# Handler for other answer
@router.message()
async def process_other_answer(message: Message):
    await message.answer(text=LEXICON_EN['no_echo'])
