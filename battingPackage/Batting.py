# package battingPackage
from teamPackage import Pitcher
from teamPackage import Player
from random import randint

class Batting(object):

    chanceOfBall = 0
    chanceOfStrike = 0
    chanceOfHit = 0
    chanceOfFoul = 0
    z = 0
    avg_IPR = 52.7
    max_Z = 144.0
    FBPR = 0

    def __init__(self):
        pass

    def start_Batting(self, cb):
        self.balls = 0
        self.strikes = 0
        self.current_Batting = cb
        self.pitcher = cb.get_Pitcher()
        self.player = cb.get_Player()
        self.FBPR = generate_FBPR()

        self.chanceOfBall = (1 - self.pitcher.get_Zone_Per()) * (1 - self.player.get_to_Swing())
        self.chanceOfStrike = (self.pitcher.get_Zone_Per() * self.player.get_z_Swing() * (1 - self.player.get_z_Contact())) + (self.pitcher.get_Zone_Per() * (1 - self.player.get_z_Swing())) + (((1 - self.pitcher.get_Zone_Per()) * self.player.get_o_Swing() * (1 - self.player.get_o_Contact())))
        self.chanceOfFoul = ((1 - self.pitcher.get_Zon_ePer()) * self.player.get_o_Swing() * self.player.get_o_Contact() * self.FBPR) + (self.pitcher.get_Zone_Per() * self.player.get_z_Swing() * self.player.get_z_Contact() * self.FBPR)
        self.chanceOfHit = ((1 - self.pitcher.get_Zone_Per()) * self.player.get_o_Swing() * self.player.get_o_Contact() * (1 - self.FBPR)) + (self.pitcher.get_Zone_Per() * self.player.get_z_Swing() * self.player.get_z_Contact() * (1 - self.FBPR))

        self.chanceOfBall = self.chanceOfBall * 1000
        self.chanceOfStrike = self.chanceOfStrike * 1000
        self.chanceOfHit = self.chanceOfHit * 1000
        self.chanceOfFoul = self.chanceOfFoul * 1000

        self.a_Single = self.player.get_Chance_Single() * 100
        self.a_Double = self.player.get_Chance_Double() * 100
        self.a_Triple = self.player.get_Chance_Triple() * 100

        return atBat()

    def generate_FBPR(self):
        z = -66.7 + (self.generate_Pitch_Speed()/self.player.get_IPR())
        if z < self.avg_IPR:
            z = (z/self.avg_IPR) * 0.5
        else:
            z = 0.5 + (((self.z-self.avgIPR)/(self.maxZ - self.avg_IPR)) * 0.5);
        return z

    def generate_new_FBPR(self):

        self.FBPR = self.generate_FBPR()
        self.chanceOfFoul = ((1 - self.pitcher.get_Zon_ePer()) * self.player.get_o_Swing() * self.player.get_o_Contact() * self.FBPR) + (self.pitcher.get_Zone_Per() * self.player.get_z_Swing() * self.player.get_z_Contact() * self.FBPR)
        self.chanceOfHit = ((1 - self.pitcher.get_Zone_Per()) * self.player.get_o_Swing() * self.player.get_o_Contact() * (1 - self.FBPR)) + (self.pitcher.get_Zone_Per() * self.player.get_z_Swing() * self.player.get_z_Contact() * (1 - self.FBPR))

        self.chanceOfFoul = 1000 * self.chanceOfFoul
        self.chanceOfHit = 1000 * self.chanceOfHit

    def generate_Pitch_Speed(self):
        return self.pitcher.get_Pitch_Speed()

    def at_Bat(self):
        self.strikes = self.current_Batting.get_Strikes()
        while strikes <= 2 and balls <= 3:
            self.generate_New_FBPR()
            outcome = self.pitch()

        if outcome == 0:
            return hit()

        if self.current_Batting.get_Balls() == 4:
            current_Batting.setHomerunOrWalk("walk")
            return 1

        return 0

    def pitch(self):
        temp = randint(0, 999)
        #ball
        if temp < self.chanceOfBall:
            self.current_Batting.add_Ball()
            self.balls = self.current_Batting.get_Balls()
            print "Ball " + self.balls + " outcome " + temp
            return 1
        #strike
        elif temp < self.chanceOfBall + self.chanceOfStrike:
            self.current_Batting.add_Strike()
            self.strikes = self.current_Batting.get_Strikes()
            print "Strike " + self.strikes + " outcome " + temp
            return 1
        #foul
        elif temp < self.chanceOfBall + self.chanceOfStrike + self.chanceOfFoul:
            if self.current_Batting.get_Strikes() < 2:
                self.current_Batting.add_Strike()
                self.strikes = self.current_Batting.get_Strikes()
                print "Foul that was strike " + self.strikes + " outcome " + temp
                return 1
            else:
                current_Batting.add_Foul()
                print "foul " + self.currentBatting.get_Fouls() + " outcome " + temp
                return 1
        #hit
        else:
            print "Ball was hit by " + self.player + " outcome = " + temp
            return 0

    def hit(self):
        temp = randint(0, 99)
        if temp < self.a_Single:
            return 1
        elif temp < self.a_Single + self.a_Double:
            return 2
        elif temp < self.a_Single + self.a_Double + self.a_Triple:
            return 3
        else:
            self.current_Batting.setHomerunOrWalk("homerun")
            return 4

    def get_Batter(self):
        return self.current_Batting.get_Player()

    def toString(self):
        return "Chance of ball: " + self.chanceOfBall + "\n" + "Chance of hit: " + self.chanceOfHit + "\n" + "Chance of foul: " + self.chanceOfFoul + "\n" + "Chance of strike: " + self.chanceOfStrike + "\n"
