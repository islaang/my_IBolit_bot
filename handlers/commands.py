from aiogram import Router,F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message,CallbackQuery,FSInputFile
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from config import TOKEN

bot = Bot(TOKEN)
router = Router()   
@router.message(CommandStart())
async def start(message:Message):
    description = (
        "Привет, я доктор АйБолит! \n"
        "я даю вам советы смотря на вашу болезнь\n"
        "Но для начала скажите что именно у вас болит!\n"
        "Используй эти кнопки!"
    )
    kb = [
        [KeyboardButton(text='Номер скорой помощи'), KeyboardButton(text='Адрес больниц в Бишкеке')],
        [KeyboardButton(text='Болит голова'), KeyboardButton(text='Болит живот')],
        [KeyboardButton(text='Болит горло'), KeyboardButton(text='Болит зуб')]
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    await message.answer(description, reply_markup=keyboard)

@router.message(F.text == 'Болит голова')   
async def head(message:Message):
    await message.answer("Если у вас болит голова, есть несколько действий, которые можно предпринять, чтобы облегчить состояние: \n" 
"1. **Отдых и расслабление:** Попробуйте немного отдохнуть, улечься или просто закрыть глаза на несколько минут. \n"
"2. **Пить воду:** Нередко головная боль может быть вызвана обезвоживанием. Попробуйте выпить стакан воды. \n"
"3. **Избегать яркого света и шума:** Убедитесь, что вокруг вас нет яркого освещения или громкого шума, так как это может усилить боль.\n"
"4. **Массаж:** Нежные массажные движения в области висков и шеи могут помочь снять напряжение.\n"
"5. **Холод или тепло:** Некоторым людям помогает нанесение холодного компресса на лоб или затылок, а другим - тепло (например, горячий компресс или тёплая душевая).\n"
"6. **Лекарства:** При необходимости можно принять безрецептурные препараты против головной боли, такие как парацетамол или ибупрофен. Однако следует следовать инструкции по дозировке и проконсультироваться с врачом, если у вас есть какие-либо медицинские противопоказания.\n"
"7. **Избегать стресса:** Стресс часто является провоцирующим фактором для головной боли. Попробуйте найти способы справляться со стрессом, такие как глубокое дыхание, медитация или занятия йогой.\n"
"8. **Консультация с врачом:** Если головные боли становятся частыми или сильными, обратитесь за консультацией к врачу для диагностики и уточнения причин, особенно если они сопровождаются другими симптомами.\n"
"Запомните, что головная боль может иметь разные причины, от обычного напряжения и усталости до более серьёзных медицинских состояний, поэтому важно обращаться к врачу, если вы часто сталкиваетесь с этим симптомом или если боли очень сильные.\n")



@router.message(F.text=="Болит живот")
async def stomach(message: Message):
    await message.answer(
        "Если у вас болит живот, рекомендуется:\n"
        "- Обратить внимание на диету и избегать тяжёлых блюд.\n"
        "- Исключить возможные аллергены или несовместимые продукты.\n"
        "- Употреблять больше жидкости и фруктов.\n"
        "- Возможно, принять лёгкое обезболивающее или антигазовое средство.\n"
        "- Если боли становятся сильными или длительными, обратиться к врачу для диагностики и рекомендаций.\n"
    )

@router.message(F.text =="Болит горло")
async def throat(message: Message):
    await message.answer(
        "Если у вас болит горло, можно попробовать следующие методы:\n"
        "- Промывание горла солевым раствором или травяным отваром.\n"
        "- Пить тёплые напитки, такие как чай с мёдом и лимоном.\n"
        "- Избегать холодных напитков и острой, кислой пищи.\n"
        "- Принять обезболивающее для горла или антисептик в виде спрея.\n"
        "- Покрыть горло тёплым шарфом и избегать холодного воздуха.\n"
        "- Если симптомы ухудшаются или сопровождаются лихорадкой, обратиться к врачу.\n"
    )

@router.message(F.text =="Болит зуб")
async def tooth(message: Message):
    await message.answer(
        "Если у вас болит зуб, можно попробовать следующие рекомендации:\n"
        "- Осторожно промыть рот тёплой солевым раствором.\n"
        "- Принять обезболивающее, например, парацетамол или ибупрофен.\n"
        "- Избегать очень горячей или очень холодной пищи.\n"
        "- В случае наблюдения воспаления десен или наличия дентального пломбы, обратиться к стоматологу.\n"
    )


# @router.message(F.text == 'Советы')
# async def advice(message:Message):
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Болит голова', callback_data='headache')],
#         [InlineKeyboardButton(text='Болит живот', callback_data='stomachache')],
#         [InlineKeyboardButton(text='Болит горло', callback_data='sorethroat')],
#         [InlineKeyboardButton(text='Болит зуб', callback_data='toothache')]
#     ])
#     await message.answer(text='Выберите тему:', reply_markup=keyboard)

@router.message(F.text == 'Номер скорой помощи')
async def number(message:Message):
    await message.answer('Номер скорой помощи в России: 103, в США: 911')

@router.message(F.text == 'Адрес больниц в Бишкеке')
async def address(message:Message):
    await message.answer('Научно-исследовательский центр охраны здоровья народа:\n'
'Адрес: ул. Тыныстанова, 16\n'
'Городская клиническая больница № 1:\n'
'Адрес: ул. Ибраимова, 87\n'
'Городская клиническая больница № 4:\n'
'Адрес: ул. Логвиненко, 3\n'
'Городская клиническая больница № 6:\n'
'Адрес: ул. Каракольская, 6\n'
'Городская клиническая больница № 8:\n'
'Адрес: ул. Раззакова, 2\n'
)

async def periodic_messages():  
    while True:
        await asyncio.sleep(2)
        await bot.send_message(chat_id=1375504505, text="Не забудьте почистить зубы!")