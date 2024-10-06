# app/models.py

# TODO: Define database models.

# For MongoDB:
# - Since MongoDB is schemaless, you don't need to define models like in SQL.
# - However, you can create data classes or Pydantic models for type checking if desired.
# - Use the collection names directly in your code (e.g., 'users', 'recommendations').

# Example:
#
# users collection documents:
# {
#     "_id": "<user_id>",
#     // additional user fields if needed
# }
#
# recommendations collection documents:
# {
#     "_id": ObjectId,
#     "user_id": "<user_id>",
#     "recommendations": ["recommendation1", "recommendation2", ...]
# }

# For SQL (optional):
# - Define SQLAlchemy models for User and Recommendation tables.
# - Example:
#
# from sqlalchemy import Column, Integer, String, Text, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(String, primary_key=True, index=True)
#
# class Recommendation(Base):
#     __tablename__ = 'recommendations'
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(String, ForeignKey('users.id'))
#     recommendations = Column(Text)  # Store as JSON string or use a relationship
#
#     user = relationship('User', back_populates='recommendations')
#
# User.recommendations = relationship('Recommendation', order_by=Recommendation.id, back_populates='user')
