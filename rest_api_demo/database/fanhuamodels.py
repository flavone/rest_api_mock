from rest_api_demo.database import db


class InsuranceInfo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)