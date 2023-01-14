
def input_check(enter):
    login = None
    check = True
    while check:
        try:
            login = float(input(f"{enter}"))
            check = False
        except ValueError:
            print("Неверный ввод!")
    return login


def U11Task1():
    import codecs
    import json

    f = codecs.open("Unit11/Task.ipynb", 'r')
    source = f.read()

    y = json.loads(source)
    pySource = '##Python code from jpynb:\n'
    for x in y['cells']:
        for x2 in x['source']:
            pySource = pySource + x2
            if x2[-1] != '\n':
                pySource = pySource + '\n'
    print(pySource)


