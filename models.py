from wtforms import  StringField
from . import db
class Investor(Form):
    email = StringField('Email')
    forename = StringField('Forename')
    surname = StringField('Surname')
    company = StringField('Company/Organization')
    phone = StringField('Phone Number')
    gender = StringField('Gender')
    category = StringField('Category Preference')
    budget = StringField('Investing Budget')
    startuplocation = StringField('Location of Startup')
    numberofpeople = StringField('Number of People in the Team')
    stage = StringField('Development Stage')
    returntype = StringField('Return Type')   

class Startup(db.Model):
    email = db.Column(db.String(100))
    full_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    category = db.Column(db.String(100))
    description = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    budget_need = db.Column(db.Integer)
    company_location = db.Column(db.String(100))
    return_type_startup = db.Column(db.String(100))
    additional_support = db.Column(db.String(100))