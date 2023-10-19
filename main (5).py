


'''implement a class called player that reperesent a cricket player. the player class should have a
method called play() which prints "the player is playing cricket. derive two classes, batsman and
bowler, from the player class.override yhr play() method in each derived class to print "the batsman
is batting" and "the bowlwer is bowling", respectively. write a program to creat objects of boyj the 
batsman and bowler classes and call the play() method for each object.'''


# define the base class player
class player:
  def play(self):
      print("the play is playing cricket.")

# define yhe derived clas batsman 
class batsman(player):
    def play(self):
        print("the batsman is batting.")
      
# define the derived class bowler
class bowler(player):
    def play(self):
        print("the bowler is bowling.")
      
# creat object of batsman and bowler classes
batsman = batsman()
bowler = bowler()

# call the play() method for each object
batsman.play()
bowler.play()

