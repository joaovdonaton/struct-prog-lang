import re

patterns = [
    (r'\s+', 'whitespace'),
    (r'\d+', 'number'),
    (r'\+', '+'),
    (r'\-', '-'),
    (r'\/', '/'),
    (r'\*', '*'),
    (r'.', 'error'),
]

patterns = [((re.compile(p)), tag) for p, tag in patterns]

def tokenize(characters):
    tokens = []
    position = 0
    line, column = 1, 1
    current_tag = None

    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                current_tag = tag
                break

        assert match is not None

        value = match.group(0)

        if current_tag == 'error':
            raise Exception(f'Unexpected character: {value!r}')
    
        if current_tag != 'whitespace':
            token = {'tag': current_tag, 'line': line, 'column': column}
            if current_tag == 'number':
                token['value'] = int(value)
            tokens.append(token)

        for ch in value:
            if ch == '\n':
                line += 1
                column = 1
            else:
                column += 1
        position = match.end()

    tokens.append({'tag': None, 'line': line, 'column': column})

    return tokens


def test_digits():
    print('testing tokenize digits')

    t = tokenize('123')
    assert t[0]['tag'] == 'number'
    assert t[0]['value'] == 123
    assert t[1]['tag'] is None

    t = tokenize('1')
    assert t[0]['tag'] == 'number'
    assert t[0]['value'] == 1
    assert t[1]['tag'] is None


def test_operators():
    print('testing tokenize operators')

    t = tokenize('+ - * /')
    tags = [tok['tag'] for tok in t]
    assert tags == ['+', '-', '*', '/', None]


def test_expressions():
    t = tokenize('1+2*3')

    # notes


def test_whitespace():
    pass


def test_error():
    pass


if __name__ == '__main__':
    test_digits()
    test_operators()
    test_expressions()
    test_whitespace()
    test_error()
    print('done')
