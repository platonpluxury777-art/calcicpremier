from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, MessageEntity
from aiogram.enums import MessageEntityType
import asyncio

TOKEN = "8915592143:AAHG2dv6Vip0h9tmwYlp-99JAD9a9jBoTpo"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ID группы
ALLOWED_GROUP_ID = -1003876522272

# Premium emoji ID
PREMIUM_EMOJI_ID = "5271837459783638319"


# ---------- ПРИВЕТСТВИЕ ----------
@dp.message(F.new_chat_members)
async def welcome(message: Message):

    for user in message.new_chat_members:

        # если добавили именно бота
        if user.id == (await bot.me()).id:

            text = (
                "↔️ Добро пожаловать!\n\n"
                "Бот работает только в группе PREMIER ORDERS\n\n"
                "https://t.me/premier_orders"
            )

            entities = [
                MessageEntity(
                    type=MessageEntityType.CUSTOM_EMOJI,
                    offset=0,
                    length=2,
                    custom_emoji_id=PREMIUM_EMOJI_ID
                )
            ]

            await message.answer(
                text=text,
                entities=entities
            )


# ---------- КАЛЬКУЛЯТОР ----------
@dp.message()
async def calculator(message: Message):

    # работает только в нужной группе
    if message.chat.id != ALLOWED_GROUP_ID:
        return

    text = message.text.replace(" ", "")

    allowed = "0123456789+-*/()."

    if not all(c in allowed for c in text):
        return

    try:
        result = eval(text)

        response = f"↔️ {result}"

        entities = [
            MessageEntity(
                type=MessageEntityType.CUSTOM_EMOJI,
                offset=0,
                length=2,
                custom_emoji_id=PREMIUM_EMOJI_ID
            )
        ]

        await message.reply(
            text=response,
            entities=entities
        )

    except:
        pass


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())