from random import *
import json



phones={'Alex': {"phones":["+ 375 29 125 48 63", "+375 33 256 96 86"]},
'Dima': {"phones":["+375 29 859 63 12"]},
'Tasha': {"phones":["+375 33 269 56 26", "+375 29 526 36 98"]}}

def save():
    with open("phones.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(phones,ensure_ascii=False))
    print("Телефонный справочник добавлен в файл pfones.json")
while True:
    command=input('Изучите перечень команд через ввод цифры "0".Введите команду 0:')

    if command=="1":

        print('Список контактов: ')
        print(phones)
    elif command=="2":
        f=input('Введите имя контакта: ')
        k=input('Введите номер контакта: ')
        phones[f]=k
        save()
        print ("Номер был успешно добавлен в справочник")
    elif command == "0":
        print('1 - список контактов, 2 - добавить контакт, 3 - удалить контакт, 4 - сохранить измененный справочник, 5 - редактирование контакта, 6-поиск контакта, 7- загрузить измененный справочник')
    elif command=="3":
        f=input('Введите имя контакта, который нужно удалить:')  
        try:
            del phones[f]
            print('Контакт успешно удален')  
        except:
            print('Такого контакта нет в справочнике')   
    elif command == "5":
        n=input('Введите имя редактируемого контакта: ')
        q=phones[n]
        print(q)
        m=input('Введите отредактированное имя контакта: ')
        b=input('Ииедите отредактированный контакт: ')
        phones[n]=b
        phones[m] = phones[n]
        del phones[n]
        print('Контакт был успешно изменен')
        print(phones)
    elif command =="6":
        a=input('Введите имя контакта для поиска: ')
        with open("phones.json","r",encoding="utf-8") as fh:
            score =0
            while True:
                x=fh.readline()
                if a in x:
                    score+=1
                    print(phones[a])
                elif x=='':
                    if score>0:
                        break
                    else:
                        print("Таких данных нет")
                        break
  
    elif command=="7":
        with open ("phones.json","r",encoding="utf-8") as fh:
            phones=json.load(fh)
        print('Справочник был успешно загружен.')     
    else:
        print('Неопознанная команда. Просьба изучить мануал через команду /help')

