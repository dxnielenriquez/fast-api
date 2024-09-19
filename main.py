from fastapi import FastAPI
from router import router
from db.base import Base   # now import Base from db.base not db.base_class
from db.session import engine

app = FastAPI()
app.include_router(router.router)

def create_tables():
	Base.metadata.create_all(bind=engine)
