from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from routes.most_eaten_ranking import most_eaten_ranking
from peewee import fn
from models import Food

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():

    score_ranking = Food \
        .select(Food.restaurant,fn.COUNT(Food.evaluation)) \
        .group_by(Food.restaurant) \
        .order_by(fn.COUNT(Food.evaluation).desc()) \
        .limit(5)
    
    restaurant_ranking = Food.select(Food.restaurant,fn.Avg(Food.evaluation)).group_by(Food.restaurant).order_by(fn.Avg(Food.evaluation).desc()).limit(5)

    return render_template('index.html',restaurant_ranking=restaurant_ranking,score_ranking = score_ranking, foods = most_eaten_ranking())
if __name__ == '__main__':
    app.run(port=8080, debug=True)
