from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .routers.index import router as index_router
from .routers.mailer import router as mail_router
from .routers.upload import router as upload_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(index_router, tags=["index"])
app.include_router(mail_router)
app.include_router(upload_router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
