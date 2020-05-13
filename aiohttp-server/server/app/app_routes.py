from . import routes
from aiohttp import web
from .app_logic import _upload, _download, _size


@routes.post('/upload')
async def upload(request):
    if request.method == 'POST':
        response = await _upload(request)
        return response
    else:
        web.json_response({'response': 'wrong requests method'})



@routes.get('/hello')
async def upload(request):
    return web.Response(text='Greetings! This is a test aiohttp server aimed at processing files\n\n')


@routes.get('/download')
async def download(request):
    if request.method == 'GET':
        data = await _download(request)
        return data
    else:
        web.json_response({'response': 'wrong requests method'})


@routes.get('/size')
async def size(request):
    if request.method == 'GET':
        data = await _size(request)
        return data
    else:
        web.json_response({'response': 'wrong requests method'})
