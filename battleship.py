
class Player:
	def __init__(self):
		name = input("Enter player's name: ")
		self.name = name
		self.board = self.board_init()
		self.score = 30


	def board_init(self): 
		return { (chr(l),str(n)) : "   empty    " for  l in  range(ord("A"),ord("K")) for n in range(1,11) }



	def choosing_positions(self):
 		# choose AIRCRAFT position 
		aircraft_pos_l = input("choose a position for your AIRCRAFT size 5: Letter: ")
		aircraft_pos_n = int(input("choose a position for your AIRCRAFT size 5: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while aircraft_pos_n > 6 or aircraft_pos_n < 1:
				aircraft_pos_n = input("choose a position for your AIRCRAFT size 5: Number under 7: ")
			for i in range(0,5):
				self.board[(aircraft_pos_l,str(int(aircraft_pos_n)+i))] = "AIRCRAFT"
		else:
			while ord(aircraft_pos_l) > ord("F") or ord(aircraft_pos_l) < ord("A"):
				aircraft_pos_l = input("choose a position for your AIRCRAFT size 5: another letter: ")
			for i in range(0,5):
					self.board[(chr(ord(aircraft_pos_l) + i ),str(aircraft_pos_n))] = "  AIRCRAFT  "

		# choose BATTLESHIP1
		Battleship_pos_l = input("choose a position for your Battleship1 size 4: Letter: ")
		Battleship_pos_n = int(input("choose a position for your Battleship1 size 4: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while Battleship_pos_n > 7 or Battleship_pos_n < 1:
				Battleship_pos_n = input("choose a position for your Battleship1 size 4: Number under 7: ")
			for i in range(0,4):
				self.board[(Battleship_pos_l,str(int(Battleship_pos_n)+i))] = "Battleship1"
		else:
			while ord(Battleship_pos_l) > ord("G") or ord(Battleship_pos_l) < ord("A"):
				Battleship_pos_l = input("choose a position for your Battleship1 size 4: another letter: ")
			for i in range(0,4):
					self.board[(chr(ord(Battleship_pos_l) + i ),str(Battleship_pos_n))] = "Battleship1 "

		# choose BATTLESHIP2
		Battleship_pos_l = input("choose a position for your Battleship2 size 4: Letter: ")
		Battleship_pos_n = int(input("choose a position for your Battleship2 size 4: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while Battleship_pos_n > 7 or Battleship_pos_n < 1:
				Battleship_pos_n = input("choose a position for your Battleship2 size 4: Number under 7: ")
			for i in range(0,4):
				self.board[(Battleship_pos_l,str(int(Battleship_pos_n)+i))] = "Battleship2"
		else:
			while ord(Battleship_pos_l) > ord("G") or ord(Battleship_pos_l) < ord("A"):
				Battleship_pos_l = input("choose a position for your Battleship2 size 4: another letter: ")
			for i in range(0,4):
					self.board[(chr(ord(Battleship_pos_l) + i ),str(Battleship_pos_n))] = "Battleship2 "

		# choose Submarine1
		submarine_pos_l = input("choose a position for your submarine1 size 3: Letter: ")
		submarine_pos_n = int(input("choose a position for your submarine1 size 3: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while submarine_pos_n > 8 or submarine_pos_n < 1:
				submarine_pos_n = input("choose a position for your submarine1 size 3: Number under 8: ")
			for i in range(0,3):
				self.board[(submarine_pos_l,str(int(submarine_pos_n)+i))] = "submarine1"
		else:
			while ord(submarine_pos_l) > ord("H") or ord(submarine_pos_l) < ord("A"):
				submarine_pos_l = input("choose a position for your submarine1 size 3: another letter: ")
			for i in range(0,3):
					self.board[(chr(ord(submarine_pos_l) + i ),str(submarine_pos_n))] = " submarine1 " 

		# choose Submarine2
		submarine_pos_l = input("choose a position for your submarine2 size 3: Letter: ")
		submarine_pos_n = int(input("choose a position for your submarine2 size 3: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while submarine_pos_n > 8 or submarine_pos_n < 1:
				submarine_pos_n = input("choose a position for your submarine2 size 3: Number under 8: ")
			for i in range(0,3):
				self.board[(submarine_pos_l,str(int(submarine_pos_n)+i))] = "submarine2"
		else:
			while ord(submarine_pos_l) > ord("H") or ord(submarine_pos_l) < ord("A"):
				submarine_pos_l = input("choose a position for your submarine2 size 3: another letter: ")
			for i in range(0,3):
					self.board[(chr(ord(submarine_pos_l) + i ),str(submarine_pos_n))] = " submarine2 " 

		# choose Submarine3
		submarine_pos_l = input("choose a position for your submarine3 size 3: Letter: ")
		submarine_pos_n = int(input("choose a position for your submarine3 size 3: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while submarine_pos_n > 8 or submarine_pos_n < 1:
				submarine_pos_n = input("choose a position for your submarine3 size 3: Number under 8: ")
			for i in range(0,3):
				self.board[(submarine_pos_l,str(int(submarine_pos_n)+i))] = "submarine3"
		else:
			while ord(submarine_pos_l) > ord("H") or ord(submarine_pos_l) < ord("A"):
				submarine_pos_l = input("choose a position for your submarine3 size 3: another letter: ")
			for i in range(0,3):
					self.board[(chr(ord(submarine_pos_l) + i ),str(submarine_pos_n))] = " submarine3 " 

		# choose Patrol Boat 1
		patrol_boat_pos_l = input("choose a position for your patrol_boat1 size 3: Letter: ")
		patrol_boat_pos_n = int(input("choose a position for your patrol_boat1 size 2: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while patrol_boat_pos_n > 9 or patrol_boat_pos_n < 1:
				patrol_boat_pos_n = input("choose a position for your patrol_boat1 size 2: Number under 9: ")
			for i in range(0,2):
				self.board[(patrol_boat_pos_l,str(int(patrol_boat_pos_n)+i))] = "patrol_boat1"
		else:
			while ord(patrol_boat_pos_l) > ord("I") or ord(patrol_boat_pos_l) < ord("A"):
				patrol_boat_pos_l = input("choose a position for your patrol_boat1 size 2: another letter: ")
			for i in range(0,2):
					self.board[(chr(ord(patrol_boat_pos_l) + i ),str(patrol_boat_pos_n))] = "patrol_boat1" 

		# choose Patrol Boat 2
		patrol_boat_pos_l = input("choose a position for your patrol_boat2 size 3: Letter: ")
		patrol_boat_pos_n = int(input("choose a position for your patrol_boat2 size 2: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while patrol_boat_pos_n > 9 or patrol_boat_pos_n < 1:
				patrol_boat_pos_n = input("choose a position for your patrol_boat2 size 2: Number under 9: ")
			for i in range(0,2):
				self.board[(patrol_boat_pos_l,str(int(patrol_boat_pos_n)+i))] = "patrol_boat2"
		else:
			while ord(patrol_boat_pos_l) > ord("I") or ord(patrol_boat_pos_l) < ord("A"):
				patrol_boat_pos_l = input("choose a position for your patrol_boat2 size 2: another letter: ")
			for i in range(0,2):
					self.board[(chr(ord(patrol_boat_pos_l) + i ),str(patrol_boat_pos_n))] = "patrol_boat2" 

		# choose Patrol Boat 3
		patrol_boat_pos_l = input("choose a position for your patrol_boat3 size 3: Letter: ")
		patrol_boat_pos_n = int(input("choose a position for your patrol_boat3 size 2: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while patrol_boat_pos_n > 9 or patrol_boat_pos_n < 1:
				patrol_boat_pos_n = input("choose a position for your patrol_boat3 size 2: Number under 9: ")
			for i in range(0,2):
				self.board[(patrol_boat_pos_l,str(int(patrol_boat_pos_n)+i))] = "patrol_boat3"
		else:
			while ord(patrol_boat_pos_l) > ord("I") or ord(patrol_boat_pos_l) < ord("A"):
				patrol_boat_pos_l = input("choose a position for your patrol_boat3 size 2: another letter: ")
			for i in range(0,2):
					self.board[(chr(ord(patrol_boat_pos_l) + i ),str(patrol_boat_pos_n))] = "patrol_boat3" 

		# choose Patrol Boat 4
		patrol_boat_pos_l = input("choose a position for your patrol_boat4 size 3: Letter: ")
		patrol_boat_pos_n = int(input("choose a position for your patrol_boat4 size 2: Number: "))
		hor_ver = input("choose horizantal or vertical, type hor or ver: ")
		if hor_ver == "ver":
			while patrol_boat_pos_n > 9 or patrol_boat_pos_n < 1:
				patrol_boat_pos_n = input("choose a position for your patrol_boat4 size 2: Number under 9: ")
			for i in range(0,2):
				self.board[(patrol_boat_pos_l,str(int(patrol_boat_pos_n)+i))] = "patrol_boat4"
		else:
			while ord(patrol_boat_pos_l) > ord("I") or ord(patrol_boat_pos_l) < ord("A"):
				patrol_boat_pos_l = input("choose a position for your patrol_boat4 size 2: another letter: ")
			for i in range(0,2):
					self.board[(chr(ord(patrol_boat_pos_l) + i ),str(patrol_boat_pos_n))] = "patrol_boat4" 


	def boat_attacked(self):
		letter_to_hit = input("choose a position to shoot: Letter: ")
		number_to_hit = input("choose a position to shoot: Number: ")
		if self.board[(letter_to_hit,number_to_hit)] == "   empty    " or self.board[(letter_to_hit,number_to_hit)] == "   touched   ":
			print("A missed shot")
		else: 
			print("Nice shot you just hit your opponent: ", self.board[(letter_to_hit,number_to_hit)] )
			self.score -= 1 
			self.board[(letter_to_hit,number_to_hit)] == "   touched   "
		print("Your Oponent Score is :",self.score)





	def print_board(self):
		
		for n in range (1,11):
			for l in range (ord("A"),ord("K")):

				print(self.board[chr(l),str(n)],"  ", end="")
			print("")

class Game:
	def __init__(self):
		self.game = True 


	def play(self):
		player1 = Player()
		player1.choosing_positions()
		print (player1.name,"score is: ", player1.score," board: ")
		player1.print_board()
		player2 = Player()
		player2.choosing_positions()
		print (player2.name,"score is: ", player2.score," board: ")
		player2.print_board()
		while player1.score > 0 and player2.score > 0:
			print (player1.name,"  will  attack now... ")
			player2.boat_attacked()
			print (player2.name,"  will  attack now... ")
			player1.boat_attacked()
		if player1.score > player2.score:
			print("The winner is:  ",player1.name)
		else: 
			print("The winner is:  ",player2.name)



game = Game()
game.play()

