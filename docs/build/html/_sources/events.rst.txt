Events
======

While simple you might get lost in how to use events, but it's really simple, let's take a look at all the events!

Setup
+++++

Events are setup in your game loop, and run every frame.

Here is how to setup the events:

.. code-block:: python

    for pe.event.c in pe.event.get():
      #PUT EVENTS HERE
      
Now we just replace ``#PUT EVENTS HERE`` with the included events.

One of the events you'll use in probably every game / application is the quitcheckauto.

event.quitcheckauto()
---------------------

Like the name stands Quit Check Auto, automatically closes the game / application if the "X"  button is pressed.

If you want another action when "X" is pressed like a save action, then you can use quitcheck.

event.quitcheck()
-----------------

Like the name stands Quit Check will check if the "X" button is pressed and return a bool.

Here is an example of it's use:

.. code-block:: python

    if pe.event.quitcheck():
      save()
      pe.Pquit()
      quit()

event.keylog()
--------------

This is a testing function, it logs the key number of any key that get's pressed or released and returns it.

event.keyUP(var)
----------------

This is the key up event, using keylog we can see what value to feed this function, after that we get a bool

Here is an example of it's use:

.. code-block:: python

    if pe.event.keyUP(119):
      jump()

event.keyDOWN(var)
------------------

This is the key down event, using keylog we can see what value to feed this function, after that we get a bool

Here is an example of it's use:

.. code-block:: python

    if pe.event.keyDOWN(115):
      sneak()