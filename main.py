# Turn off: __pycache__
import sys
sys.dont_write_bytecode = True


from config import CONFIG

import common.messages.buttons as button_msg
import common.messages.replies as reply_msg

from common.static.articles.fact import FACTS
from common.static.articles.whoami import WHOAMI

from common.objects.filter import TFilter

from common.utils.filter import apply_filter
from common.utils.keygen import keygen

from telebot.async_telebot import AsyncTeleBot
from telebot.types import KeyboardButton, Message, ReplyKeyboardMarkup
from typing import Any, Coroutine, Dict

import asyncio

import os
import random


USER_TO_RECENT_FILTER: Dict[str, TFilter] = {}


bot = AsyncTeleBot(token=CONFIG.TOKEN)

@bot.message_handler(commands=["start", "menu"])
async def menu(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2,
    )

    markup.add(
        KeyboardButton(button_msg.FILTER),
        KeyboardButton(button_msg.WHOAMI),
        KeyboardButton(button_msg.FACT),
        KeyboardButton(button_msg.PERCENT),
        KeyboardButton(button_msg.ABOUT),
        KeyboardButton(button_msg.FUND),
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.MENU,
        reply_markup=markup,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["about"])
async def about(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    path_to_image = "/".join([CONFIG.IMAGE_FODLER, "1.png"])
    with open(file=path_to_image, mode="rb") as file:
        image = file.read()

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image,
        caption=reply_msg.ABOUT,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["filter"])
async def filter(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2,
    )

    markup.add(
        KeyboardButton(button_msg.BILATERAL),
        KeyboardButton(button_msg.EMBOSS),
        KeyboardButton(button_msg.GAUSSIAN_BLUR),
        KeyboardButton(button_msg.GRAYSCALE),
        KeyboardButton(button_msg.INVERT),
        KeyboardButton(button_msg.RETRO),
        KeyboardButton(button_msg.MENU),
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.FILTER,
        reply_markup=markup,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["whoami"])
async def whoami(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    article = random.choice(WHOAMI)
    with open(file=article.path_to_image, mode="rb") as file:
        image = file.read()

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image,
        caption=f"\U000025AA\U0001F380 Сегодня ты... <b>{article.title}</b>",
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["percent"])
async def percent(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    monkey = random.choice(
        [
            "\U0001F412",
            "\U0001F98D",
            "\U0001F9A7",
        ]
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Ваше сходство с обезьяной составляет <b>{random.randint(0, 100)}%</b> {monkey}",
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["fact"])
async def fact(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    article = random.choice(FACTS)
    text = "\n\n".join(
        [
            f'<a href="{article.source}">\U000025AA <b>{article.title}</b> \U0001F4AC</a>',
            article.text,
        ],
    )

    with open(file=article.path_to_image, mode="rb") as file:
        image = file.read()

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image,
        caption=text,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["fund"])
async def fund(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    path_to_image = "/".join([CONFIG.IMAGE_FODLER, "2.png"])
    with open(file=path_to_image, mode="rb") as file:
        image = file.read()

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image,
        caption=reply_msg.FUND,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["bilateral"])
async def bilateral(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER[message.from_user.id] = TFilter.BILATERAL
    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.BILATERAL,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["emboss"])
async def emboss(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER[message.from_user.id] = TFilter.EMBOSS
    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.EMBOSS,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["blur"])
async def blur(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER[message.from_user.id] = TFilter.GAUSSIAN_BLUR
    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.GAUSSIAN_BLUR,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["grayscale"])
async def grayscale(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER[message.from_user.id] = TFilter.GRAYSCALE
    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.GRAYSCALE,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["invert"])
async def invert(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER[message.from_user.id] = TFilter.INVERT
    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.INVERT,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(commands=["retro"])
async def retro(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER[message.from_user.id] = TFilter.RETRO
    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.RETRO,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(content_types=["photo"])
async def image_handler(message: Message) -> Coroutine[Any, Any, Message]:
    """
    Downloading was implemented based on the answer from StackOverflow:
    https://stackoverflow.com/questions/42796300/get-photo-in-telegram-bot-through-pytelegrambotapi
    """

    filter = USER_TO_RECENT_FILTER.get(message.from_user.id, None)
    if filter is None:

        await bot.send_message(
            chat_id=message.chat.id,
            text=reply_msg.UNSELECTED_FILTER,
            parse_mode=CONFIG.PARSE_MODE,
        )
        
        return

    image_id = message.photo[-1].file_id
    image_info = await bot.get_file(image_id)

    download_path = image_info.file_path
    downloaded_image = await bot.download_file(download_path)

    path_to_image = "/".join(
        [
            CONFIG.TEMP_FOLDER,
            f"{keygen()}.png",
        ]
    )

    with open(file=path_to_image, mode="wb") as file:
        file.write(downloaded_image)

    apply_filter(path=path_to_image, filter=filter)

    with open(file=path_to_image, mode="rb") as file:
        filtered_image = file.read()

    os.remove(path_to_image)
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=filtered_image,
        caption=reply_msg.FILTERED,
        parse_mode=CONFIG.PARSE_MODE,
    )


@bot.message_handler(content_types=["text"])
async def handler(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)

    # --- --- --- --- --- Menu --- --- --- --- ---
    if message.text == button_msg.ABOUT:
        await about(message)

    elif message.text == button_msg.FACT:
        await fact(message)

    elif message.text == button_msg.FILTER:
        await filter(message)

    elif message.text == button_msg.PERCENT:
        await percent(message)

    elif message.text == button_msg.WHOAMI:
        await whoami(message)

    elif message.text == button_msg.FUND:
        await fund(message)

    # --- --- --- --- --- Filter --- --- --- --- ---
    elif message.text == button_msg.BILATERAL:
        await bilateral(message)

    elif message.text == button_msg.EMBOSS:
        await emboss(message)

    elif message.text == button_msg.GAUSSIAN_BLUR:
        await blur(message)

    elif message.text == button_msg.GRAYSCALE:
        await grayscale(message)

    elif message.text == button_msg.INVERT:
        await invert(message)

    elif message.text == button_msg.RETRO:
        await retro(message)

    elif message.text == button_msg.MENU:
        await menu(message)

    # --- --- --- --- --- Other --- --- --- --- ---
    else:
        await error(message)


@bot.message_handler()
async def error(message: Message) -> Coroutine[Any, Any, Message]:
    USER_TO_RECENT_FILTER.pop(message.from_user.id, None)
    await bot.send_message(
        chat_id=message.chat.id,
        text=reply_msg.ERROR,
        parse_mode=CONFIG.PARSE_MODE,
    )


asyncio.run(
    bot.infinity_polling()
)
