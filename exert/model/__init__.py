from tortoise import Tortoise


async def init_db():
    '''
    初始化数据库。
    '''
    await Tortoise.init(
        db_url='mysql://root:root@127.0.0.1:3306/exert',
        modules={
            'models': [
                'exert.model.tester'
            ],
        }
    )
