def export_data():
    with open('oopUnit1/src/data/phone.csv', 'r', encoding="utf-8") as file:
        data = []
        t = []
        for line in file:
            if ':' in line:
                temp = line.strip().split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data
