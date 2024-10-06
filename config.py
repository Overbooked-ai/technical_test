# config.py

import os

# MongoDB configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://db:27017")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "app_db")

# SQLAlchemy configuration (optional)
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/app_db")
