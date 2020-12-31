#! python3

import sys
from jd_spider_requests import JdSeckill

if __name__ == '__main__':
    a = """

       oooo oooooooooo.            .oooooo..o                     oooo         o8o  oooo  oooo  
       `888 `888'   `Y8b          d8P'    `Y8                     `888         `"'  `888  `888  
        888  888      888         Y88bo.       .ooooo.   .ooooo.   888  oooo  oooo   888   888  
        888  888      888          `"Y8888o.  d88' `88b d88' `"Y8  888 .8P'   `888   888   888  
        888  888      888 8888888      `"Y88b 888ooo888 888        888888.     888   888   888  
        888  888     d88'         oo     .d8P 888    .o 888   .o8  888 `88b.   888   888   888  
    .o. 88P o888bood8P'           8""88888P'  `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o o888o 
    `Y888P                                                                                                                                                  
                                               
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
    """
    jd_seckill = JdSeckill()

    choice_dict = {
        "1": jd_seckill.reserve,
        "2": jd_seckill.seckill_by_proc_pool
    }

    choice = ''

    if len(sys.argv) == 2:
        choice = sys.argv[1]
    else:
        print(a)
        choice = input('请选择:')

    if choice in choice_dict:
        choice_dict[choice]()
    else:
        print('没有此功能')
        sys.exit(1)
