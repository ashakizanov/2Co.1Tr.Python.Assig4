from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Aa8036673371@localhost/CoinMarket'
db = SQLAlchemy(app)


class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    content = db.Column(db.String(200000), nullable=True)

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):
        return '<Coin %r>' % self.id


@app.route('/coin', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        coin_name = request.form['name']
        url = 'https://coinmarketcap.com/ru/currencies/{0}'.format(coin_name)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        coin_content = str(soup.find_all('p'))
        new_task = Coin(name=coin_name, content=coin_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/coin')
        except:
            return 'error'
    else:
        coins = Coin.query.order_by(desc(Coin.id)).first()
        url = 'https://coinmarketcap.com/ru/currencies/{0}'.format(coins.name)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        return render_template('coin.html', soupp=soup.p, soupfindall=soup.find_all('p'), nname=coins.name)


if __name__ == "__main__":
    app.run(debug=True)

# url = 'https://coinmarketcap.com/ru/currencies/{0}'.format(task_name)
#         r = requests.get(url)
#         soup = BeautifulSoup(r.content, 'html.parser')
#         task_content = soup.p
