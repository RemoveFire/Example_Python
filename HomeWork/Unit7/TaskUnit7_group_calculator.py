import math


sanetize = lambda a: float(a)

symbols = {
    '%': lambda a, b: sanetize(a) % sanetize(b),
    '^': lambda a, b: sanetize(a) ** sanetize(b)
}


def calc(text):
    split = format(text)
    array = numpy.array(split)
    for symbol in symbols:
        count = split.count(symbol)
        for _ in range(count):
            # Find all symbol indices.
            indices = numpy.where(array == symbol)[0]

            for index in indices:
                result = symbols[symbol](split[index - 1], split[index + 1])
                text = text.replace(split[index - 1] + " " + symbol + " " + split[index + 1], str(result)).replace(
                    split[index - 1] + symbol + split[index + 1], str(result))
            split = format(text)
            array = numpy.array(split)

    return text

print(calc(input("Введите: ")))
