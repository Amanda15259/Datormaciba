#Autors: Amanda Beinarovica
#Fails varaviksne.py

from PythonMagick import Image

bilde = Image ( "7x4", "#22aaff" )

x = y = 0


bilde.pixelColor (0, 0, "#ff0000" )
bilde.pixelColor (0, 1, "#ff0000" )
bilde.pixelColor (0, 2, "#ff0000" )
bilde.pixelColor (0, 3, "#ff0000" )

bilde.pixelColor (1, 0, "#00008b" )
bilde.pixelColor (1, 1, "#00008b" )
bilde.pixelColor (1, 2, "#00008b" )
bilde.pixelColor (1, 3, "#00008b" )

bilde.pixelColor (2, 0, "#98fb98" )
bilde.pixelColor (2, 1, "#98fb98" )
bilde.pixelColor (2, 2, "#98fb98" )
bilde.pixelColor (2, 3, "#98fb98" )

bilde.pixelColor (3, 0, "#ffff00" )
bilde.pixelColor (3, 1, "#ffff00" )
bilde.pixelColor (3, 2, "#ffff00" )
bilde.pixelColor (3, 3, "#ffff00" )

bilde.pixelColor (4, 0, "#87ceeb" )
bilde.pixelColor (4, 1, "#87ceeb" )
bilde.pixelColor (4, 2, "#87ceeb" )
bilde.pixelColor (4, 3, "#87ceeb" )

bilde.pixelColor (5, 0, "#800080" )
bilde.pixelColor (5, 1, "#800080" )
bilde.pixelColor (5, 2, "#800080" )
bilde.pixelColor (5, 3, "#800080" )

bilde.pixelColor (6, 0, "#ff8c00" )
bilde.pixelColor (6, 1, "#ff8c00" )
bilde.pixelColor (6, 2, "#ff8c00" )
bilde.pixelColor (6, 3, "#ff8c00" )

bilde.scale ( "200x200" )

bilde.write ( "varaviksne.png" )
