from fastapi.routing import APIRouter
from mock_db import users

# CRUD: Create Retrieve Update Delete

router = APIRouter(prefix="/users", tags=["user"])



@router.post('/')
def create_user(data: dict):
    user = {
        data['username']: data
    }
    users.update(user)

    return user


@router.get('/')
def get_user_list():
    return users


@router.get('/{username}')
def get_user_detail(username: str):
    user = users.get(username)
    if user is None:
        return {"error": "User not found"}

    return user


@router.get('/{username}/stakes')
def get_user_detail(username: str):
    if (user := users.get(username)) is None:
        return {"error": "User not found"}

    user_stakes = user['stakes']

    return user_stakes




