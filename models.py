from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
default_profile = 'https://imgs.search.brave.com/1J7aUenaIiMb_Hj-nR3IrQbDhLOwxKZTX1NZI1ireWw/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA1LzQwLzQ0LzE5/LzM2MF9GXzU0MDQ0/MTk0M192RmJxTTZE/ZnBYWlVNUTkwUnhR/c2VFbEZmdG80MFpT/MS5qcGc'
    
class Pet(db.Model):
    '''pets table'''
    
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True)
    photo_url = db.Column(db.Text, nullable=True, default=default_profile)