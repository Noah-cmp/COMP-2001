from flask import abort, make_response
from config import db
from models import Profile, profile_schema, profiles_schema

ALLOWED_ROLES = {"Admin", "User"}

def _validate(profile: dict, is_create: bool):
    required = ["email", "username", "password", "role"]
    if is_create:
        missing = [k for k in required if k not in profile]
        if missing:
            abort(400, f"Missing required fields: {', '.join(missing)}")

    if "role" in profile and profile["role"] not in ALLOWED_ROLES:
        abort(400, "role must be 'Admin' or 'User'")

    if "email" in profile:
        email = profile["email"]
        if len(email) > 30:
            abort(400, "email must be <= 30 characters")
        if "@" not in email or "." not in email:
            abort(400, "email must be a valid email format")

    if "username" in profile and len(profile["username"]) > 30:
        abort(400, "username must be <= 30 characters")

    if "password" in profile and len(profile["password"]) > 30:
        abort(400, "password must be <= 30 characters")


