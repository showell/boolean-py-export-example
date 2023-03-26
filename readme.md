This is a very small example of using the [boolean.py](https://github.com/bastikr/boolean.py)
library to simplify boolean expressions.

The library allows you to construct a boolean expression like so:

<pre>
(~w) & (z | (x & y & (~z)) | (~y | z))
</pre>

And then it simplifies it:

<pre>
~w&(x|~y|z)
</pre>

You can details on how to do this yourself in their excellent [documentation](https://booleanpy.readthedocs.io/en/latest/index.html).

You can also see me doing it [example.py](./example.py).
