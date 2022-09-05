from loguru import logger

logger.add("./db/logs/debug.log",format="{time} {level} {message}",
           level="DEBUG", rotation="10 MB", compression="zip")
@logger.catch()
def shit(a,b):
    return a/b

if __name__ == '__main__':
    shit(1,0)
