import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb+srv://suchandra1998:Suchu%401998@cluster0.qyy5q28.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.blog

user_collection = database.get_collection("user_collection")
post_collection = database.get_collection("post_collection")
comment_collection = database.get_collection("comment_collection")




def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "password": user["password"],
    }

# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True



def post_helper(post)  -> dict:
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "body": post["body"],
    }


#add a  new post into the database 
async def add_post(post_data: dict) -> dict:
    post = await post_collection.insert_one(post_data)
    new_post = await post_collection.find_one({"_id": post.inserted_id})
    return post_helper(new_post)


# Retrieve all posts present in the database
async def retrieve_posts():
    posts = []
    async for post in post_collection.find():
        posts.append(post_helper(post))
    return posts

# Retrieve a post with a matching ID
async def retrieve_post(id: str) -> dict:
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        return post_helper(post)


# Update a post with a matching ID
async def update_post(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        updated_post = await post_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_post:
            return True
        return False


# Delete a post from the database
async def delete_post(id: str):
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        await post_collection.delete_one({"_id": ObjectId(id)})
        return True
    


def comment_helper(comment)  -> dict:
    return {
        "id": str(comment["_id"]),
        
        "fullname": comment["fullname"],
        "email": comment["email"],
        "body": comment["body"],
        "post_id": comment["post_id"],
    }

#add a  new post into the database 
async def add_comment(comment_data: dict) -> dict:
    comment = await comment_collection.insert_one(comment_data)
    new_comment = await comment_collection.find_one({"_id": comment.inserted_id})
    return comment_helper(new_comment)


async def retrieve_comment(id: str) -> dict:
    post = await comment_collection.find_one({"post_id": id})
    if post:
        return comment_helper(post)