from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class createBlog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None


@app.post("/blog")
def createBlog(request: createBlog):

    return {"title": request.title, "body": request.body, "publised": request.published}
