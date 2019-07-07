### PYTHON MODULE Actions
from queue import *
import System


# Define Actions
def serverInfo(system, element):
        status = 'Error'
        resStr = 'Error Found'
        try:
                if element.lower() == "version":
                        status = "Success"
                        resStr = "Service Name: AaReyS | Version: 0.1.0" 
                else:
                        status = "Failed"
                        resStr = "Parameter Not correct. Please check." 

        except:
                status = 'Error'
                resStr = 'Error found'
        res = {"Status": status, "Response": resStr}
        return res

def listCreate(system, listName = None, value = None):
        status = 'Failed'
        resStr = ''
        if listName is None:
                resStr = 'No name present to create list'
        if value == '' or value == None:
                resStr = 'No List Created'
        if system.regAddList(listName):
                status = 'Success'
                resStr = 'List is created. No Value is present to insert'
        else:
                if not system.findRegList(listName):
                        if system.regAddList(listName):
                                l = system.getList(listName)
                                l.append(value)
                                status = 'Success'
                                resStr = 'Value is added in List'
                else:
                        resStr = 'LIST already present'
        res = {"Status":status, "Response":resStr}
        #print system.LISTREG
        return res

def listInsertItem(system, listName, value):
        status = 'Failed'
        resStr = ''
        if listName is None:
                resStr = 'No name present to create list'
                if value == '':
                        resStr = 'No data present'
        else:
                if value is not None:
                        if system.findRegList(listName):
                                l = system.getList(listName)
                                found = False
                                for v in l:
                                        if v == value:
                                                found = True
                                                break
                                if not found:
                                        l.append(value)
                                        status = 'Success'
                                        resStr = 'Value is added in List'
                                else:
                                        resStr = 'Value is already Present'
                                        res = {"Status":status, "Response":resStr}
        #print system.LISTREG
        return res


def listUpdateItem(system, listName, value1, value2 ):
        pass

def listGetAllItem(system, listName):
        status = 'Failed'
        resStr = ''
        data = []
        try:
                if system.findRegList(listName):
                        data = system.getList(listName)
                        status = 'Success'
        except:
                resStr = 'Error found'
        res = {"Status":status, "Response":resStr, "Data":data}
        #print system.LISTREG
        return res

def listFindItem(system, listName, value ):
        status = 'Failed'
        resStr = 'Not Found in LIST'
        try:
                if system.findRegList(listName):
                        l = system.getList(listName)
                        status = 'NotFound'
                        resStr = 'Item not in LIST'
                        for item in l:
                                if item == value:
                                        status = 'Found'
                                        resStr = 'Item found in LIST'
                                        break

        except:
                resStr = 'Error found'
        res = {"Status":status, "Response":resStr}
        #print system.LISTREG
        return res


def listDeleteItem(system, listName, value):
        status = 'Error'
        resStr = 'Error Found'
        try:
                if system.findRegList(listName):
                        l = system.getList(listName)
                        status = 'NotFound'
                        resStr = 'Item not in LIST'
                        try: 
                                l.remove(value)
                                status = 'Success'
                                resStr = 'Item Removed from LIST'
                        except:
                                status = 'Failed'
                                resStr = 'Item not in LIST'
                else:
                        status = 'Failed'
                        resStr = 'LIST not Found'
        except:
                resStr = 'Error found'
        res = {"Status":status, "Response":resStr}
        #print system.LISTREG
        return res

def listDelete(system, listName):
        status = 'Error'
        resStr = 'Error Found'
        try:
                if system.findRegList(listName):
                        l = system.getList(listName)
                        if system.regDelList(listName):
                                status = 'Success'
                                resStr = 'LIST is Deleted'
                        else:
                                status = 'Failed'
                                resStr = 'LIST Deletion Failed'
                else:
                        status = 'Failed'
                        resStr = 'LIST not Found'
        except:
                resStr = 'Error found'
        res = {"Status":status, "Response":resStr}
        #print system.LISTREG
        return res

