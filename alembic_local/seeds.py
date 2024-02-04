from flask import current_app as app
from backend.database.core import db

if app.env == "development":
    import alembic_local.dev_seeds
elif app.env == "production":
    import alembic_local.prod_seeds
