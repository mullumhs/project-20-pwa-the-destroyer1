from flask import Flask
from views import init_routes
from flask import render_template, request, redirect, url_for, flash
from models import db, item

# Create the Flask app and configure it
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise the database and routes
db.init_app(app)
init_routes(app)


@app.route('/add', methods=['GET', 'POST'])

def add_movie():

    if request.method == 'POST':

        new_item = item(

            title=request.form['title'],

            description=request.form['description'],

            date_listed=int(request.form['date_listed']),

            price=float(request.form['price']),

            size=request.form['size'],
        )

        db.session.add(new_item)

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html')



@app.route('/', methods=['GET'])

def get_items():

    # This route should retrieve all items from the database.

    # Query the database to get all items and return them, formatted as a list of dictionaries.

    return render_template('index.html', message='Displaying all items')


@app.route('/update', methods=['POST'])

def update_item():

    # This route should handle updating an existing item identified by the given ID.

    return render_template('index.html', message=f'Item updated successfully')

@app.route('/delete', methods=['POST'])

def delete_item():

    # This route should handle deleting an existing item identified by the given ID.

    return render_template('index.html', message=f'Item deleted successfully')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)