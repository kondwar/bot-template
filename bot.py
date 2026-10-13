import asyncio
import glob
import importlib
import logging
import os

from aiogram import Bot, Dispatcher

from config import settings


def load_features(dp: Dispatcher) -> None:
    """Auto-load every feature_*.py file that exposes a `router`."""
    folder = os.path.dirname(os.path.abspath(__file__))
    for path in sorted(glob.glob(os.path.join(folder, "feature_*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        module = importlib.import_module(name)
        router = getattr(module, "router", None)
        if router is not None:
            dp.include_router(router)
            logging.info("Loaded feature: %s", name)


async def main() -> None:
    logging.basicConfig(level=settings.LOG_LEVEL)
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    load_features(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
