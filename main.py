from fastapi import FastAPI
from fastapi import Depends
from application.routers import routers as ia_router

app = FastAPI()

app.include_router(ia_router.router)