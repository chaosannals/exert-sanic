from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def index(request):
    return json({'hello': 'world'})

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
    