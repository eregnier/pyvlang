PyVlang
=======

This is wrapper around v language usable from python.

How does it works
-----------------

This package expects there is an available v program you machine path. Then it generates c code from v sources and builds a library from it.

Then the python ctype is used to call compiled library code.

Usage
-----

Compile v file:

```python
from pyvlang import VLang

VLang.make_lib("test.v", "/tmp/test-pyvlang.so")
```

Use generated library:

```python
from pyvlang import VLang

lib = VLang("./test.so")
assert lib.add(1, 2) == 3
```

Development
-----------

Use the Makefile to setup a working environement : `make install`

Test
----

Use Makefile to trigger tests : `make test` (requires a make install)

Note
----

This is an early buggy version at the moment. It just starts to work.

Licence
-------

MIT
