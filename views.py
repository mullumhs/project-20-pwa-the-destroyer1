from flask import render_template, request, redirect, url_for, flash
from models import db, Item

def init_routes(app):

    @app.route('/')
    def index():
        items = Item.query.all()
        return render_template('index.html', items=items)

    @app.route('/add', methods=['GET', 'POST'])
    def add_movie():
        if request.method == 'POST':
            new_item = Item(
                title=request.form['title'],
                item_type=request.form['item_type'],
                description=request.form['description'],
                price=float(request.form['price']),
                size=request.form['size'],
                colour=request.form['colour'],
                images=request.form['image']
            )
            db.session.add(new_item)
            db.session.commit()
            flash('Item added successfully!', 'success')
            return redirect(url_for('index'))

        return render_template('add.html')
    

    @app.route('/view', methods=['GET'])
    def view_items():
        "Display all items from the database."
        items = Item.query.all()
        return render_template('view.html', items=items)


    @app.route('/update>', methods=['GET', 'POST'])
    def update_item(item_id):
        item = Item.query.get_or_404(item_id)

        if request.method == 'POST':
            item.title = request.form['title']
            item.item_type = request.form['item_type']
            item.description = request.form['description']
            item.size = request.form['size']
            item.price = float(request.form['price'])
            item.colour = request.form['colour']
            item.images = request.form['image']

            db.session.commit()
            flash('Item updated successfully!', 'success')
            return redirect(url_for('index'))

        return render_template('update.html', item=item)

    @app.route('/delete/<int:item_id>', methods=['POST'])
    def delete_item(item_id):
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully!', 'success')
        return redirect(url_for('index'))
