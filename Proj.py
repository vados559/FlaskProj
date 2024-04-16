from flask import Flask
from flask import request, render_template

app = Flask(__name__, static_folder ="E:\\FlaskProj\\static")

UID = {'1': {
            'name': 'Евгений',
            'city': 'Красноярск',
            'age': 14
},
       '2': {
            'name': 'Иван',
            'city': 'Находка',
            'age': 16
},
       '3': {
            'name': 'Софья',
            'city': 'Калининград',
            'age': 15
}
}
@app.route('/')
def index():
    name = "LOL"
    return render_template('index.html')

@app.route('/table')
def table():
    return render_template('Table.html', users=UID)

@app.route('/user/<id>')
def user(id):
    if id in UID:
        return f"Здравствуйте, Ваше имя:{UID[id]['name']}, Ваш город:{UID[id]['city']}, Ваш возраст:{UID[id]['age']}"
    else:
        return 'Такого пользователя не существует'
  
@app.route('/users')
def users():
    a = ''
    for i in range(1,4):
        a += f"Имя: {UID[str(i)]['name']}, Город: {UID[str(i)]['city']}, Возраст: {UID[str(i)]['age']}\n" 
    return a 

@app.route('/get_example') # добавляет пользователя в словарь, форма заполнения: ?name=""&city=""&age=""
def get_example():
    name = request.args.get('name')
    city = request.args.get('city')
    age = request.args.get('age')
    UID[str(int(max(UID))+1)]= {
        'name': name,
        'city': city,
        'age': age
    }
    return f"name = {name}; city = {city}; age = {age}"

if __name__ == '__main__':
    app.run(debug=True)



