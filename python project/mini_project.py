import time
import random

def dice():
    global dicenum
    dicenum=random.randint(1,6)
    print(dicenum)

def congo():
    congodata=["congratulation","wonderful","yippeee","yay","fabulous"]
    congoname=random.choice(congodata)
    print(congoname,end=" ")
    
def sad():
    saddata=["oops","ouch","oh-dear","geez","nooo"]
    sadname=random.choice(saddata)
    print(sadname,end=" ")

ladder={2:23,6:45,20:59,52:72,57:96,71:92}

snake={43:17,50:5,56:8,73:15,84:58,87:49,98:40}


num=int(input("enter number of players"))
playername=[]
for i in range(num):
    b=input(f"enter player{i+1} name")
    playername.append(b)
    
playerdata=[]
for i in range(num):
    playerdata.append(0)
    
    
print(playername)


while(True):
    for i in playername:
        input(f"{i} please enter to roll the dice")
        print("dice rolling.....")
        time.sleep(3)
        dice()
        index=playername.index(i)
        data=playerdata[index]
        data=data+dicenum
        playerdata.remove(playerdata[index])
        playerdata.insert(index,data)
        
        
        if data in ladder:
            congo()
            print(f"{i} you got a ladder")
            data=ladder[data]
            playerdata.remove(playerdata[index])
            playerdata.insert(index,data)
        if data in snake:
            sad()
            print(f"{i} you got bitten by a snake")
            data=snake[data]
            playerdata.remove(playerdata[index])
            playerdata.insert(index,data)
        if(data>100):
            data=data-dicenum
            playerdata.remove(playerdata[index])
            playerdata.insert(index,data)
            print(f"{i} you are exceeding the limit this dice roll won't count")
        if(data==100):
            congo()
            print(f"{i} you won the game")
            break
            
            
        print(f"{i} your updated position is: {data}")
        print(playerdata)
    if(data==100):
        break





















        
