import logging
import os
from datetime import datetime
##################################################
# Create log directory
if not os.path.exists('./log/'):
    os.makedirs('./log/')

# 簡單的寫法
def create_logger():
    # 基本參數設定
    FILENAME = './log/{}.txt'.format(datetime.now().strftime('%Y-%m-%d %H.%M.%S'))
    FORMAT = '%(asctime)s %(levelname)s %(message)s'
    # 若參數不給 filemode、filename，則錯誤訊息會顯示在console中
    logging.basicConfig(level=logging.ERROR,
                        filemode='w',
                        filename=FILENAME,
                        format=FORMAT)
    # 輸出log資訊，參數exc_info=True 可將except訊息傳出
    logging.error('Catch Error: ', exc_info=True)                # 也可寫成logger.exception('Catch Error: ')

if __name__ == '__main__':
    try:
        ans = 1 / 0
    except:
        create_logger()
        exit()
