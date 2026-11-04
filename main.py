from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

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


# 전체 게시물 출력
@app.get('/posts')
def post_list(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='list.html',
        context={'posts': list(posts.values())}
    )


# 사용자가 데이터 입력할수 있는 페이지 제공
@app.get('/posts/new')
def post_new(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='new.html'
    )

#사용자가 넘겨준 데이터를 저장
@app.post('/posts/create')
def post_create(title: str = Form(), content: str = Form()):
    # return {'t': title, 'c': content}
    new_id = max(posts.keys()) + 1
    posts[3] = {'id': new_id, 'title': title, 'content': content}

    return RedirectResponse(f'/posts/{new_id}', status_code=303)



# 하나의 게시물 출력
@app.get('/posts/{post_id}')
def post_detail(request: Request, post_id: int):

    post = posts[post_id]

    return templates.TemplateResponse(
        request=request,
        name='detail.html',
        context={'post': post}
    )

@app.get('/posts/{post_id}/edit')
def post_edit(request: Request, post_id: int):
    # SELECT * FROM posts WHERE post_id = 1;
    post = posts[post_id]

    return templates.TemplateResponse(
        request=request,
        name='edit.html',
        context={'post': post}
    )

@app.post('/posts/{post_id}/update')
def post_update(post_id: int, title: str = Form(), content: str = Form()):
    # 기존 정보 찾기
    old_post = posts[post_id]

    # 새로운 정보로 수정하기
    old_post['title'] = title
    old_post['content'] = content

    new_post = old_post

    # 전체 데이터에 적용시키기
    posts[post_id] = new_post

    return RedirectResponse(f'/posts/{post_id}', status_code=303)


@app.get('/posts/{post_id}/delete')
def post_delete(post_id: int):
    posts.pop(post_id)

    return RedirectResponse('/posts', status_code=303)

