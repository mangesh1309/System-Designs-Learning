class EagerLoading:
    __instance = None

    def __init__(self):
        if EagerLoading.__instance is None:
            EagerLoading.__instance = self
    
    @staticmethod
    def getInstance():
        return EagerLoading.__instance
    

obj1 = EagerLoading.getInstance()
obj2 = EagerLoading.getInstance()
obj3 = EagerLoading.getInstance()


print(obj1 is obj2 is obj2)