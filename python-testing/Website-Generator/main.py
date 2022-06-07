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


semicolon = ";"

html_b1 = """
<html>
    <head>
        <title> </title>
    
       <style>
          img {
"""

html_img_bhw1 = """                width: """
html_img_bhh1 = """
                height: """

html_b2 = """
                object-fit: cover;
           }
        </style>
    </head>
    <body>
        <h1>"""

html_b3 = """</h1>
    </body>

    <body>
"""


html_b4 = """    </body>
</html>"""


html_img_sd1 = '''        <img src="'''
html_img_sd2 = '''">
'''


html_t = "HDF = Halt die fresse"


img_cw = "400px"
img_ch = "400px"
img_1 = "img/1.PNG"
img_2 = "img/2.png"
img_3 = "img/3.jpg"



html_img = html_img_sd1 + img_1 + html_img_sd2 + html_img_sd1 + img_2 + html_img_sd2 + html_img_sd1 + img_3 + html_img_sd2

html = html_b1 + html_img_bhw1 + img_cw + semicolon + html_img_bhh1 + img_ch + semicolon + html_b2 + html_t + html_b3 + html_img + html_b4



print(html)


with open(filepath, "w") as file:
    file.write(html)
