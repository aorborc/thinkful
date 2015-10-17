class Band(object):
	members = []
	def hire_musician(self,member):
		self.members.append(member)
		print self.members
	def fire_musician(self,member):
		self.members.remove(member)
	
	def play_solo(self,length):
		for i in self.members:
			print self.members[i].isDrummer

class Musician(object):
    def __init__(self, sounds,isDrummer):
        self.sounds = sounds
        self.isDrummer = isDrummer
        
    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician):
	def __init__(self):
		# Call the __init__ method of the parent class
		super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"],False)

class Guitarist(Musician):
	def __init__(self):
		# Call the __init__ method of the parent class
		super(Guitarist, self).__init__(["Boink", "Bow", "Boom"],False)
	
	def tune(self):
		print "Be with you in a moment"
		print "Twoning, sproing, splang"
class Drummer(Musician):
	def __init__(self):
		super(Drummer, self).__init__(["Hi", "Hat"],True)


Jingle = Band()
ruben = Drummer()
nigel = Guitarist()
Jingle.hire_musician(ruben)
