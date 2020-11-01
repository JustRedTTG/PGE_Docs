Sprites
=======

Sprites are a great part of Pygame Extra!

Let's see how to use them!

Making
------

Let's make a sprite, here is the syntax, running this will return the sprite object:

.. code-block:: python

    sprite.make(imagef, size, position, rotation)

Now let's go over everything:

* imagef - this is the image file, aka the sprite file
* size - the sprite size in pixels, aka the image size
* position - the center position of the sprite
* rotation - the rotation of the sprite, this is automatically set to 90, so you don't have to set it, unless you want the image to start off rotated

Great, now a the variables of a sprite:

* image - the loaded image object
* rotation - the rotation value
* position - the center position value or (x,y)
* rect - aka size
* size - the size multiplier of the sprite, this is one by default
* new - the updated image aka the current sprite with all its values loaded on
* refresh - this is a variable for the user to use, to keep track of wheather a sprite should be updated, this variable is only in place to save time, it's set to True by default

There's something very important to keep in mind, when you edit a sprite's variables, that really all your doing, editing variables, to make pygame use this valiables to make the new image we do:

.. code-block:: python

    spriteOBJ.init(spriteOBJ)
    
If you don't want to init the entire sprite that's fine, there's an init for everything seperately!

.. code-block:: python

    spriteOBJ.init_rotation(spriteOBJ)

.. code-block:: python

    spriteOBJ.init_position(spriteOBJ)

All sprite inits return the "new" aka "spriteOBJ.new" variable, witch has been updated, from there you can display it with:

.. code-block:: python

    sprite.display(spriteOBJ)
    
Let's put all that knowledge into making a sprite!

.. code-block:: python

    import pygameextra as pe
    pe.display.make((500, 500), 'My Game')
    pe.fill.full((255,255,255))
    crown = pe.sprite.make('example.jpeg',(100,100),(250,250), 70)
    crown.init(crown)
    while not pe.event.quitcheck():
      pe.sprite.display(crown)
      pe.display.update()
    pe.quit()
    quit()
