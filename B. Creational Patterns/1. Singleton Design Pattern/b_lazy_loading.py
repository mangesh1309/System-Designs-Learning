# Simple lazy laoding - has race around conditions 
class LazyLoadingSimple:
    __instance = None

    def __init__(self):
        if LazyLoadingSimple.__instance is None:
            LazyLoadingSimple.__instance = self

    @staticmethod
    def getInstance():
        if LazyLoadingSimple.__instance is None:
            return LazyLoadingSimple()
        return LazyLoadingSimple.__instance

# Safe Lazy Loading - May slow down the application in high-concurrency scenarios.
from threading import Lock

class LazyLoadingSingleLock:
    __instance = None
    __lock = Lock()

    def __init__(self):
        if LazyLoadingSingleLock.__instance is None:
            LazyLoadingSingleLock.__instance = self

    @staticmethod
    def getInstance():
        with LazyLoadingSingleLock.__lock:
            if LazyLoadingSingleLock.__instance is None:
                return LazyLoadingSingleLock()
        return LazyLoadingSingleLock.__instance

# Safe Lazy Loading - Double-Checked Locking
from threading import Lock

class LazyLoadingDoubleLock:
    __instance = None
    __lock = Lock()

    def __init__(self):
        if LazyLoadingDoubleLock.__instance is None:
            LazyLoadingDoubleLock.__instance = self

    @staticmethod
    def getInstance():
        if LazyLoadingDoubleLock.__instance is None:
            with LazyLoadingDoubleLock.__lock:
                if LazyLoadingDoubleLock.__instance is None:
                    return LazyLoadingDoubleLock()
        return LazyLoadingDoubleLock.__instance
    
obj1 = LazyLoadingSingleLock.getInstance()
obj2 = LazyLoadingSingleLock.getInstance()
obj3 = LazyLoadingSingleLock.getInstance()


print(obj1 is obj2 is obj2)