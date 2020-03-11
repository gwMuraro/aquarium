class Foncteur :
    def __init__(self, fonction, **kwargs): 
        setattr(self, "fonctionCallback", fonction(**kwargs))
