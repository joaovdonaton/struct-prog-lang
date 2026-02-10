import parser

def evaluate(ast):
    if ast['tag'] == 'number':
        return ast['value']
    elif ast['tag'] == '+':
        return evaluate(ast['left']) + evaluate(ast['right'])
    elif ast['tag'] == '-':
        return evaluate(ast['left']) - evaluate(ast['right'])
    elif ast['tag'] == '*':
        return evaluate(ast['left']) * evaluate(ast['right'])
    elif ast['tag'] == '/':
        return evaluate(ast['left']) / evaluate(ast['right'])
    else:
        raise ValueError(f'Unkown AST node {ast}')
    

def test_evaluate():
    print('test evaluate')

    # repo

    pass


if __name__ == '__main__':
    test_evaluate()