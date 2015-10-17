class Wheels:
	def __init__(self,name, weight, cost, type):
		self.name = name
		self.weight = weight
		self.cost = cost
		self.type = type

class Frames:
	def __init__(self,name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost
		
class Bicycle(object):
	def __init__(self,name,weight,cost,man):
		self.name = name
		self.weight = weight
		self.cost = cost
		self.man = man
class Bicycle_Manufacturers:
	def __init__(self,name, margin):
		self.name = name
		self.margin = margin
		self.inventory = {}
	def produce_bicycle(self,Wheel,Frame,name):
		weight = Wheel.weight + Frame.weight
		cost = Wheel.cost + Frame.cost
		sale_cost = cost + (cost * float(self.margin)/100)
		return Bicycle(name, weight, sale_cost,self)
		
		#self.inventory[bicycle] = self.inventory[bicycle] + 1
class Bike_shop(object):
	def __init__(self,name,margin):
		self.name = name
		self.inventory = {}
		self.margin = margin
		self.profit = 0
	def buy_bicycle(self,bicycle,count):
		self.inventory[bicycle] = count
	def sell_bicycle(self, bicycle):
		self.inventory[bicycle] = self.inventory[bicycle] - 1
		self.profit = self.profit + self.calc_profit(bicycle)
	def calc_profit(self,bicycle):
		return bicycle.cost * (float(self.margin)/100)
	def print_inventory(self):
		for bicycle in self.inventory:
			print bicycle.name + " : " + str(self.inventory[bicycle])

class Customers(object):
	bicycles_owned = []
	def __init__(self,name,money):
		self.name = name
		self.money = money
		print "\n{}".format(self.name)
	def purchase_bicycle(self,bicycle,shop):
		print "Initial Balance is : " + str(self.money)
		sale_price = bicycle.cost + shop.calc_profit(bicycle)
		if sale_price <= self.money:
			shop.sell_bicycle(bicycle)
			self.bicycles_owned.append(bicycle)
			self.money = self.money - sale_price
			print bicycle.name + " cost "+ str(sale_price) + ". That leaves " + self.name + " with " + str(self.money)
			
	def list_affordable_bicycles(self,shop):
		for bicycle in shop.inventory:
			
			sale_price = bicycle.cost + shop.calc_profit(bicycle)
			if sale_price <= self.money:
				
				print bicycle.name + " costs " + str(sale_price) + ". Money available is " + str(self.money)
				
    		
    		
