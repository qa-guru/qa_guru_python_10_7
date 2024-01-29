from zipfile import ZipFile


with ZipFile("Архив.zip") as reader:
    print(reader.namelist())
    text = reader.read("hello_extend").decode()
    print(text)
    reader.extract("new_image.svg", "resources")

