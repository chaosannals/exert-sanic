import os
import sys
from sanic import Sanic
from sanic.response import json
from tortoise import Tortoise
from exert.model.tester import Tester

app = Sanic()
here = os.path.dirname(os.path.realpath(sys.argv[0]))
app.static('/', os.path.join(here, 'public'))

@app.listener('before_server_start')
async def init_db(app, loop):
    await Tortoise.init(
        db_url='mysql://root:root@127.0.0.1:3306/exert',
        modules={ 'models': ['exert.model.tester'] }
    )

@app.route('/')
async def index(request):
    r = [ i.id for i in await Tester.all()]
    return json({'hello': r })

@app.websocket('/api')
async def work(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    