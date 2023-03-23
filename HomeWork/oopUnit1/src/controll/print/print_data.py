def print_data(data):
    if len(data) > 0:
        print("Surname".center(20), "Name".center(20), "Patronymic".center(20), "Date of birth".center(20),
              "Telephone".center(15))
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15))
    else:
        print("The directory is empty!")
