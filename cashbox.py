class Purse:

    

    def __init__(self, valuta, name= 'Unknown'):
        if valuta not in ('USD', 'EUR'):
           raise ValueError ('') 
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany


    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('0')
            raise ValueError ('0')
        self.__money = self.__money - howmany
        return howmany


    def info(self):
        print(self.__money) 


    def __del__(self):
        print('delite')
         




x = Purse('USD') 
y = Purse('EUR', 'Bill') 
x.top_up_balance(100)
y.top_up_balance(17)
#
x.info()
y.info()
x.top_down_balance(y.top_down_balance(7))    
