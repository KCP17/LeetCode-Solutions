class Solution():
    def buyChoco(self, prices, money):
        
        choco1_min = prices[0]
        for price in prices[1:]:
            if price < choco1_min:
                choco1_min = price

        prices.remove(choco1_min)
        
        choco2_min = prices[0]
        for price in prices[1:]:
            if price < choco2_min:
                choco2_min = price
        
        leftover = money - (choco1_min + choco2_min)
        return leftover if leftover >= 0 else money
