import sys
from SEPA import SEPA
from JSAP import JSAP_file

    # Update sul grafo testpython
SEPA(JSAP_file).Update('INSERT DATA { GRAPH <http://testpython> { <http://a> <http://b> <http://Diciassette_Dicembre> } }')

    # Query sul grafo testpython
SEPA(JSAP_file).Query('SELECT * FROM <http://testpython> WHERE {?s ?p ?o}')

    # Websocket sul grafo testpython
SEPA(JSAP_file).Subscribe('select * from <http://test_python> where { ?s ?p ?o }')


