#private attribute
#public and  protected

class bankaccount:
    def __init__(self,name,balance,id):
        self.name=name #public
        self._balance=balance#protected
        self.__id=id#private


    def get_balance(self):
        return self.__id

acc1= bankaccount("hari",100202,32)

print(acc1.name,acc1._balance,acc1.get_balance())
#in private only we cannot accees a element
#we can accese a private data as well we
# write acc1._class name__balance