from datetime import datetime
from models.food import Food
from models.restaurant import Restaurant
from models.user import User


def seed():
    User.delete().execute()
    User.create(student_id="k23075", name="ただ", gender="male", age=19)
    User.create(student_id="k23060", name="しばた", gender="male", age=20)
    User.create(student_id="k23003", name="あきもと", gender="male", age=20)
    User.create(student_id="k23054", name="さかい", gender="male", age=19)
    User.create(student_id="k23083", name="ながお", gender="female", age=20)

    Restaurant.delete().execute()
    Restaurant.create(name="すき家", address="愛知県豊田市八草町八千草9999",  lat=35.1830033, long=137.1126659)
    Restaurant.create(name="吉野家", address="愛知県豊田市八草町八千草12366",  lat=35.1829482, long=137.112724)
    Restaurant.create(name="なか卯", address="愛知県豊田市八草町八千草1234",  lat=35.1846798, long=137.1150462)
    Restaurant.create(name="松屋", address="愛知県豊田市八草町八千草0000",  lat=35.1861263, long=137.1132236)
    Restaurant.create(name="牛丼屋", address="愛知県豊田市八草町八千草8292",  lat=35.1852017, long=137.1091925)

    Food.delete().execute()
    time = datetime.now()
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 1), restaurant=Restaurant.get(Restaurant.id == 5), food="寿司", evaluation=1)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 2), restaurant=Restaurant.get(Restaurant.id == 5), food="寿司", evaluation=1)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 3), restaurant=Restaurant.get(Restaurant.id == 5), food="寿司", evaluation=1)
    Food.create(time=time, user=User.get(User.id == 4), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 4), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 4), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 4), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 4), restaurant=Restaurant.get(Restaurant.id == 5), food="寿司", evaluation=1)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 1), food="カレー", evaluation=5)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 2), food="ラーメン", evaluation=4)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 3), food="うどん", evaluation=3)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 4), food="カツ丼", evaluation=2)
    Food.create(time=time, user=User.get(User.id == 5), restaurant=Restaurant.get(Restaurant.id == 5), food="寿司", evaluation=1)



if __name__ == "__main__":
    seed()