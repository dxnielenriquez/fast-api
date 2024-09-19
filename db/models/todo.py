from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todo(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)


