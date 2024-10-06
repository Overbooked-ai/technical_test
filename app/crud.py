# app/crud.py

# CRUD operations for interacting with the database.

# For MongoDB:

from bson.objectid import ObjectId


# Example functions:

async def get_user(db, user_id: str):
    # Retrieve a user document from the 'users' collection
    return await db["users"].find_one({"_id": user_id})


async def create_user(db, user_id: str):
    # Insert a new user document into the 'users' collection
    user = {"_id": user_id}
    await db["users"].insert_one(user)
    return user


async def save_recommendations(db, user_id: str, recommendations: list):
    # Save or update recommendations for a user in the 'recommendations' collection
    await db["recommendations"].update_one(
        {"user_id": user_id},
        {"$set": {"recommendations": recommendations}},
        upsert=True
    )


async def get_recommendations(db, user_id: str):
    # Retrieve recommendations for a user from the 'recommendations' collection
    return await db["recommendations"].find_one({"user_id": user_id})


# Hints:
# - Use `find_one`, `insert_one`, `update_one` methods from Motor's API.
# - Remember to handle cases where documents might not exist.

# For SQLAlchemy (optional):

"""
from sqlalchemy.orm import Session
from app import models

def get_user(db: Session, user_id: str):
    # Retrieve a user from the database
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user_id: str):
    # Create a new user in the database
    db_user = models.User(id=user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def save_recommendations(db: Session, user_id: str, recommendations: list):
    # Save recommendations for a user
    user = get_user(db, user_id)
    if not user:
        user = create_user(db, user_id)
    db_recommendations = models.Recommendation(user_id=user_id, recommendations=recommendations)
    db.add(db_recommendations)
    db.commit()

def get_recommendations(db: Session, user_id: str):
    # Retrieve recommendations for a user
    return db.query(models.Recommendation).filter(models.Recommendation.user_id == user_id).first()

# Hints:
# - Use SQLAlchemy session methods like `add`, `commit`, `query`.
# - Handle relationships between models if necessary.
"""
