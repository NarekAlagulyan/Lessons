from typing import Union

from fastapi import FastAPI


from user import views as user_views

app = FastAPI()



app.include_router(user_views.router)
