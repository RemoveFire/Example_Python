from oopUnit1.src.controll.imp.import_data import import_data
from oopUnit1.src.controll.exp.export_data import export_data
from oopUnit1.src.controll.print.print_data import print_data
from oopUnit1.src.controll.search.search_data import search_data


def input_data():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    middle_name = input("Enter your patronymic: ")
    brith_name = input("Enter your date of birth: ")
    phone_number = input("Enter the contact number: ")
    return [last_name, first_name, middle_name, brith_name, phone_number]


def input_telefon():
    print("Available phone book operations:\n\
    1 - import;\n\
    2 - export;\n\
    3 - contact search.")
    ch = input("Enter a number: ")
    if ch == '1':
        import_data(input_data())
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Enter the search data: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Surname".center(20), "Name".center(20), "Patronymic".center(20), "Date of birth".center(20),
                  "Telephone".center(15))
            print("-" * 95)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15))
        else:
            print("No data detected")
