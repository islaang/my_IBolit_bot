# from aiogram import Bot, Dispatcher
# from config import TOKEN
# import asyncio
# from handlers.commands import router
# from handlers.commands import periodic_messages
# import logging
# import sys


# async def main():
#     bot = Bot(token=TOKEN) 
#     dp = Dispatcher()
#     dp.include_router(router=router)
#     await dp.start_polling(bot) #Держит бота в активном состоянии
#     await periodic_messages()
#     # await models_main()

    
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)

#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(main())

#     try:
#         asyncio.run(main())
#     except Exception as e:
#         print("Ошибка",e)

from aiogram import Bot, Dispatcher
from config import TOKEN
import asyncio
from handlers.commands import router
import logging
import sys

bot = Bot(token=TOKEN)

async def periodic_messages():
    while True:
        await asyncio.sleep(2)
        await bot.send_message(chat_id=1375504505, text="Не забудьте почистить зубы!")

async def main():
    dp = Dispatcher()
    dp.include_router(router=router)
    
    # Запуск функции periodic_messages в фоновом режиме
    asyncio.create_task(periodic_messages())
    
    await dp.start_polling(bot) # Держит бота в активном состоянии

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    try:
        asyncio.run(main())
    except Exception as e:
        print("Ошибка", e)
