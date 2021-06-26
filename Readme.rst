Latex2Png Discord bot
==========
A not so good but okay version of a latex renderer for discord

I wrote the code in python 3.8
Packages:
.. code:: sh
    # Discord.py
    pip install -U discord.py
    
    # Matplotlib
    pip install -U matplotlib
    
    # Pillow
    pip install Pillow

Features:
========
it uses the logic given by Slabko in the following Stackexchange answer: https://stackoverflow.com/questions/1381741/converting-latex-code-to-images-or-other-displayble-format-with-python
It saves the rendered image in the form of a png file and send that png file to the discord channel
