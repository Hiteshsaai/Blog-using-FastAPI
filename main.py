from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# import uvicorn

app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):

    if published:
        return {"data": f"Displaying {limit} articals which are published"}

    else:
        return {"data": "25 articals are not published"}


@app.get("/blog/unpublished")
def blog_unpublished():

    ## Listing all the unpublished blogs
    return {"data": "list of unpublished blogs"}


@app.get("/blog/{id}")
def blog_detail(id: int):

    ## fetch blog based on id:id
    return {"blog_id": id}


@app.get("/blog/{id}/comments")
def blog_comments(id: int, limit: int = 10):

    ## fetch comments of the blog with id:id
    return {"blog": {id: [1, 2, 3, 4, 5], "limit": limit}}


class CreateBlog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None


@app.post("/blog")
def create_blog(request: CreateBlog):
    return {"data": f"blog has been created with title `{request.title}` "}
