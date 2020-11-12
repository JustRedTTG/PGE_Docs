Math
====

Let's look at some math functions!

Rect Center
-----------

Using math.center we can get the center position of a rect.

Syntax:

.. code-block:: python

    math.center(rect)

So if you do the following, for example:

.. code-block:: python

    print(math.center((0,0,100,100)))

The rect starts at 0,0 and expands 100 x 100 this means the middle of this rect is at 50, 50 and this is exactly what this returns

.. code-block:: python

    (50,50)

Perspective
-----------

I myself forgot what this did, witch is funny, but i'll try to tell you what it does.

Syntax:

.. code-block:: python

    math.perspective(point_a, point_b, length)

Now as far as i remmember, this starts at point_a and goes length distance to point_b.
Imagine this as the walk function in scrath, the function places itself on point_a and looks toward point_b, it then walks toward point_b for the length of distance given.

I hope you understand what i mean but here is an image to help with what i just explained 
