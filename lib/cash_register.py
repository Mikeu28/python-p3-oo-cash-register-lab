#!/usr/bin/env python3

class CashRegister:



    def __init__( self, discount = 0 ):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_price = 0
    
    def add_item( self, title, price, quantity = 1 ):
        items_price = price * quantity
        self.total += items_price
        self.last_price = items_price
        for i in range( quantity ):
            self.items.append(title)
            

    def apply_discount( self ):
        if( self.discount ):
            self.total *= 1 - ( self.discount / 100 )
            print( f"After the discount, the total comes to ${(int(self.total))}." )
        else:
            print( "There is no discount to apply." )

    def void_last_transaction( self ):
        self.total -= self.last_price
    
    
        