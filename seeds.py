from flask import Flask
from models import db, default_profile, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    
    p1 = Pet(
        name='Bear', species='dog',
        photo_url='https://imgs.search.brave.com/L1skehmdhyOX45fR7i8-5qH3LwEB2I6U1Mcsm0OPZ84/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNjM2/NDc1NDk2L3Bob3Rv/L3BvcnRyYWl0LW9m/LWJyb3duLXB1cHB5/LXdpdGgtYm9rZWgt/YmFja2dyb3VuZC5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/T3Q2M2RRT1lwbG0w/a0xKZGxTVldidEtH/d0drdVpmbmZkd0g1/cnk5YTZFUT0',
        age=5, notes="He is not very smart, but he's a very good boy.",
        available=True)
    p2 = Pet(
        name='Buddy', species='dog',
        photo_url=default_profile,
        available=False)
    
    db.session.add_all([p1, p2])
    db.session.commit()