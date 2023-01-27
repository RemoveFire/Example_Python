
def U12Task1():
    import codecs
    import json

    f = codecs.open("Unit12/Task12.ipynb", 'r')
    source = f.read()

    y = json.loads(source)
    pySource = '##Python code from jpynb:\n'
    for x in y['cells']:
        for x2 in x['source']:
            pySource = pySource + x2
            if x2[-1] != '\n':
                pySource = pySource + '\n'
    print(pySource)
