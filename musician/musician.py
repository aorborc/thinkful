class Band(object):
	def __init__(self):
		self.members = []
	def hire_musician(self,member):
		self.members.append(member)
		
	def fire_musician(self,member):
		self.members.remove(member)
	
	def play_solo(self,length):
		for member in self.members:
			if isinstance(member,Drummer):
				member.solo(4)
	
		for member in self.members:
			if not isinstance(member,Drummer):
				member.solo(length)

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician):
	def __init__(self):
		# Call the __init__ method of the parent class
		super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
	def __init__(self):
		# Call the __init__ method of the parent class
		super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
	
	def tune(self):
		print "Be with you in a moment"
		print "Twoning, sproing, splang"
class Drummer(Musician):
	def __init__(self):
		super(Drummer, self).__init__(["Hi", "Hat"])


Jingle = Band()
ruben = Drummer()
nigel = Guitarist()

Jingle.hire_musician(ruben)
Jingle.hire_musician(nigel)

Jingle.play_solo(6)