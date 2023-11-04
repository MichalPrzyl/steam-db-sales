def __insert (source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]

def format_price(input_price: int):
    coma_index = -2
    str_price = str(input_price)
    new_str = __insert(str_price, ",", coma_index)
    return new_str

def color(color):
    return {
            'HEADER': '\033[95m',
            'OKBLUE': '\033[94m',
            'OKCYAN': '\033[96m',
            'OKGREEN': '\033[92m',
            'WARNING': '\033[93m',
            'FAIL': '\033[91m',
            'ENDC': '\033[0m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m',
    }[color]