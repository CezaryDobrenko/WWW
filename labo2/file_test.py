from cw2.file import FileManager

plik = FileManager('test.txt')
print(plik.read_file())
print(plik.update_file("Additional text to add to the end of the file."))