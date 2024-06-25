import os

URL = os.environ.get('URL', 'https://happytohelp-mesolitica-com-2927-rasa.nous.mesolitica.com/webhooks/rest_v2/webhook')
NAME = os.environ.get('NAME', 'Bot')

from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(docs_url=None, redoc_url=None)


StaticFiles.is_not_modified = lambda *args, **kwargs: False
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse(
        'index.html', {
            'request': request,
            'url': URL,
            'name': NAME,
        }
    )