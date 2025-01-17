class nuevoCanal:
    def __init__(self):
        self._suscriptor = []
        self.laters_news = None
        
        
    def suscribir(self, suscribirse):
        self._suscriptor.append(suscribirse)
        
    def desuscribir(self, desuscribirse):
        self._suscriptor.remove(desuscribirse)        
        
    def noti(self):
        for sus in self._suscriptor:
            sus.update(self._laters_news)   
            
    def publicacion(self, news):
        self._laters_news = news
        print(f"notificacion publicada: {news}")
        self.notificacion()
        
class suscriptores:
    def __init__(self, name):
        self.name = name
        
    def update(self, news):
        print(f"{self.name} ha recibido la notificacion: {news}") 
        
canalDevSeniorCode = nuevoCanal()

sus1 = suscriptores("Juan")                       
sus2 = suscriptores("San")                       
sus3 = suscriptores("Lin")                                         
            
canalDevSeniorCode.suscribir(sus1)            
canalDevSeniorCode.suscribir(sus2)            
            
canalDevSeniorCode.publicacion("Tenemos tutoria el dia de hoy")             