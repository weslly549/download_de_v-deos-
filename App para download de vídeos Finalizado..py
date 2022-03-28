import webbrowser

url = input("cole aqui a url:")
url = url[:12]+"ss"+url[12:]
webbrowser.open(url)

