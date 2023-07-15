import sys
import os

print("""<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Response</title>
</head>""")
print("<body>")
print(f"<p style='text-align:center'><strong>{sys.argv[1:]}</strong></p>")
print("<p style='text-align:center'><a href='/'>Back to home</a></p>")
print("</body>")
print("</html>")
