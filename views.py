from flask import render_template, request, redirect, url_for, flash
from models import db # Also import your database model here
from models import db, Item

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):


    @app.route('/')

    def index():

        item = Item.query.all()

        return render_template('index.html', item=item)
    


    @app.route('/add', methods=['GET', 'POST'])

    def add_movie():

        if request.method == 'POST':

            new_item = Item(

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





    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')