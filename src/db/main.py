from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker


async_engine = create_async_engine(
    url=Config.DATABASE_URL,
    # echo=True
)


async def init_db() -> None:
    async with async_engine.begin() as conn:
        from src.db.models import Book 
        await conn.run_sync(SQLModel.metadata.create_all)
        print("✅ Database initialized successfully!")  


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session