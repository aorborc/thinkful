from bicycle import Bicycle, Bike_shop,Customers,Wheels,Frames,Bicycle_Manufacturers

# Creating Manufacturers
man1 = Bicycle_Manufacturers("Ruben Bars",15)
man2 = Bicycle_Manufacturers("Hercules",25)

#Creating Wheels
wheel1 = Wheels("Alloy",3,10,"type1")
wheel2 = Wheels("Spoke",2,8,"type2")
wheel3 = Wheels("Wire",5,100,"type3")

#Creating Frames
frame1 = Frames("aluminum",10,20)
frame2 = Frames("carbon",5,200)
frame3 = Frames("steel",6,500)

# Producing Bicycles

bicycle1 = man1.produce_bicycle(wheel1,frame1,"Ranger")
bicycle2 = man2.produce_bicycle(wheel1,frame2,"Danger")
bicycle3 = man1.produce_bicycle(wheel1,frame3,"Stranger")
bicycle4 = man2.produce_bicycle(wheel2,frame3,"Gamer")
bicycle5 = man1.produce_bicycle(wheel3,frame3,"Toner")
bicycle6 = man2.produce_bicycle(wheel3,frame2,"Fiver")

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