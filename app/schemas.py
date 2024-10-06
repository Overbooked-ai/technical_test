# app/schemas.py

# TODO: Define Pydantic models for request and response bodies.
# Hints:
# - Create a `UserPreferences` model with fields:
#     - `user_id`: str
#     - `preferences`: List[str]
# - Create a `RecommendationResponse` model with fields:
#     - `user_id`: str
#     - `recommendations`: List[str]
# - Use Pydantic validators to ensure:
#     - `user_id` is a non-empty string.
#     - `preferences` is a non-empty list of non-empty strings.
# - Example:
#
# from pydantic import BaseModel, validator
# from typing import List
#
# class UserPreferences(BaseModel):
#     user_id: str
#     preferences: List[str]
#
#     @validator('user_id')
#     def user_id_must_not_be_empty(cls, v):
#         if not v.strip():
#             raise ValueError('user_id must be a non-empty string')
#         return v
#
#     @validator('preferences')
#     def preferences_must_not_be_empty(cls, v):
#         if not v:
#             raise ValueError('preferences must be a non-empty list')
#         if not all(isinstance(pref, str) and pref.strip() for pref in v):
#             raise ValueError('All preferences must be non-empty strings')
#         return v
#
# class RecommendationResponse(BaseModel):
#     user_id: str
#     recommendations: List[str]
