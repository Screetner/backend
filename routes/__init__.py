from .auth import router as auth_router
from .root import router as root_router

__all__ = [
    "root_router",
    "auth_router"
]
