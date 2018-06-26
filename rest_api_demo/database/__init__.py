from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from rest_api_demo.database.models import Post, Category  # noqa
    db.drop_all()
    db.create_all()


def recreate_fanhua_database():
    from rest_api_demo.database.fanhuamodels import InsuranceInfo
    db.drop_all()
    db.create_all()
