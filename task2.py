from enum import Enum, auto



class States(Enum):
    NEUTRAL = auto() #natural state
    ATTACK = auto()  #state of attack
    DEATH = auto()   #death

#oops
class GameObject:
    def __init__(self):
        self.__state = States.NEUTRAL #normal state

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


class Entity(GameObject):
    def get_health(self):
        return self.__health

    def set_health(self, health):  
        h = health
        if h<0:  #when health is smaller than 0 it becomes 0 as health smaller than 0 not possible
            h = 0
        self.__health = h

player = Entity()
player.set_state(States.ATTACK) #player in attack mode

enemy = Entity()
enemy.set_health(35)
enemy.set_state(States.NEUTRAL) #enemy initially in neutral mode

i=0 #variable to count iteration .....

print('Iteration Number: '+str(i),end='\n')
print('Input: -', end=' | ')
print('Output: 000', end=' | ')
print('Present State: 111')

def binary_for_player(num):     # function specially made to give output in desired format
    if num == 0:
        return '00'
    elif num==1:
        return '01'
    else:
        return bin(num).replace('0b','') #when we use bin() it gibes 0b at front so we must remove it

def binary_for_enymy(num):
    if 0<=num<=1:
        return bin(num).replace('0b','00')
    elif 1<num<=3:
        return bin(num).replace('0b','0')
    elif 3<num:
        return bin(num).replace('0b','')


state=0 # enemy alive
while enemy.get_health()>0:
    i = i+1 #iteratoin num increases by 1
    
    flag= enemy.get_health() #has a puopose
    print('Iteration Number: '+str(i))
    
    T = input("B for 'Barbarian'\nG for 'Giant'\nP for 'P.E.K.K.A'\nEnter the player; ")
    if T=='B':
        player.set_health(5)
    if T=='G':
        player.set_health(10)
    if T=='P':
        player.set_health(20)
       
    if player.get_state() == States.ATTACK:
        enemy.set_health(enemy.get_health()-player.get_health())
        enemy.set_state(States.ATTACK) # if player attacking enemy also attacks
    if enemy.get_state() == States.ATTACK:
        player.set_health(player.get_health()-flag)
    if enemy.get_health() <= 0: 
        enemy.set_state(States.DEATH)
        state = 1   #enemy died


    print('Input: ',T, end='|')
    print('Output: ', state, end='')
    print((binary_for_player(player.get_health()//5)) , end='|')
    print('Present State: ', (binary_for_enymy(enemy.get_health()//5)), end='\n\n')
    if enemy.get_health() == 0:
        break
