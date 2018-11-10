class Enemy(object):

    def move_left(self):
        print('Moving left...')

    def move_right(self):
        print('Moving right...')

class Ninja(Enemy):

    def karate_chop(self):
        print('Karate chop!')

class Zombie(Enemy):

    def bite(self):
        print('I am biting you!')

enemy = Enemy()
enemy.move_left()

# Ninja also includes all functions from parent class (Enemy)
ninja = Ninja()
ninja.move_left()
ninja.karate_chop()

# Zombie is called (the child class), inherits from Enemy (parent class)
zombie = Zombie()
zombie.move_right()
zombie.bite()

'''- when you have a child class that gets basic behavior from parent class
- used to avoid rewriting common functions in every class that share 
similar behavior

In this example, we have two types on enemies (Ninja and Zombie). 
Since all enemies share certain behaviors (movingleft and right) 
we can write all of the common functionality inside 
one parent class instead of every enemy class. '''

