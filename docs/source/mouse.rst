Mouse events
============

Pygame Extra has a class just for mouse operations!

Let's take a look at what this class offers.

Position
--------

Using mouse.pos() we can get the position of the mouse, in tuple!

Clicked?
--------

Using mouse.clicked() we can check if the mouse is clicked, now since there's 3 mouse buttons, running this will return a bool list

Say we have our left mouse button pressed

[True, False, False]

Now, say we have our right mouse button pressed

[False, False, True]

Basically the syntax here is:

pe.mouse.clicked()
[Left, Middle, Right]
