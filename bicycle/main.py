from bicycle import Bicycle, Bike_shop,Customers

bicycle1 = Bicycle("Ranger",8,25)
bicycle2 = Bicycle("Danger",9,1200)
bicycle3 = Bicycle("Stranger",7,800)
bicycle4 = Bicycle("Gamer",8,450)
bicycle5 = Bicycle("Toner",2,605)
bicycle6 = Bicycle("Fiver",4,300)

LavaCycles = Bike_shop("Lava Cycles",20)
LavaCycles.buy_bicycle(bicycle1,100)
LavaCycles.buy_bicycle(bicycle2,100)
LavaCycles.buy_bicycle(bicycle3,100)
LavaCycles.buy_bicycle(bicycle4,100)
LavaCycles.buy_bicycle(bicycle5,100)
LavaCycles.buy_bicycle(bicycle6,100)


Ruben = Customers("Ruben",200)
Ruben.purchase_bicycle(bicycle1,LavaCycles)
print " \n"
#Ruben.list_affordable_bicycles(LavaCycles)
Jesse = Customers("Jesse",500)
Jesse.purchase_bicycle(bicycle6,LavaCycles)
print " \n"
#Jesse.list_affordable_bicycles(LavaCycles)
Bangs = Customers("Bangs",1000)
print " \n"
#Bangs.list_affordable_bicycles(LavaCycles)
Bangs.purchase_bicycle(bicycle5,LavaCycles)
print " \n"
print "Lava Cycles Inventory and profit is below"
LavaCycles.print_inventory()
print LavaCycles.profit