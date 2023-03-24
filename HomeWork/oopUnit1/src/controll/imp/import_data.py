def import_data(data):
    sep = ":"
    with open('oopUnit1/src/data/phone.csv', 'a+', encoding="utf-8") as file:
        file.write(sep.join(data))
        file.write(f"\n")
