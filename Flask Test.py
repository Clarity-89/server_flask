from flask import Flask, render_template

app = Flask(__name__)

# Import CRUD operations and database classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


@app.route('/')
@app.route('/hello')
def hello_world():
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)

    return render_template('menu.html', restaurant=restaurant, items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
