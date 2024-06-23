from aiogram import Bot, Dispatcher
from config import TOKEN
import asyncio
from handlers.commands import router

import logging
import sys



async def main():
    bot = Bot(token=TOKEN) 
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot) #Держит бота в активном состоянии
    # await models_main()

    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

    try:
        asyncio.run(main())
    except Exception as e:
        print("Ошибка",e)
