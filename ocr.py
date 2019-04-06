from pprint import pprint


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def disassembly_input(input_):
    list_of_chunks = []
    for line in input_.split('\n'):
        _chunks = list(chunks(line, 3))
        list_of_chunks.append(_chunks)
    return ["".join(x) for x in zip(*list_of_chunks)]


def get_numbers_dict():
    basic_input = (
        " _     _  _     _  _  _  _  _ \n"
        "| |  | _| _||_||_ |_   ||_||_|\n"
        "|_|  ||_  _|  | _||_|  ||_| _|\n"
        "                              "
    )
    numbers = disassembly_input(basic_input)
    numbers_dict = {}
    for x in range(10):
        numbers_dict[numbers[x]] = x
    return numbers_dict


NUMBERS_DICT = get_numbers_dict()


def scan(input_):
    result = ""
    for raw_string in disassembly_input(input_):
        result += str(NUMBERS_DICT.get(raw_string, "?"))
    return result


def checksum_calculation(input_):
    res = 0
    res_in_string = scan(input_)
    for idx, number_str in enumerate(res_in_string[::-1], 1):
        res += int(number_str) * idx
    res = res % 11
    return res == 0


def validated_scan(input_):
    pass


def guessed_scan(input_):
    pass


pprint(NUMBERS_DICT)

input_ = (
        " _  _  _  _  _  _  _  _    \n"
        "| || || || || || || ||_   |\n"
        "|_||_||_||_||_||_||_| _|  |\n"
        "                           "
    )

print(scan(input_))
