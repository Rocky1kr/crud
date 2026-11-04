from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
# directory => 앞으로 HTML 파일을 찾을 위치
templates = Jinja2Templates(directory='templates')


# 가상 데이터
posts = {
    1: {"id": 1, "title": "hi", "content": "반갑습니다."},
    2: {"id": 2, "title": "배고파요", "content": "뭐먹지"},
}

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
def pong(count: int):
    return {'result': count ** 3}

@app.post('/pong')
def pong_post(count: int = Form()):
    return {'result': count ** 2}