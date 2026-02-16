import parser

def evaluate(ast):
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])
    elif ast["tag"] == "-":
        return evaluate(ast["left"]) - evaluate(ast["right"])
    elif ast["tag"] == "*":
        return evaluate(ast["left"]) * evaluate(ast["right"])
    elif ast["tag"] == "/":
        return evaluate(ast["left"]) / evaluate(ast["right"])
    elif ast['tag'] == '%':
        return evaluate(ast["left"]) % evaluate(ast["right"])
    else:
        raise ValueError(f"Unknown AST node: {ast}")

def test_evaluate():
    print("test evaluate()")
    ast = {"tag": "number", "value": 3}
    assert evaluate(ast) == 3
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 3},
        "right": {"tag": "number", "value": 4},
    }
    assert evaluate(ast) == 7
    ast = {
        "tag": "*",
        "left": {
            "tag": "+",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 4},
        },
        "right": {"tag": "number", "value": 5},
    }
    assert evaluate(ast) == 35

    # test modulo
    ast = {
        "left": {
            "left": {"tag": "number", "value": 8},
            "right": {"tag": "number", "value": 4},
            "tag": "/",
        },
        "right": {"tag": "number", "value": 5},
        "tag": "%",
    }
    assert evaluate(ast) == 2
    
    ast = {
        "left": {"tag": "number", "value": 8},
        "right": {"tag": "number", "value": 4},
        "tag": "%",
    }
    assert evaluate(ast) == 0

if __name__ == "__main__":
    test_evaluate()
    print("done.")
