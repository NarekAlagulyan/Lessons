from sanic import Sanic, text
from sanic.response import json

app = Sanic("my-hello-world-app")

@app.get('/')
async def test(request):
    return json({'hello': 'world'})

@app.get("/foo")
async def typical_use_case(request):
    return text("I said foo!")