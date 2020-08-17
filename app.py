from sanic.response import json, html
from sanic.log import logger
from jinja2 import Environment, PackageLoader, select_autoescape
from exert import Application
from exert.model import init_db
from exert.model.tester import Tester

# 创建应用。
app = Application('exert')


@app.listener('before_server_start')
async def initialize(app, loop):
    '''
    初始化。
    '''

    await init_db()


@app.route('/jinja2.html')
async def jinja2(request):
    env = Environment(
        loader=PackageLoader('view', '.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('index.html')
    return html(template.render(users=[{
        'url': 'url1',
        'username': 'user1'
    }, {
        'url': 'url2',
        'username': 'user2'
    }]))


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
