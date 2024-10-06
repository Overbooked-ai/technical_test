# app/dependencies.py

# TODO: Define dependencies for database connections.

# For MongoDB:

# Hints:
# - Create a dependency that yields the database instance.
# - Use this dependency in your routes to access the database.

# Example:

"""
from app.database import get_database

async def get_db():
    db = get_database()
    yield db
    # No need to close the connection; Motor handles connection pooling
"""

# For SQL (optional):

# Hints:
# - Create a dependency that provides a database session.
# - Ensure proper session management (commit, rollback, close).

# Example:

"""
from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
