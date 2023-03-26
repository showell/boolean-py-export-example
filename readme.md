This is a very small example of using the [boolean.py](https://github.com/bastikr/boolean.py)
library to simplify boolean expressions.

Their library allows me to construct a boolean expression like so:

<pre>
(~w) & (z | (x & y & (~z)) | (~y | z))
</pre>

And then the library simplifies it as this (super cool!):

<pre>
~w&(x|~y|z)
</pre>

You can details on how to do this yourself in their excellent [documentation](https://booleanpy.readthedocs.io/en/latest/index.html).

You can also see me doing it [example.py](./example.py).

## Exporting expressions ##

For my use case I want to let `boolean.py` do the heavy lifting of simplifying
a boolean expression.  But then once that happens, I want to export the expression
from `boolean.py` into my own system of objects.

Here is the code that I wrote to do that, which you will find in [boolean_export.py](./boolean_export.py):

<pre>
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
</pre>

The code works fine for me, but it is obviously relying on some implementation details
of their library.


Here is what I do with `export` inside [example.py](./example.py):

<pre>

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
</pre>

In my actual use case I want to do something a bit more sophisticated than just rendering the
expression in ALL-CAPS, but I believe that my `export` function will handle a lot of typical
use cases.

## Feature request ##

I am hoping that the folks who maintain `boolean.py` will consider adding my export function into
the library and supporting it.  For now I filed https://github.com/bastikr/boolean.py/issues/116
