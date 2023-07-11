from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "Hello",
        "content": "World",
    },
    {
        "id": 2,
        "title": "First Post",
        "content": "This is my first post!",
    },
    {
        "id": 3,
        "title": "Exciting News",
        "content": "I have something exciting to share with you all!",
    },
    {
        "id": 4,
        "title": "Travel Adventures",
        "content": "Exploring new places and creating amazing memories.",
    },
    {
        "id": 5,
        "title": "Favorite Recipe",
        "content": "Sharing my all-time favorite recipe with you!",
    },
    {
        "id": 6,
        "title": "Book Review",
        "content": "Just finished reading an incredible book. Here's my review!",
    },
    {
        "id": 7,
        "title": "Fitness Journey",
        "content": "Documenting my fitness progress and goals.",
    },
    {
        "id": 8,
        "title": "Thoughts on Technology",
        "content": "Discussing the latest tech trends and innovations.",
    },
    {
        "id": 9,
        "title": "Gardening Tips",
        "content": "Sharing my tips for maintaining a beautiful garden.",
    },
    {
        "id": 10,
        "title": "Movie Recommendations",
        "content": "Listing my top movie recommendations of all time.",
    },
    {
        "id": 11,
        "title": "Career Advice",
        "content": "Sharing valuable career advice based on my experience.",
    },
    {
        "id": 12,
        "title": "Pet Stories",
        "content": "Heartwarming and funny stories about my pets.",
    },
    {
        "id": 13,
        "title": "Product Review",
        "content": "Reviewing a popular product and sharing my thoughts.",
    },
    {
        "id": 14,
        "title": "Photography Tips",
        "content": "Providing tips and tricks for capturing stunning photos.",
    },
    {
        "id": 15,
        "title": "Hiking Adventure",
        "content": "Recounting my thrilling hiking adventure in the mountains.",
    }
]
# posts = []

# Post Model


class Post(BaseModel):
    id: int
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts", status_code=status.HTTP_200_OK)
async def get_posts(response: Response):
    if not posts:
        response.status_code = status.HTTP_204_NO_CONTENT
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    posts.append(post.model_dump())
    return posts[-1]


@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
async def get_post(id: int, response: Response):
    for post in posts:
        if post["id"] == id:
            return post
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Post not found"}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, response: Response):
    for post in posts:
        if post["id"] == id:
            posts.remove(post)
            response.status_code = status.HTTP_204_NO_CONTENT
            return
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Post not found"}
