import pickle

import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

type_dict = {
    0: "Внедорожник",
    1: "Седан",
    2: "Минивен",
    3: "Универсал",
    4: "Компакт",
    5: "Кроссовер"
}

menu = [{"name": "Лаба 1", "url": "p_knn"},
        {"name": "Лаба 2", "url": "p_lab2"},
        {"name": "Лаба 3", "url": "p_lab3"}]

loaded_model_knn = pickle.load(open('model/AutoKNN', 'rb'))
loaded_model_Log = pickle.load(open('model2/AutoLogist', 'rb'))




@app.route("/")
def index():
    return render_template('index.html', title="Лабораторные работы, выполненные Королём Богданом Александровичем", menu=menu)


@app.route("/p_knn", methods=['POST', 'GET'])
def f_lab1():
    if request.method == 'GET':
        return render_template('lab1.html', title="Метод k -ближайших соседей (KNN)", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[int(request.form['Weight']),
                           int(request.form['Power']),
                           int(request.form['Seats']),
                           int(request.form['Fuel']),
                           int(request.form['KPP'])]])
        pred = loaded_model_knn.predict(X_new)
        type = type_dict[pred[0]]
        return render_template('lab1.html', title="Метод k -ближайших соседей (KNN)", menu=menu,
                               class_model="Это: " + type)

@app.route("/p_lab2", methods=['POST', 'GET'])
def f_lab2():
    if request.method == 'GET':
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu)
    if request.method == 'POST':
        X_new = np.array([[int(request.form['Weight']),
                           int(request.form['Power']),
                           int(request.form['Seats']),
                           int(request.form['Fuel']),
                           int(request.form['KPP'])]])
        pred = loaded_model_Log.predict(X_new)
        type = type_dict[pred[0]]
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu,
                               class_model="Это: " + type)


@app.route("/p_lab3")
def f_lab3():
    if request.method == 'GET':
        return render_template('lab3.html', title="Дерево решений", menu=menu)
    if request.method == 'POST':
        X_new = np.array([[int(request.form['Weight']),
                           int(request.form['Power']),
                           int(request.form['Seats']),
                           int(request.form['Fuel']),
                           int(request.form['KPP'])]])
        pred = loaded_model_Log.predict(X_new)
        type = type_dict[pred[0]]
        return render_template('lab3.html', title="Дерево решений", menu=menu,
                               class_model="Это: " + type)

@app.route('/api', methods=['get'])
def get_sort():
    X_new = np.array([[int(request.args.get('Weight')),
                       int(request.args.get('Power')),
                       int(request.args.get('Seats')),
                       int(request.args.get('Fuel')),
                       int(request.args.get('KPP'))]])
    pred = loaded_model_knn.predict(X_new)
    type = type_dict[pred[0]]

    return jsonify({'classification': type}, ensure_ascii=False)



if __name__ == "__main__":
    app.run(debug=True)
