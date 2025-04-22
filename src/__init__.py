from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from src.errors import register_error_handlers
from src.middleware import register_middleware

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Server is started....")
    await init_db()
    yield
    print(f"Server has been stopped....")

# version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Handles all CRUD operations and search functionalities for managing book records.
- Manages user registration, login, JWT authentication, and role-based access control.
- Sets up the database engine, models, and session handling using SQLModel.
- Allows users to post, retrieve, and manage reviews associated with books.
- Supports tagging of books for categorization and efficient filtering.
    """
version_prefix ="/api/v1"

app = FastAPI(
    title="Bookly",
    description=description,
    version="1.0",
    contact={
        "name": "Shashank singh",
        # "url": "",
        "email": "shashank190220@gmail.com",
    },
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)


register_error_handlers(app)
register_middleware(app)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"{version_prefix}/tags", tags=["tags"]) 