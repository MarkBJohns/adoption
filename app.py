from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, default_profile, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.debug = True

toolbar = DebugToolbarExtension(app)

connect_db(app)
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

initialized = False

@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'Pet': Pet}

@app.route('/')
def welcome_page():
    pets = Pet.query.all()
    for pet in pets:
        print(pet.name)
    return render_template('home.html', pets=pets)

@app.route('/add')
def show_pet_form():
    form = AddPetForm()
    return render_template('add_pet.html', form=form)
    
@app.route('/add', methods=['POST'])
def add_pet():
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        photo_url = form.photo_url.data or default_profile
        print(f'''
            name={name}, 
            species={species},
            age={age},
            notes={notes},
            photo_url={photo_url}
        ''')
        
        pet = Pet(name=name, species=species, age=age, notes=notes, photo_url=photo_url)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)
    
@app.route('/pet/<int:pet_id>')
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet.html', pet=pet)

@app.route('/pet/<int:pet_id>/edit')
def show_edit_form(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    return render_template('edit_pet.html', form=form)

@app.route('/pet/<int:pet_id>/edit', methods=['POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data or default_profile
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        render_template('edit_pet.html', form=form)
        
