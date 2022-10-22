import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(levelname)s [%(filname)s]:%(lineno)s %(messaje)s', datefmt='%I:%M:%S %p', handlers=[log.FileHandler('./Notas/Unidad 2/Semana2 copy/capa_datos.log'), log.StreamHandler()])
if __name__=='__main__':
    log.debug("Mensaje debug") 