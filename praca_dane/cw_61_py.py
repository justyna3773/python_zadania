# Sparsuj przygotowanego XML (parserem SAX i DOM) i go
# zmodyfikuj np. zmień wartość któregoś tag’a i zapisz do nowego
# pliku

from xml.dom import minidom

file = minidom.parse('books.xml')

tags = file.getElementsByTagName( "title" )
file.getElementsByTagName( "title" )[ 0 ].childNodes[0].nodeValue = "Paradox Found"

with open('books1.xml', "w") as f:
    file.writexml(f)