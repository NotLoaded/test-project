from os import walk
import os

directory = "./Python-Testing/Website-Generator/"
filename = "index.html"
filepath = os.path.join(directory,filename)
if not os.path.isdir(directory):
    os.mkdir(directory)



base_html = """
<html>
    <head>
        <title> </title>
    
       <style>
          img {
                width: 400px;
                height: 150px;
                object-fit: cover;
           }
        </style>
    </head>
    <body>
        <h1>Pictures</h1>
    </body>

    <body>
        <img src="img/1.png">
        <img src="img/2.png">
        <img src="img/3.jpg">
    </body>
</html>
"""

html = base_html

print(html)

with open(filepath, "w") as file:
    file.write(html)
