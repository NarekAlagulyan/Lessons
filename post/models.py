from user.models import User


class Post:
    id: int
    title: str
    content: str
    image: str

    author_id: User.id


class Comment:
    id: int
    content: str

    author_id: User.id
    post_id: Post.id


class Parent:
    id: int


class Child:
    id: int
    parent_id: int  = Parent.id
