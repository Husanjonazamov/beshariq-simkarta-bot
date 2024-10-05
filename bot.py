import asyncio
import logging
import sys

from loader import main

import handler


"""
Asosiy botni ishga tushiradigan fayl
"""


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())