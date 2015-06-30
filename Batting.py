

import random()
class Batting(object):
    chance_Of_Ball = 0
    chance_Of_Strike = 0
    chance_Of_Hit = 0
    chance_Of_Foul = 0
    z = 0
    avg_IPR = 52.7
    max_Z = 144.0
    
    def__init__(self,current_Batting,player,pitcher,outcome,strikes,balls,a_Single,a_Double,a_Triple):
        self.current_Batting = current_Batting
        self.player = player
        self.pitcher = pitcher
        self.outcome = outcome
        self.strikes = strikes
        self.balls = balls
        self.a_Single= a_Single
        self.a_Double= a_Double
        self.a_Triple = a_Triple

    def start_Batting(self,cb):
        cb = Current_Batting()
        self.balls = 0
        self.strikes = 0
        self.current_Batting = cb
        pitcher = cb.get_Pitcher()
        player = cb.get_Player()

        FBPR = generate_FBPR()
        chance-Of-Ball = (1 - pitcher.get_Zone_Per()) * (1 - player.get_to_Swing())
        chance-Of-Strike = (pitcher.get_Zone_Per() * player.get_z_Swing() * (1-player.get_z_Contact())) + (pitcher.get_Zone_Per() * (1-player.get_z_Swing())) + (((1-pitcher.get_Zone_Per()) * player.get_O_Swing() * (1-player.get_o_Contact())))
        chance-Of-Foul = ((1-pitcher.get_Zon_ePer()) * player.get_o_Swing() * player.get_o_Contact() * FBPR) + (pitcher.get_Zone_Per() * player.get_z_Swing() * player.get_z_Contact() * FBPR)
        chance_Of_Hit = ((1-pitcher.get_Zone_Per()) * player.get_o_Swing() * player.get_o_Contact() * (1 - FBPR)) + (pitcher.get_Zone_Per() * player.get_z_Swing() * player.get_z_Contact() * (1-FBPR))

        chance-Of-Ball = chance_Of_Ball * 1000
	chance-Of-Strike =chance_Of_Strike * 1000
	chance-Of-Hit = chance_Of_Hit * 1000
	chance-Of-Foul = chance_Of_Foul * 1000;
	
	a_Single = player.get_Chance_Single() * 100
	a_Double = player.get_Chance_Double() * 100
	a_Triple = player.get_Chance_Triple() * 100
	
	return atBat()

    def generate_FBPR():
        
        z = -66.7f +(generate_Pitch_Speed()/player.get_IPR())
	
	if z < avg_IPR:
		z = (z/avg_IPR)* 1/2
	
	else:
		z = 1/2f + (((z-avgIPR)/(maxZ - avg_IPR))*(.5));
	
	
	return z
    
    def generate_new_FBPR():

        FBPR = generate_FBPR()
        chance-Of-Foul = ((1-pitcher.get_Zon_ePer()) * player.get_o_Swing() * player.get_o_Contact() * FBPR) + (pitcher.get_Zone_Per() * player.get_z_Swing() * player.get_z_Contact() * FBPR)
        chance-Of-Hit = ((1-pitcher.get_Zone_Per()) * player.get_o_Swing() * player.get_o_Contact() * (1 - FBPR)) + (pitcher.get_Zone_Per() * player.get_z_Swing() * player.get_z_Contact() * (1-FBPR))
	
	chance-Of-Foul = 1000 * chance-Of-Foul
	chance-Of-Hit = 1000 * chance-Of-Hit

    def generate_Pitch_Speed():
	
        return pitcher.get_Pitch_Speed()


    def at_Bat():
	strikes = current_Batting.get_Strikes()
	while strikes <= 2 and balls <= 3:
		generate_New_FBPR()
		outcome = pitch()
		
		if outcome == 0
			return hit()
		
	
	if current_Batting.get_Balls() == 4
		return 1
	
	return 0
 

    def pitch():
	 temp = (Math.random() * 1000)
	//ball
	if temp < chance_Of_Ball:
		current_Batting.addBall()
		balls = currentBatting.getBalls()
		System.out.println("Ball " + balls + " outcome " + temp)
		return 1
	
	//strike
	elif temp < chance_Of_Ball + chance_Of_Strike:
		current_Batting.add_Strike()
		strikes = current_Batting.get_Strikes()
		print "Strike " + currentBatting.getStrikes() + " outcome " + temp
		return 1
	}
	//foul
	elif temp < chanceOfBall + chanceOfStrike + chanceOfFoul:
		if current_Batting.get_Strikes() < 2:
			current_Batting.add_Strike()
			strikes = current_Batting.get_Strikes()
			print "Foul that was strike " + currentBatting.getStrikes() + " outcome " + temp
			return 1
		
		else:
			current_Batting.add_Foul()
			print "foul " + currentBatting.getFouls() + " outcome " + temp
			return 1
		
	
	//hit
	else:
		print "Ball was hit by " + player + " outcome = " + temp
		return 0
	


    def hit():
         temp = (Math.random() * 100)
	if temp < a_Single:
		return 1
	
	elif temp < a_Single + a_Double:
        	return 2
	
	elif temp < a_Single + a_Double + a_Triple:
		return 3
	
	else:
		return 4
	


    def get_Batter():
	return current_Batting.get_Player()


    def toString():
	return "Chance of ball: " + chance_Of_Ball + "\n" + "Chance of hit: " + chance_Of_Hit + "\n" +
			"Chance of foul: " + chance_Of_Foul + "\n" + "Chance of strike: " + chance_Of_Strike + "\n"

       

