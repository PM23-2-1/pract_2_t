# librarys
import warnings
import math

import universal
import db
import exel

# ignoring log level warning
warnings.filterwarnings("ignore")

def create_set():
    seti = tuple(input('tuple: ').split())
    db.save_result('tuple', seti)

def get_i_set():
    seti = db.get_last_set()
    if seti is not None:
        seti = tuple(str(i) for i in db.get_last_set()[1:-1].replace("'", '').split(', '))
        diction = {k:v for k, v in zip(range(len(seti)), seti)}
        db.save_result('dict', diction)

def get_srez():
    seti = db.get_last_set()
    if seti is not None:
        seti = tuple(str(i) for i in db.get_last_set()[1:-1].replace("'", '').split(', '))
        a, b = list(map(int, input('a, b: ').split()))
        db.save_result('srez', seti[max(0, a):min(len(seti), b)])

def get_set():
    seti = tuple(str(i) for i in db.get_last_set()[1:-1].replace("'", '').split(', '))
    print(seti)

# main console menu
def main():
    db.check_db()
    run = True
    commands = """==========================================================================
1. Создание кортежа, сохранение и вывод из MySQL.
2. Извлечь элементы по индексам, сохранение и вывод из MySQL.
3. Взятие среза по индексам, сохранение и вывод из MySQL.
4. Вывод всех элементов кортежа из MySQL.
5. Сохранить данные из MySQL в Excel и вывести на экран.
6. Завершить"""
    while run:
        run = universal.uni(commands, 
                      create_set, get_i_set, get_srez,
                      get_set, db.save_db_to_xlxs)
    return

if __name__ == '__main__':
    main()