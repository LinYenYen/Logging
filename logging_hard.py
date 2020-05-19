import logging
from datetime import datetime
import os
##################################################
# Create log directory
if not os.path.exists('./log/'):
    os.makedirs('./log/')

# 複雜詳細的寫法
def create_logger():
    # 基本參數設定
    FILENAME = './log/{}.txt'.format(datetime.now().strftime('%Y-%m-%d %H.%M.%S'))
    FORMATE = '%(asctime)s %(levelname)s %(message)s'
    # 建立logger、formatter
    # level等級：DEBUG(10) < INFO(20) < WARNING(30)	< ERROR(40) < CRITICAL(50)
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter(FORMATE)
    logger.setLevel(logging.ERROR)
    # 建立file handler 用FileHandler將log輸出成檔案
    fileHandler = logging.FileHandler(FILENAME, 'w')
    fileHandler.setFormatter(formatter)                         # 沒額外設定該Handler的level級數，就為logger.setLevel(logging.XXX)的初始設定
    logger.addHandler(fileHandler)
    # 建立console handler 用StreamHandler將log輸出到console
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    consoleHandler.setLevel(logging.INFO)                       # 可額外設定每個Handler的level級數，若不設定就為logger.setLevel(logging.XXX)的初始設定
    logger.addHandler(consoleHandler)
    # 輸出log資訊，參數exc_info=True 可將except訊息傳出
    logger.error('Catch Error: ', exc_info=True)                # 也可寫成logger.exception('Catch Error: ')

if __name__ == '__main__':
    try:
        1 / 0
    except:
        create_logger()
        exit()
