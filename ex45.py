from sys import exit
from random import randint
from ex45MoneyAdd import MoneyAdd
from ex45MoneyAdd import is_int
from ex45MoneyAdd import card_draw

linebreak = '\n==============================================\n'

class Pick(object):
	
	def __init__(self):
		self.money = money

	def enter(self, money):
		
		if 0 < money < 100:
			print(linebreak,"\bHow much would you like to bet?")
			bet = input("> $")
			is_bet_var = is_int(bet) 
				
			if is_bet_var == True:
				bet = int(bet)

				if bet <= money:
					print("Choose either 1 or 2.")
					choice = input("> ")
					is_choice_var = is_int(choice)

					if is_choice_var == True:
						choice = int(choice)
						randnum = randint(1, 2)
						print(f"You chose number {choice} and the number is: ", randnum)

						if choice == randnum:
							money_won = money + bet
							print(f"You won ${bet}, your total amount of money is ${money_won}.")
							winnings = MoneyAdd()
							winnings.money_add(money_won)

							while True:
								next_room = input("Would you like to try again?[y/n/exit game]> ")

								if next_room == 'y':
									new_room = Pick()
									new_room.enter(money_won)

								elif next_room == 'n':
									new_room = RoomChoice()
									new_room.room_choice(money_won)

								elif next_room == 'exit game':
									exit(0)

								else:
									print("Invalid Selection")

						else:
							money_won = money - bet
							print(f"You lost ${bet}, your total amount of money is ${money_won}.")
							winnings = MoneyAdd()
							winnings.money_add(money_won)
							
							while True:
								next_room = input("Would you like to try again?[y/n/exit game]> ")
								
								if next_room == 'y':
									new_room = Pick()
									new_room.enter(money_won)

								elif next_room == 'n':
									new_room = RoomChoice()
									new_room.room_choice(money_won)

								elif next_room == 'exit game':
									exit(0)

								else:
									print("Invalid Selection")

					else:
						print("Try again.")
						new_room = Pick()
						new_room.enter(money)

				else:
					print("Try again.")
					new_room = Pick()
					new_room.enter(money)

			else:
				print("Try again.")
				new_room = Pick()
				new_room.enter(money)
		else:
			print(linebreak,f"\bYou have ${money}, the room minimum is $1 and the max is $100")
			print("Exiting Room.", linebreak)
			new_room = RoomChoice()
			new_room.room_choice(money)

class Black(object):
	
	def __init__(self):
		self.money = money

	def enter(self, money):
		
		if 100 <= money < 500:
			print(linebreak,"\bHow much would you like to bet?")
			bet = input("> $")
			is_bet_var = is_int(bet) 
			
			if is_bet_var == True:
				bet = int(bet)

				if bet <= money:
					card1 = card_draw()
					card2 = card_draw()
					card3 = card_draw()
					card4 = card_draw()
					card1_value = int(card1.pop())
					card1_face = card1.pop()
					card2_value = int(card2.pop())
					card2_face = card2.pop()
					card3_value = int(card3.pop())
					card3_face = card3.pop()
					card4_value = int(card4.pop())
					card4_face = card4.pop()
					print(f"\bYou were dealt {card1_face} and {card2_face} equaling {card1_value + card2_value}")

					if card1_value + card2_value == 21:
						money_won = money + bet * 1.5
						print(f"You won ${bet * 1.5}, your total amount of money is ${money_won}.")
						winnings = MoneyAdd()
						winnings.money_add(money_won)

						while True:							
							next_room = input("Would you like to try again?[y/n/exit game]> ")

							if next_room == 'y':
								new_room = Black()
								new_room.enter(money_won)

							elif next_room == 'n':
								new_room = RoomChoice()
								new_room.room_choice(money_won)

							elif next_room == 'exit game':
								exit(0)

							else:
								print("Invalid Selection")

					else:
						choice = input(f"You can see that the dealer has {card4_face} equaling {card4_value} what would you like to do?[hit/pass]> ")
