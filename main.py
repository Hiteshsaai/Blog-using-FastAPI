from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"hello": {"world": "I am learning FastAPI"}}


@app.get("/about")
def detail():
    return {
        "about": {
            "Name": "Hitesh Saai",
            "Age": "26",
            "Job Title": "ML Software Engineer",
        }
    }
