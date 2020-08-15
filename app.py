import os
import sys
from sanic.response import json
from sanic.log import logger
from exert import Application
from exert.model import init_db
from exert.model.tester import Tester

# 创建应用。
app = Application('exert')

# 初始化


@app.listener('before_server_start')
async def initialize(app, loop):
    await init_db()


@app.route('/')
async def index(request):
    r = [i.id for i in await Tester.all()]
    logger.info('log output')
    return json({'hello': r})


@app.websocket('/api')
async def work(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
        access_log=True
    )
