from re import L
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False, unique=True)
  price = db.Column(db.Integer, nullable=False)
  barcode = db.Column(db.String(12), nullable=False, unique=True)
  description = db.Column(db.String(1024), nullable=False, unique=True)

  def __repr__(self):
    return f'Item {self.name}'


with app.app_context():
  db.create_all()


@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')


@app.route('/market')
def market_page():
  items = Item.query.all()
  return render_template('market.html', items=items)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
