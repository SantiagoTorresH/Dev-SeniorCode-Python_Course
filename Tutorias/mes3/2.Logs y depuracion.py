#los losgs rastrean eventos 
#* tipos de eventos
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL 


import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s -%(levelname)s -%(message)s ")

logging.debug("Mensaje de depuracion")

