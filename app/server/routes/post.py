from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_post,
    retrieve_posts,
    retrieve_post,
    update_post,
    delete_post,
    add_comment,
    retrieve_comment,
)

from server.models.blog import (
    ErrorResponseModel,
    ResponseModel,
    PostSchema,
    UpdatePostModel,
    CommentSchema,
)

router = APIRouter()

@router.post("/", response_description="Post data added into the database")
async def add_post_data(post: PostSchema = Body(...)):
    post = jsonable_encoder(post)
    new_post = await add_post(post)
    return ResponseModel(new_post, "post added successfully.")

@router.get("/", response_description="Posts retrieved")
async def get_posts():
    posts = await retrieve_posts()
    if posts:
        return ResponseModel(posts, "post data retrieved successfully")
    return ResponseModel(posts, "Empty list returned")

@router.get("/{id}", response_description="user post retrieved")
async def get_post_data(id):
    post = await retrieve_post(id)
    if post:
        return ResponseModel(post, "post data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")

@router.put("/{id}")
async def update_user_data(id: str, req: UpdatePostModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_post = await update_post(id, req)
    if updated_post:
        return ResponseModel(
            "post with ID: {} name update is successful".format(id),
            "post name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the User data.",
    )


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_post_data(id: str):
    deleted_post = await delete_post(id)
    if deleted_post:
        return ResponseModel(
            "post with ID: {} removed".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "post with id {0} doesn't exist".format(id)
    )


@router.post("/{id}/comments", response_description="comment data added into the database")
async def add_comment_data(id: str, comment: CommentSchema = Body(...)):

    comment = jsonable_encoder(comment)
    add_postid_comment = {"post_id": id}
    comment.update(add_postid_comment) 
    new_comment = await add_comment(comment)
    return ResponseModel(new_comment, "comment added successfully.")


@router.get("/{id}/comments", response_description="Comments retrieved")
async def get_comments(id):
    posts = await retrieve_comment(id)
    if posts:
        return ResponseModel(posts, "post data retrieved successfully")
    return ResponseModel(posts, "Empty list returned")