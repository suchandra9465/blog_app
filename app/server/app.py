from fastapi import FastAPI

from server.routes.user import router as UserRouter
from server.routes.post import router as PostRouter

app = FastAPI()

#Adding prefix tags in the route url for section wise separation
app.include_router(UserRouter, tags=["user"], prefix="/user")
app.include_router(PostRouter, tags=["post"], prefix="/post")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this Blog app!"}


