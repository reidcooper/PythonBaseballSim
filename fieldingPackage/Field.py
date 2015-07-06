import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from random import random
from teampackage import player
class Field(object):
    
 def __init__(self,currentField):
  CurrentField.CurrentField = currentField
  self.temp = []
  self.currentAmountOfOuts = 0

 def Field(cf):
  currentField = cf

 def newPlayerOnBases( n, p, numOfOuts,walkOrHomeRun):
  currentField.resetOuts()
  self.currentAmountOfOuts = numOfOuts
  if walkOrHomeRun == "walks":
    newPlayerOnBasesWalk(Player.p)


  elif walkOrHomeRun.equals("homerun"):
        newPlayerOnBasesHomerun(Player.p)


  else:
    currentField.putBallIntoRandomSquare()
    if not(checkIfBallIsCaught()):
     try:
      print "amount of bases to move " + n
      if n > 0:  
           if not(currentField.three.getPlayerOnBase() == False):
                  playerOnThrid()
        
        
           if not(currentField.two.getPlayerOnBase() == False):
                  currentField.two.movePlayerOneBase()
                  isPlayerOutOnBase(3, checkIfPlayerIsOnSameBaseAsBall(3))
                  if n >= 2:
                       playerOnThrid()
                
        
        
        if not (currentField.one.getPlayerOnBase() == False):
                       if n == 1:
                
                        currentField.one.movePlayerOneBase()
                    isPlayerOutOnBase(2, checkIfPlayerIsOnSameBaseAsBall(2))
                    
                    moveOneBase(p)
                    break
                
                       elif n ==2:
                
                         currentField.one.movePlayerOneBase()
                         isPlayerOutOnBase(2, checkIfPlayerIsOnSameBaseAsBall(2))
                         currentField.two.movePlayerOneBase()
                         isPlayerOutOnBase(3, checkIfPlayerIsOnSameBaseAsBall(3))
    
                         moveTwoBases(p)
                         break
                       elif n==3:
                
                
                        currentField.one.movePlayerOneBase()
                        isPlayerOutOnBase(2, checkIfPlayerIsOnSameBaseAsBall(2))
                        currentField.two.movePlayerOneBase()
                        isPlayerOutOnBase(3, checkIfPlayerIsOnSameBaseAsBall(3))
                        playerOnThrid()
    
                       movePlayerThreeBases(p)
                       break
                
                       elif n==4:
                
                        currentField.one.movePlayerOneBase()
                        isPlayerOutOnBase(2, checkIfPlayerIsOnSameBaseAsBall(2))
                        currentField.two.movePlayerOneBase();
                        isPlayerOutOnBase(3, checkIfPlayerIsOnSameBaseAsBall(3))
                        playerOnThrid()
                    
                        movePlayerFourBases(p)
                        break
                
     else:
            if n==1:
            
                moveOneBase(p)
                break
            
            elif n==2:
                moveTwoBases(p)
                break
            
            elif n==3:
                movePlayerThreeBases(p)
                break
            
            elif n==4:
                movePlayerFourBases(p)
                break
            
 except(Exception):
    print "three outs have happened! ending fielding"
    


else:
        currentField.addOneToOuts()
    


return currentField.getOuts()


def moveOneBase(Player) raise Exception:
    currentField.one.addPlayerToBase(Player.p)
    isPlayerOutOnBase(1, checkIfPlayerIsOnSameBaseAsBall(1))


def moveTwoBases(Player) raise Exception:
        currentField.one.addPlayerToBase(Player.p)
        b = isPlayerOutOnBase(1, checkIfPlayerIsOnSameBaseAsBall(1))
    
    if not b:
        currentField.one.movePlayerOneBase()
        isPlayerOutOnBase(2, checkIfPlayerIsOnSameBaseAsBall(2))
        


def movePlayerThreeBases(Player) raise Exception:
    currentField.one.addPlayerToBase(Player.p)
    boolean b = isPlayerOutOnBase(1, checkIfPlayerIsOnSameBaseAsBall(1))
    
    if not b:
        currentField.one.movePlayerOneBase()
        b = isPlayerOutOnBase(2, checkIfPlayerIsOnSameBaseAsBall(2))
        
    
    if not b:
        currentField.two.movePlayerOneBase();
        isPlayerOutOnBase(3, checkIfPlayerIsOnSameBaseAsBall(3));
    


 def movePlayerFourBases(Player):
    currentField.one.addPlayerToBase(Player.p)
    currentField.two.movePlayerOneBase()
        
    if(currentField.three.getPlayerOnBase() == False):
        
    

    else:
    currentField.three.movePlayerOneBase()
    currentField.addScore()
    System.out.println(currentField.home.getPlayerOnBase() + " has scored")
    


 def checkIfBallIsCaught():
    #gridFieldArray[0][0].setKey("LF", 15);
    #gridFieldArray[0][2].setKey("CF", 15);
    #gridFieldArray[0][4].setKey("RF", 15);
    self.temp = currentField.ball.getPostion() 
    print "Ball hit into field at " + " Ball pos " + temp[0] +" :" + temp[1]

    if (temp[0] == 0 and temp[1] == 0) or (temp[0] == 0 and temp[1] == 2) or (temp[0] == 0 and temp[1] == 4):
        print "...checking if ball was caught"
        return isBallCaught(temp[0], temp[1])
    
    else:
         return False


