### PYTHON MODULE for SYSTEM
#
##======================================================================
#
#  CAUTION: NEVER CHANGE ANYTHING IN THIS FILE
#
#  This is a System FILE
#
#==========================================================================

# Define SYSTEM REGISTRY variables:
#LISTREG = dict()
#QUEUEREG = dict()
from queue import *

import time

time.time()


# define some functions
class Registry:
        def __init__(self):
                self.LISTREG = dict()
                self.QUEUEREG = dict()
        def regAddList(self, listName):
                try:
                        if listName not in self.LISTREG:
                                l = list()
                                self.LISTREG.update({listName:l})
                        return True
                except:
                        return False
        def getList(self, listName):
                try:
                        if listName in self.LISTREG:
                                return self.LISTREG[listName]
                        else:
                                return []
                except:
                        return []
        def regDelList(self, listName):
                try:
                        if listName in self.LISTREG:
                                del self.LISTREG[listName]
                                return True
                        else:
                                return False
                except :
                        return False
        def findRegList(self, listName):
                try:
                        if listName in self.LISTREG:
                                return True
                        else:
                                return False
                except:
                        return False

        def getRegList(self):
                return list(self.LISTREG)
        def regAddQueue(self, qName):
                try:
                        if qName not in self.QUEUEREG:
                                q = Queue()
                                self.QUEUEREG.setdefault(qName, q)
                                #self.QUEUEREG[qName] = q
                        return True
                except:
                        return False
        def getQueueDict(self):
                return self.QUEUEREG
        def findRegQueue(self, qName):
                if qName in self.QUEUEREG:
                        return True
                else:
                        return False
        def getRegQueue(self):
                return list(self.QUEUEREG)
        def delFromRegQueue (self, qName):
                try:
                        if qName in self.QUEUEREG:
                                del self.QUEUEREG[qName]
                                return True
                        else:
                                return False
                except:
                        return False
        def delRegAllList(self):
                try:
                        self.LISTREG = dict()
                        return True
                except:
                        return False
        def delRegAllQueue(self):
                try:
                        self.QUEUEREG = dict()
                        return True
                except:
                        return False