from tokenizer import tokenize

# expression = term { ("+" | "-") term }
# term = factor { ("*" | "/") factor }
# factor = <number> | "(" expression ")"

def parse_factor(tokens):
    # factor = <number>
    token = tokens[0]

    if token['tag'] == 'number':
        node = {'tag': 'number', 'value': token['value']}
        return node, tokens[1:]
    if token['tag'] == '(':
        node, tokens = parse_expression(tokens[1:])
        if tokens[0]['tag'] != ')':
            raise SyntaxError('Expected \')\'')
        return node, tokens[1:]
    
    assert False, f'Expected a number, but got {token}'


def test_parse_factor():
    print('test parse factor')
    tokens = tokenize('3')

    ast, tokens = parse_factor(tokens)
    assert ast == {'tag': 'number', 'value': 3}
    assert tokens == [{'tag': None, 'line': 1, 'column': 2}]


def parse_term(tokens):
    # term = factor { ("*" | "/") factor }
    left, tokens = parse_factor(tokens)

    while tokens[0]['tag'] in ['*', '/']:
        op = tokens[0]['tag']
        tokens = tokens[1:]
        right, tokens = parse_factor(tokens)
        left = {'tag': op, 'left' : left, 'right': right}

    return left, tokens


def test_parse_term():
    print('test parse_term')

    # repo

 
def parse_expression():
    # expression = term { ("+" | "-") term }
    pass
    # repo


def test_parse_expression():
    pass
    # res


def parse(tokens):
    ast, tokens = parse_expression(tokens)
    if tokens[0]['tag'] is not None:
        raise SyntaxError(f'Unexpected Token {tokens[0]}')
    return ast


if __name__ == '__main__':
    test_parse_factor()
    test_parse_term()