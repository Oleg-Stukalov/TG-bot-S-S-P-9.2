import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers

# Initialize logger
logger = logging.getLogger(__name__)


# Function for bot config and start
async def main() -> None:
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    # Output to console start bot info
    logger.info('Starting bot')

    # Load configuration in var config
    config: Config = load_config()

    # Initialize bot and dispatcher
    bot = Bot(token=config.tg_bot.token,
              #parse_mode='HTML'
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Register routers in dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Skip stored updates and start polling#
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())