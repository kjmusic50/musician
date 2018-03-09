class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician): # The Musician class is the parent of the Guitarist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self): # A behavior of the Guitarist class
        # Details of what that behavior can consist of
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician): # The Musician class is the parent of the Drummer class
    def __init__(self):
        super(Drummer, self).__init__(["Thump","Bomp", "Tap"])
    
    def count(self): #Drummer count for band to play solos
        print "One, two, three, four!"
    
    def combust(self): # The drummers individual solo
        print("Tap!..", "Boom!......")
        
class Band(object):
    def __init__(self):
        self.members = {}
        
    def hire(self, job, players): #The hire function is a job of the Band
        self.members[job] = players
       
    def fire(self, job): #The fire function is a job of the Band
     if job in self.members:
      del self.members[job]
      
    def play_music(self, length): #This function is the count to start the band solos
        self.members['drummer'].count()
        for job, players in self.members.iteritems():
            players.solo(length)

##Musicians that are playing
if __name__ == '__main__':
    chris = Drummer()
    derek = Bassist()
    nigel = Guitarist()
    the_band = Band()
    the_band.hire('drummer', chris)
    the_band.hire('guitarist', nigel)
    the_band.hire('bassist', derek)
    the_band.play_music(4)
    nigel.solo(6)
    the_band.fire('guitarist')
    derek.solo(5)
    