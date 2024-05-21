from requests import get
Weight = input('Введите Weight = ')
Power = input('Введите Power = ')
Seats = input('Введите Seats = ')
Fuel = input('Введите Fuel = ')
KPP = input('Введите KPP = ')
print(get(f'http://127.0.0.1:5000/api?Weight={Weight}&Power={Power}&Seats={Seats}&Fuel={Fuel}&KPP={KPP}').json())