import copy
import random

class room_generator:
    room = []
    def __init__(self, room):
        randomize = random.randint(5,10)
        room = [0] * randomize
        for i in range(randomize):
            room[i] = [0] * randomize
        print (room)

room_1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        ]
duplicado_r1 = copy.deepcopy(room_1)

class Player:
    def __init__(self):
        self.player_pos = [0, 0]

'''class Door:
    def __init__(self):
        self.door_pos = [random.randint(0, 5), random.randint(0, 5)]'''

def refresh_room():
    for i in range(len(room_1)): #cambiar por room después
        for j in range(len(room_1)):
            print (duplicado_r1[i][j], end = " ")
        print ()

def position(player, duplicado_r1):
    if duplicado_r1[player[0]][player[1]] != 0: 
        print("No puedes moverte a esta posición")
    else:
        duplicado_r1 = copy.deepcopy(room_1)
        duplicado_r1[player[0]][player[1]] = 'p'
    return player, duplicado_r1

def movement(player, duplicado_r1):
    inputmov = input("'w' arriba, 'a' izquierda, 's' abajo, 'd' derecha: ")
    if inputmov == "w":
        player[0] -=1
        player, duplicado_r1 = position(player, duplicado_r1)
        return player, duplicado_r1
    elif inputmov == "a":
        player[1] -=1
        player, duplicado_r1 = position(player, duplicado_r1)
        return player, duplicado_r1
    elif inputmov == "s":
        player[0] +=1
        player, duplicado_r1 = position(player, duplicado_r1)
        return player, duplicado_r1
    elif inputmov == "d":
        player[1] +=1
        player, duplicado_r1 = position(player, duplicado_r1)
        return player, duplicado_r1

#if player[0] == 2:
#            print("No puedes moverte a esta posición")
#        else:
#            player[0] +=1
#            player, duplicado_r1 = position(player, duplicado_r1)
#            return player, duplicado_r1

player = Player()
#door = Door()
duplicado_r1[player.player_pos[0]][player.player_pos[1]] = 'p'
#duplicado_r1[door.door_pos[0]][door.door_pos[1]] = 'D'
refresh_room()
while True:
    player.player_pos, duplicado_r1 = movement(player.player_pos, duplicado_r1)
    refresh_room()