#ifhit
						if choice == 'hit':
							card5 = card_draw()
							card5_value = int(card5.pop())
							card5_face = card5.pop()
							print(f"\bYou were dealt {card5_face} making your hand equal {card1_value + card2_value + card5_value}")

							if card1_value + card2_value + card5_value == 21:
								money_won = money + bet * 1.5
								print(f"You won ${bet * 1.5}, your total amount of money is ${money_won}.")
								winnings = MoneyAdd()
								winnings.money_add(money_won)
								
								while True:
									next_room = input("Would you like to try again?[y/n/exit game]> ")
									
									if next_room == 'y':
										new_room = Black()
										new_room.enter(money_won)

									elif next_room == 'n':
										new_room = RoomChoice()
										new_room.room_choice(money_won)

									elif next_room == 'exit game':
										exit(0)

									else:
										print("Invalid Selection")
#ifhitvalue>21
							elif card1_value + card2_value + card5_value > 21:

								while card1_value + card2_value + card5_value > 21:

									if card1_value == 11:
										choice_ace = input(f"Would you like to make the {card2_face} a 1?[y/n]> ")

										if choice_ace == 'y':
											card1_value = 1
											print(f"Your hand now equals {card1_value + card2_value + card5_value}")
											continue

										elif choice_ace == 'n':
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
							
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")
										else:
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
							
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")


									elif card2_value == 11:
										choice_ace = input(f"Would you like to make the {card2_face} a 1?[y/n]> ")

										if choice_ace == 'y':
											card2_value = 1
											print(f"Your hand now equals {card1_value + card2_value + card5_value}")
											continue

										elif choice_ace == 'n':
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
							
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")

										else:
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
							
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")

									elif card5_value == 11:
										choice_ace = input(f"Would you like to make the {card5_face} a 1?[y/n]> ")

										if choice_ace == 'y':
											card5_value = 1
											print(f"Your hand now equals {card1_value + card2_value + card5_value}")
											continue

										elif choice_ace == 'n':
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
							
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")

									else:
										money_won = money - bet
										print(f"You lost ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)
							
										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
								
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")

								if card3_value + card4_value == 21:
									print(f"The dealer had {card3_face} & {card4_face} equaling {card3_value + card4_value}.")

									money_won = money - bet
									print(f"You lost ${bet}, your total amount of money is ${money_won}.")
									winnings = MoneyAdd()
									winnings.money_add(money_won)
							
									while True:
										next_room = input("Would you like to try again?[y/n/exit game]> ")
									
										if next_room == 'y':
											new_room = Black()
											new_room.enter(money_won)

										elif next_room == 'n':
											new_room = RoomChoice()
											new_room.room_choice(money_won)

										elif next_room == 'exit game':
											exit(0)

										else:
											print("Invalid Selection")



								elif card3_value + card4_value <= card1_value + card2_value + card5_value:
										card6 = card_draw()
										card6_value = int(card6.pop())
										card6_face = card6.pop()
										print(f"The dealer had {card3_face} & {card4_face}, they drew {card6_face} making their hand equal {card3_value + card4_value + card6_value}.")

										if card3_value + card4_value + card6_value == 21:
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
								
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")


										elif card3_value + card4_value + card6_value > 21:

											while card3_value + card4_value + card6_value > 21:

												if card3_value == 11:
													card3_value = 1
													print(f"The dealer changed {card3_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}.")
													continue

												elif card4_value == 11:
													card4_value = 1
													print(f"The dealer changed {card3_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}.")
													continue

												elif card6_value == 11:
													card6_value = 1
													print(f"The dealer changed {card3_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}.")
													continue

												else:
													money_won = money + bet
													print("Dealer broke.")
													print(f"You won ${bet}, your total amount of money is ${money_won}.")
													winnings = MoneyAdd()
													winnings.money_add(money_won)
								
													while True:
														next_room = input("Would you like to try again?[y/n/exit game]> ")
									
														if next_room == 'y':
															new_room = Black()
															new_room.enter(money_won)

														elif next_room == 'n':
															new_room = RoomChoice()
															new_room.room_choice(money_won)

														elif next_room == 'exit game':
															exit(0)

														else:
															print("Invalid Selection")

											if card3_value + card4_value + card6_value <= card1_value + card2_value + card5_value:
												money_won = money + bet
												print(f"You won ${bet}, your total amount of money is ${money_won}.")
												winnings = MoneyAdd()
												winnings.money_add(money_won)
								
												while True:
													next_room = input("Would you like to try again?[y/n/exit game]> ")
									
													if next_room == 'y':
														new_room = Black()
														new_room.enter(money_won)

													elif next_room == 'n':
														new_room = RoomChoice()
														new_room.room_choice(money_won)

													elif next_room == 'exit game':
														exit(0)

													else:
														print("Invalid Selection")

											elif card3_value + card4_value + card6_value > card1_value + card2_value + card5_value:
												money_won = money - bet
												print(f"You lost ${bet}, your total amount of money is ${money_won}.")
												winnings = MoneyAdd()
												winnings.money_add(money_won)
								
												while True:
													next_room = input("Would you like to try again?[y/n/exit game]> ")
								
													if next_room == 'y':
														new_room = Black()
														new_room.enter(money_won)

													elif next_room == 'n':
														new_room = RoomChoice()
														new_room.room_choice(money_won)

													elif next_room == 'exit game':
														exit(0)

													else:
														print("Invalid Selection")

										elif card3_value + card5_value + card6_value > card1_value + card2_value + card5_value:
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
								
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")

								elif card3_value + card4_value > card1_value + card2_value + card5_value:
										money_won = money - bet
										print(f"You lost ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)
								
										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
								
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")
#ifhitvalue<21
							elif card1_value + card2_value + card5_value < 21:

								if card3_value + card4_value == 21:
									print(f"The dealer had {card3_face} & {card4_face} equaling {card3_value + card4_value}.")

									money_won = money - bet
									print(f"You lost ${bet}, your total amount of money is ${money_won}.")
									winnings = MoneyAdd()
									winnings.money_add(money_won)
							
									while True:
										next_room = input("Would you like to try again?[y/n/exit game]> ")
									
										if next_room == 'y':
											new_room = Black()
											new_room.enter(money_won)

										elif next_room == 'n':
											new_room = RoomChoice()
											new_room.room_choice(money_won)

										elif next_room == 'exit game':
											exit(0)

										else:
											print("Invalid Selection")

								elif card3_value + card4_value <= card1_value + card2_value + card5_value:
									card6 = card_draw()
									card6_value = int(card6.pop())
									card6_face = card6.pop()
									print(f"The dealer had {card3_face} & {card4_face}, they drew {card6_face} making their hand equal {card3_value + card4_value + card6_value}.")

									if card3_value + card4_value + card6_value == 21:
										money_won = money - bet
										print(f"You lost ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)
								
										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
								
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")


									elif card3_value + card4_value + card6_value > 21:

										while card3_value + card4_value + card6_value > 21:

											if card3_value == 11:
												card3_value = 1
												print(f"The dealer changed {card3_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}")
												continue

											elif card4_value == 11:
												card4_value = 1
												print(f"The dealer changed {card4_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}")
												continue

											elif card6_value == 11:
												card6_value = 1
												print(f"The dealer changed {card6_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}")
												continue

											else:
												money_won = money + bet
												print("Dealer broke.")
												print(f"You won ${bet}, your total amount of money is ${money_won}.")
												winnings = MoneyAdd()
												winnings.money_add(money_won)
								
												while True:
													next_room = input("Would you like to try again?[y/n/exit game]> ")
									
													if next_room == 'y':
														new_room = Black()
														new_room.enter(money_won)

													elif next_room == 'n':
														new_room = RoomChoice()
														new_room.room_choice(money_won)

													elif next_room == 'exit game':
														exit(0)

													else:
														print("Invalid Selection")

										if card3_value + card4_value + card6_value <= card1_value + card2_value + card5_value:
											money_won = money + bet
											print(f"You won ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
								
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
									
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")

										elif card3_value + card4_value + card6_value > card1_value + card2_value + card5_value:
											money_won = money - bet
											print(f"You lost ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
								
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
								
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")

									elif card3_value + card4_value + card6_value <= card1_value + card2_value + card5_value:
										money_won = money + bet
										print(f"You won ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)
								
										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
									
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")

									elif card3_value + card4_value + card6_value > card1_value + card2_value + card5_value:
										money_won = money - bet
										print(f"You lost ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)
								
										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
								
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")

								else:
									print(f"The dealer had {card3_face} & {card4_face} equaling {card3_value + card4_value}.")

									if card3_value + card4_value != 22: 
										money_won = money - bet
										print(f"You lost ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)

										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
								
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")
									else:
										print("This is really lucky... I have homework to do and don't feel like coding this in so...")
										money_won = money - bet
										print(f"You lost ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)

										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
								
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")



						elif choice == 'pass':
							if card3_value + card4_value == 21:
								print(f"The dealer had {card3_face} & {card4_face} equaling {card3_value + card4_value}.")

								money_won = money - bet
								print(f"You lost ${bet}, your total amount of money is ${money_won}.")
								winnings = MoneyAdd()
								winnings.money_add(money_won)
							
								while True:
									next_room = input("Would you like to try again?[y/n/exit game]> ")
								
									if next_room == 'y':
										new_room = Black()
										new_room.enter(money_won)

									elif next_room == 'n':
										new_room = RoomChoice()
										new_room.room_choice(money_won)

									elif next_room == 'exit game':
										exit(0)

									else:
										print("Invalid Selection")

							elif card3_value + card4_value <= card1_value + card2_value:
								card6 = card_draw()
								card6_value = int(card6.pop())
								card6_face = card6.pop()
								print(f"The dealer had {card3_face} & {card4_face}, they drew {card6_face} making their hand equal {card3_value + card4_value + card6_value}.")

								if card3_value + card4_value + card6_value == 21:
									money_won = money - bet
									print(f"You lost ${bet}, your total amount of money is ${money_won}.")
									winnings = MoneyAdd()
									winnings.money_add(money_won)
							
									while True:
										next_room = input("Would you like to try again?[y/n/exit game]> ")
								
										if next_room == 'y':
											new_room = Black()
											new_room.enter(money_won)

										elif next_room == 'n':
											new_room = RoomChoice()
											new_room.room_choice(money_won)

										elif next_room == 'exit game':
											exit(0)

										else:
											print("Invalid Selection")

								elif card3_value + card4_value + card6_value > 21:

									while card3_value + card4_value + card6_value > 21:

										if card3_value == 11:
											card3_value = 1
											print(f"The dealer changed {card3_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}.")
											continue

										elif card4_value == 11:
											card4_value = 1
											print(f"The dealer changed {card4_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}.")
											continue

										elif card6_value == 11:
											card6_value = 1
											print(f"The dealer changed {card6_face} to a 1 making their hand equal {card3_value + card4_value + card6_value}.")
											continue

										else:
											money_won = money + bet
											print(f"You won ${bet}, your total amount of money is ${money_won}.")
											winnings = MoneyAdd()
											winnings.money_add(money_won)
								
											while True:
												next_room = input("Would you like to try again?[y/n/exit game]> ")
									
												if next_room == 'y':
													new_room = Black()
													new_room.enter(money_won)

												elif next_room == 'n':
													new_room = RoomChoice()
													new_room.room_choice(money_won)

												elif next_room == 'exit game':
													exit(0)

												else:
													print("Invalid Selection")

									if card3_value + card4_value + card6_value <= card1_value + card2_value:
										money_won = money + bet
										print(f"You won ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)
								
										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
									
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection")

									elif card3_value + card4_value + card6_value > card1_value + card2_value:
										money_won = money - bet
										print(f"You lost ${bet}, your total amount of money is ${money_won}.")
										winnings = MoneyAdd()
										winnings.money_add(money_won)
								
										while True:
											next_room = input("Would you like to try again?[y/n/exit game]> ")
							
											if next_room == 'y':
												new_room = Black()
												new_room.enter(money_won)

											elif next_room == 'n':
												new_room = RoomChoice()
												new_room.room_choice(money_won)

											elif next_room == 'exit game':
												exit(0)

											else:
												print("Invalid Selection") 

								elif card3_value + card4_value + card6_value <= card1_value + card2_value:
									money_won = money + bet
									print(f"You won ${bet}, your total amount of money is ${money_won}.")
									winnings = MoneyAdd()
									winnings.money_add(money_won)
								
									while True:
										next_room = input("Would you like to try again?[y/n/exit game]> ")
									
										if next_room == 'y':
											new_room = Black()
											new_room.enter(money_won)

										elif next_room == 'n':
											new_room = RoomChoice()
											new_room.room_choice(money_won)

										elif next_room == 'exit game':
											exit(0)

										else:
											print("Invalid Selection")

								elif card3_value + card4_value + card6_value > card1_value + card2_value:
									money_won = money - bet
									print(f"You lost ${bet}, your total amount of money is ${money_won}.")
									winnings = MoneyAdd()
									winnings.money_add(money_won)
							
									while True:
										next_room = input("Would you like to try again?[y/n/exit game]> ")
								
										if next_room == 'y':
											new_room = Black()
											new_room.enter(money_won)

										elif next_room == 'n':
											new_room = RoomChoice()
											new_room.room_choice(money_won)

										elif next_room == 'exit game':
											exit(0)

										else:
											print("Invalid Selection")

							elif card3_value + card4_value > card1_value + card2_value:
								print(f"The dealer had {card3_face} & {card4_face} equaling {card3_value + card4_value}.")
								money_won = money - bet
								print(f"You lost ${bet}, your total amount of money is ${money_won}.")
								winnings = MoneyAdd()
								winnings.money_add(money_won)
							
								while True:
									next_room = input("Would you like to try again?[y/n/exit game]> ")
								
									if next_room == 'y':
										new_room = Black()
										new_room.enter(money_won)

									elif next_room == 'n':
										new_room = RoomChoice()
										new_room.room_choice(money_won)

									elif next_room == 'exit game':
										exit(0)

									else:
										print("Invalid Selection")


						else:
							money_won = money - bet
							print(f"You lost ${bet}, your total amount of money is ${money_won}.")
							winnings = MoneyAdd()
							winnings.money_add(money_won)
							
							while True:
								next_room = input("Would you like to try again?[y/n/exit game]> ")
							
								if next_room == 'y':
									new_room = Black()
									new_room.enter(money_won)

								elif next_room == 'n':
									new_room = RoomChoice()
									new_room.room_choice(money_won)

								elif next_room == 'exit game':
									exit(0)

								else:
									print("Invalid Selection")

				else:
					print("Try again.")
					new_room = Black()
					new_room.enter(money)

			else:
				print("Try again.")
				new_room = Black()
				new_room.enter(money)

		else:
			print(linebreak,f"\bYou have ${money}, the room minimum is $100 and the max is $500")
			print("Exiting Room.", linebreak)
			new_room = RoomChoice()
			new_room.room_choice(money)







class RoomChoice(object):

	def __init__(self):
		self.money = money

	def room_choice(self, money):
		if 0 < money < 100:
			print("Your only choice is pick a number game.")
			new_room = Pick()
			new_room.enter(money)

		elif 100 <= money < 500:
			print("Your only choice is blackjack.")
			new_room = Black()
			new_room.enter(money)

		elif 500 <= money:
			print("You win!")
			exit(0)

		else:
			print("You broke. K bai.")
			exit(0)


money_start = '20'
money_file_w = open('monies.txt', 'w')
money_file_w.write(money_start)
money_file_w.close()

money_file_r = open('monies.txt')
money = money_file_r.read()
money_file_r.close()
money = int(money)

player = RoomChoice()
player.room_choice(money)