def listDeleteAll(system):
        status = 'Failed'
        resStr = 'Deletion Failed'
        try:
                if system.delRegAllList():
                        status = 'Success'
                        resStr = 'All LIST is cleared'
        except:
                status = 'Error'
                resStr = 'Error found'
        res = {"Status": status, "Response": resStr}
        return res

def listGetAll(system):
        status = 'Failed'
        resStr = 'No Data Found'
        try:
                nameList = system.getRegList()
                status = 'Success'
                resStr = 'List data present'
        except:	
                nameList = []
                status = 'Error'
                resStr = 'Error Found'

        res = {"Status": status, "Response": resStr, "data": nameList}
        return res


def queueCreate(system, qName, value = None):
        status = 'Failed'
        resStr = 'Error Found'
        if qName is None:
                resStr = 'No name present in Name Argument'
        if value == '' or value == None:
                if system.regAddQueue(qName):
                        status = 'Success'
                        resStr = 'Queue is Created'

                else:
                        if not system.findRegQueue(qName):
                                if system.regAddQueue(qName):
                                        d = system.getQueueDict()
                                        d[qName].put_nowait(value)
                                        status = 'Success'
                                        resStr = 'Value is added in Queue'
                        else:
                                resStr = 'Queue already present'

        res = {"Status":status, "Response":resStr}
        return res

def queuePut(system, qName, value):
        status = 'Failed'
        resStr = ''
        if qName is None:
                resStr = 'No name present in Name Argument'
        if value == '':
                resStr = 'No data present'
        else:
                if system.findRegQueue(qName):
                        d = system.getQueueDict()
                        d[qName].put_nowait(value)
                        status = 'Success'
                        resStr = 'Value is added in Queue'
                else:
                        resStr = 'Queue is not found'

        res = {"Status":status, "Response":resStr}
        return res


def queueGet(system, qName):
        status = 'Failed'
        resStr = ''
        item = None
        if qName is None:
                resStr = 'No name present in Name Argument'
        else:
                if system.findRegQueue(qName):
                        d = system.getQueueDict()
                        if d[qName].empty():
                                resStr = "Queue is empty"
                        else:
                                item = d[qName].get_nowait()
                                resStr = str(item)
                                status = 'Success'
                else:
                        resStr = 'Queue is Not Present'

        res = {"Status":status, "Response":resStr, "data":item }
        return res


def queueIsEmpty(system, qName):
        status = 'Failed'
        resStr = 'Error Found'
        item = None
        emptyFlag = True
        if qName is None:
                resStr = 'No name present in Name Argument'
        else:
                if system.findRegQueue(qName):
                        d = system.getQueueDict()
                        resStr = "Queue is Empty"
                        if not d[qName].empty():
                                emptyFlag = False
                                resStr = "Queue is not Empty"
                                status = 'Success'
                else:
                        resStr = 'Queue is Not Present'

        res = {"Status":status, "Response":resStr, "Empty":emptyFlag }
        return res

def queueDeleteItem(system, qName):
        pass
        

def queueDelete(system, qName):
        status = 'Error'
        resStr = 'Error Found'
        if True:
                if system.delFromRegQueue(qName):
                        status = 'Success'
                        resStr = 'QUEUE is Deleted'
                else:
                        status = 'Failed'
                        resStr = 'QUEUE Deletion Failed'
        else:
                resStr = 'Error found'
        res = {"Status":status, "Response":resStr}
        #print system.LISTREG
        return res

def queueGetAll(system):
        status = 'Failed'
        resStr = 'No Data Found'
        try:
                nameList = system.getRegQueue()
                status = 'Success'
                resStr = 'List data present'
        except:
                nameList = []
                status = 'Error'
                resStr = 'Error Found'
        res = {"Status": status, "Response": resStr, "data": nameList}
        return res



def queueDeleteAll(system):
        status = 'Failed'
        resStr = 'Deletion Failed'
        try:
                if system.delRegAllQueue():
                        status = 'Success'
                        resStr = 'All QUEUE is cleared'
        except:
                status = 'Error'
                resStr = 'Error found'
        res = {"Status": status, "Response": resStr}
        return res

