# We use # https://github.com/bastikr/boolean.py
# (see their copyright at the bottom of the page, author == Sebastian Kraemer)
import boolean
import boolean_export

def test_expression():
    algebra = boolean.BooleanAlgebra()

    w = boolean.Symbol("w")
    x = boolean.Symbol("x")
    y = boolean.Symbol("y")
    z = boolean.Symbol("z")

    test_expr = (~w) & (z | (x & y & (~z)) | (~y | z))
    return test_expr.simplify()

expr = test_expression()

assert str(expr) == "~w&(x|~y|z)"

def paren(s):
    return f"({s})"

def OUT_AND(args):
    return paren(" AND ".join(str(arg) for arg in args))

def OUT_OR(args):
    return paren(" OR ".join(str(arg) for arg in args))

def OUT_NOT(args):
    assert len(args) == 1
    return paren(f"NOT {args[0]}")

def OUT_SYMBOL(arg):
    return arg.capitalize()

my_expr = boolean_export.export(expr, f_and=OUT_AND, f_or=OUT_OR, f_not=OUT_NOT, f_symbol=OUT_SYMBOL)
assert my_expr == "((NOT W) AND (X OR (NOT Y) OR Z))"