def isBallCaught( x, y):
    return currentField.wasBallCaught(x, y)


def checkIfPlayerIsOnSameBaseAsBall(int baseNum):
    #gridFieldArray[2][3].setKey("2B", 8);
    #gridFieldArray[3][0].setKey("3B", 8);
    #gridFieldArray[3][4].setKey("1B", 5);
    #gridFieldArray[3][2].setKey("C", 8);
 rand = (rand.randint()*100)
if rand > 60:
    return True

else:
    return False
    #!/*
 #def putBallIntoRandomInFieldSquare(self,basNum):
    
    #basePos = []
    
    #if basNum == 1:
        #basePos.append(3)
        #basePos.append(4)
        #break
    
    #elif basNum == 2:
        #basePos.append(2)
        #basePos.append(3)
        #break
    
    #elif basNum == 3:
        #basePos.append(3)
        #basePos[1] = 0
        #break;
    
    #elif basNum ==4:
        #basePos.append(3)
        #basePos.append(2)
        #break
    
    
    #temp = currentField.ball.getPostion()
    #print "Base num " + basePos[0] +" : "+ basePos[1] + " Ball pos " + temp[0] +" :" + temp[1]);
    #if temp[0] == basePos[0] and temp[1] == basePos[1] ):
        #print "Ball and player are on same base"
        #return isBallCaught(temp[0], temp[1])
   
    
    #return False;*/


def isPlayerOutOnBase(baseNum, b) raise Exception:
try:
    if currentAmountOfOuts + currentField.getOuts() >= 3:
        throw new Exception("3 outs have happened")
    

    if b:
     print "Player may get out on base"
     switch (baseNum){
        if baseNum == 1: 
                currentField.addOneToOuts()
                print "Player got out on 1st base!"
                currentField.one.removePlayerFromBase()
                return True
            
        elif baseNum == 2:
                currentField.addOneToOuts()
                print "Player got out on 2nd base!"
                currentField.two.removePlayerFromBase()
                return True
            
        elif baseNum ==3 : 
                currentField.addOneToOuts()
                print "Player got out on 3rd base!"
                currentField.three.removePlayerFromBase()
                return True

        
        elif baseNum == 4: 
                currentField.addOneToOuts()
                print  "Player got out on home plate!"
            return True
        
        else: 
            print "SOMETHING WENT WRONG"
        
    
    
    print "Player made it to base safely!" + b
    return False
    
        finally
        


def playerOnThrid(currentField):
    if currentField.three.getPlayerOnBase() == False:
    
    else:
        try:
             test = isPlayerOutOnBase(4, checkIfPlayerIsOnSameBaseAsBall(4))
            
            if not(test):
            currentField.three.movePlayerOneBase()
            currentField.addScore()
            print currentField.home.getPlayerOnBase() + " has scored"
                
            
            except(Exception):
                print "3 outs have happened on the field"
            
    


 def newPlayerOnBasesWalk(self, p){ 
  print("amount of bases to move is 1, walk ");
        if not (currentField.three.getPlayerOnBase() == False):
            if currentField.three.getPlayerOnBase() == False):
            
            else:
                currentField.three.movePlayerOneBase()
                currentField.addScore()
                print currentField.home.getPlayerOnBase() + " has scored"
                
            
        if not (currentField.two.getPlayerOnBase() == False):
            currentField.two.movePlayerOneBase()
        
        
        if not(currentField.one.getPlayerOnBase() == False):            
            currentField.one.movePlayerOneBase()
        
        
        else:
            currentField.one.addPlayerToBase(Player.p)
        


 def newPlayerOnBasesHomerun(self,p):
    print "Homerun!!"
    
    if not (currentField.three.getPlayerOnBase() == False):
        currentField.three.movePlayerOneBase()
        currentField.addScore()
        print currentField.home.getPlayerOnBase() + " has scored"
    
    
    if not (currentField.two.getPlayerOnBase() == False:
        currentField.two.movePlayerOneBase()
        currentField.three.movePlayerOneBase()
        currentField.addScore();
        print currentField.home.getPlayerOnBase() + " has scored"
    
    
    if not (currentField.one.getPlayerOnBase() == False):
        currentField.one.movePlayerOneBase()
        currentField.two.movePlayerOneBase()
        currentField.three.movePlayerOneBase()
        currentField.addScore();
        print currentField.home.getPlayerOnBase() + " has scored"
    
    
    currentField.one.addPlayerToBase(Player.p)
    currentField.one.movePlayerOneBase()
    currentField.two.movePlayerOneBase()
    currentField.three.movePlayerOneBase()
    currentField.addScore()
    print currentField.home.getPlayerOnBase() + " has scored"
    print "amount of outs " + currentField.getOuts()



