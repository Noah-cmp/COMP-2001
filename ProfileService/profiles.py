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


def read_all():
    profiles = Profile.query.all()
    return profiles_schema.dump(profiles), 200


def read_one(email: str):
    profile = Profile.query.get(email)
    if profile is None:
        abort(404, f"Profile with email {email} not found")
    return profile_schema.dump(profile), 200


def create(profile: dict):
    _validate(profile, is_create=True)

    existing = Profile.query.get(profile["email"])
    if existing is not None:
        abort(409, "Profile with this email already exists")

    if "role" not in profile:
        profile["role"] = "User"

    new_profile = profile_schema.load(profile, session=db.session)
    db.session.add(new_profile)
    db.session.commit()
    return profile_schema.dump(new_profile), 201


def update(email: str, profile: dict):
    _validate(profile, is_create=False)

    existing = Profile.query.get(email)
    if existing is None:
        abort(404, f"Profile with email {email} not found")

    for field in ["username", "aboutme", "location", "dob", "language", "password", "role"]:
        if field in profile:
            setattr(existing, field, profile[field])

    db.session.merge(existing)
    db.session.commit()
    return profile_schema.dump(existing), 200


def delete(email: str):
    existing = Profile.query.get(email)
    if existing is None:
        abort(404, f"Profile with email {email} not found")

    db.session.delete(existing)
    db.session.commit()
    return make_response(f"{email} deleted", 200)






