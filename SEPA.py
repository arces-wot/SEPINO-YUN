import json
import websocket
from requests import post

"""
Questa classe permette di istanziare degli oggetti attraverso i quali posso effettuare delle Update, Query e Subscribe,
i parametri necessari ad effettuare tutte le operazioni verranno presi dal File JSAP passato come argomento in ingresso
alla classe, init infatti come prima cosa effettua un parsing del JSAP (scritto in JSON) trasformandolo in dict Python.
"""

class SEPA:

    """
    Inizializzo la classe SEPA facendo il parsing dei file
    """

    def __init__(self, file_to_parse):
        self.parametri = json.loads(file_to_parse)

    """
    Faccio un Update sfruttando il metodo post di requests, esso accetta come parametri in ingresso: URL a cui fare la richiesta, 
    testo SPARQL passato come stringa in ingresso al metodo, header da inserire nella richiesta  
    
    """

    def Update(self, update_txt):
        update_URL = str(self.parametri["sparql11protocol"]["protocol"]) + "://" + str(self.parametri["host"]) + ":" + str(self.parametri["sparql11protocol"]["port"]) + str(self.parametri["sparql11protocol"]["update"]["path"])
        r = post(update_URL, data=update_txt, headers={'Content-Type': 'application/sparql-update'})
        print(r.text)

    """"
    Fa' una Query con una HTTP post molto simile alla precedente 
    """

    def Query(self, query_txt):
        query_URL = str(self.parametri["sparql11protocol"]["protocol"]) + "://" + str(self.parametri["host"]) + ":" + str(self.parametri["sparql11protocol"]["port"]) + str(self.parametri["sparql11protocol"]["query"]["path"])
        r = post(query_URL, data=query_txt, headers={'Content-Type': 'application/sparql-query'})
        print(r.text)

    """
    Apre una Websocket con il SEPA sfruttando la libreria WebSocket_client e stampa a video il contenuto delle notifiche
    specificando soggetto, predicato e oggetto 
    """

    def Subscribe(self, websocket_txt):

        websockets_URL= str(self.parametri["sparql11seprotocol"]["protocol"]) + "://" + str(self.parametri["host"]) + ":" + str(self.parametri["sparql11seprotocol"]["availableProtocols"]["ws"]["port"]) + str(self.parametri["sparql11seprotocol"]["availableProtocols"]["ws"]["path"])

        try:
            import thread

        except ImportError:
            import _thread as thread

        def on_message(ws,message):
            notifica = json.loads(message)

            if (notifica["notification"]["sequence"] == 0):
                print("Abbiamo aperto una Websocket!")
            else:
                """  Invoco una funzione di callback ogni volta che riceviamo una notifica dalla sottoscrizione  """
                callback(notifica)

        def callback(notifica):
            if (bool(notifica["notification"]["addedResults"]["results"]["bindings"])):
                soggetto_added = (
                    notifica["notification"]["addedResults"]["results"]["bindings"][0]["s"]["value"]).replace('http://', '')
                predicato_added = (
                    notifica["notification"]["addedResults"]["results"]["bindings"][0]["p"]["value"]).replace('http://', '')
                oggetto_added = (
                    notifica["notification"]["addedResults"]["results"]["bindings"][0]["o"]["value"]).replace('http://', '')

                """  Stampo a video il dato aggiunto al grafo a cui siamo sottoscritti  """

                print("E' stato aggiunto un dato:\n"
                      "soggetto: " + soggetto_added + "\n" +
                      "predicato: " + predicato_added + "\n" +
                      "oggetto: " +oggetto_added)
            else:
                soggetto_removed = (
                    notifica["notification"]["removedResults"]["results"]["bindings"][0]["s"]["value"]).replace('http://', '')
                oggetto_removed = (
                    notifica["notification"]["removedResults"]["results"]["bindings"][0]["o"]["value"]).replace('http://', '')
                predicato_removed = (
                    notifica["notification"]["removedResults"]["results"]["bindings"][0]["p"]["value"]).replace('http://', '')

                """  Stampo a video il dato rimosso al grafo a cui siamo sottoscritti  """

                print("E' stato rimosso un dato:\n"
                      "soggetto: " + soggetto_removed + "\n" +
                      "predicato:" + oggetto_removed + "\n" +
                      "oggetto:" +predicato_removed)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")


        def on_open(ws):
            print("Apertura della Websocket, inviamo la richiesta...")
            ws.send(json.dumps({"subscribe": {"sparql": websocket_txt}}))

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(websockets_URL, on_message=on_message, on_error=on_error, on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()

