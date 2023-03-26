import boolean
# We use https://github.com/bastikr/boolean.py
# (see their copyright at the bottom of the page, author == Sebastian Kraemer)

def export(expr, *, f_and, f_or, f_not, f_symbol):
    def f(expr):
        if type(expr) == boolean.boolean.OR:
            return f_or([f(arg) for arg in expr.args])
        elif type(expr) == boolean.boolean.AND:
            return f_and([f(arg) for arg in expr.args])
        elif type(expr) == boolean.boolean.NOT:
            return f_not([f(arg) for arg in expr.args])
        elif type(expr) == boolean.boolean.Symbol:
            return f_symbol(expr.obj)
        else:
            assert False
    return f(expr)

