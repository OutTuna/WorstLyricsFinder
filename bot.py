import logging
from aiogram.utils import executor
from load import dp
import handlers #used


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    executor.start_polling(dp)
