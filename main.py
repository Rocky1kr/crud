from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
# directory => 앞으로 HTML 파일을 찾을 위치
templates = Jinja2Templates(directory='templates')

@app.get('/')
def home():
    return {'hello': 'world'}

# 사용자에게 정보를 입력받는 페이지를 리턴

@app.get('/ping')
def ping(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='ping.html'
    )

# 받은 정보를 사용하는 페이지
@app.get('/pong')
def pong():
    pass