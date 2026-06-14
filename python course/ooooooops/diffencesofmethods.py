class amazon_store:
     count=0
     def __init__(self,name,price):
          self.name=name
          self.price=price
          amazon_store.count+=1
    

     @staticmethod
     def discount_(price,discount):
        final_amount=price-(price*discount/100)
        print(f" the final amount is {final_amount}")

     @classmethod
     def count_(cls):
         print(f"the total objects in store is ={cls.count}")


    
p1=amazon_store("phone",1000000)
p2=amazon_store("washing machine",10000)
amazon_store.count_()
amazon_store.discount_(1000000,10)