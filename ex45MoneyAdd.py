from random import randint

class MoneyAdd(object):

	def __init__(self):
		money = 0
		self.money = money

	def money_add(self, money):
		money_won = str(money)
		money_won_w = open('monies.txt', 'w')
		money_won_w.write(money_won)
		money_won_w.close()

def is_int(val):
	if val.isdigit():
		return True
	
	else:
		return False

def card_draw():
	cards ={
		'1' : "Ace of Diamonds",
		'2' : "Ace of Spades",
		'3' : "Ace of Hearts",
		'4' : "Ace of Clubs",
		'5' : "Two of Diamonds",
		'6' : "Two of Spades",
		'7' : "Two of Hearts",
		'8' : "Two of Clubs",
		'9' : "Three of Diamonds",
		'10' : "Three of Spades",
		'11' : "Three of Hearts",
		'12' : "Three of Clubs",
		'13' : "Four of Diamonds",
		'14' : "Four of Spades",
		'15' : "Four of Hearts",
		'16' : "Four of Clubs",
		'17' : "Five of Diamonds",
		'18' : "Five of Spades",
		'19' : "Five of Hearts",
		'20' : "Five of Clubs",
		'21' : "Six of Diamonds",
		'22' : "Six of Spades",
		'23' : "Six of Hearts",
		'24' : "Six of Clubs",
		'25' : "Seven of Diamonds",
		'26' : "Seven of Spades",
		'27' : "Seven of Hearts",
		'28' : "Seven of Clubs",
		'29' : "Eight of Diamonds",
		'30' : "Eight of Spades",
		'31' : "Eight of Hearts",
		'32' : "Eight of Spades",
		'33' : "Nine of Diamonds",
		'34' : "Nine of Spades",
		'35' : "Nine of Hearts",
		'36' : "Nine of Clubs",
		'37' : "Ten of Diamonds",
		'38' : "Ten of Spades",
		'39' : "Ten of Hearts",
		'40' : "Ten of Clubs",
		'41' : "Jack of Diamonds",
		'42' : "Jack of Spades",
		'43' : "Jack of Hearts",
		'44' : "Jack of Clubs",
		'45' : "Queen of Diamonds",
		'46' : "Queen of Spades",
		'47' : "Queen of Hearts",
		'48' : "Queen of Clubs",
		'49' : "King of Diamonds",
		'50' : "King of Spades",
		'51' : "King of Hearts",
		'52' : "King of Clubs"
	}

	card = randint(1, 13)

	if card == 1:
		card_face = cards.get(str(randint(1, 4)))
		card = [card_face, 11]
		return card

	elif card == 2:
		card_face = cards.get(str(randint(5, 8)))
		card = [card_face, 2]
		return card

	elif card == 3:
		card_face = cards.get(str(randint(9, 12)))
		card = [card_face, 3]
		return card

	elif card == 4:
		card_face = cards.get(str(randint(13, 16)))
		card = [card_face, 4]
		return card

	elif card == 5:
		card_face = cards.get(str(randint(17, 20)))
		card = [card_face, 5]
		return card

	elif card == 6:
		card_face = cards.get(str(randint(21, 24)))
		card = [card_face, 6]
		return card

	elif card == 7:
		card_face = cards.get(str(randint(25, 28)))
		card = [card_face, 7]
		return card

	elif card == 8:
		card_face = cards.get(str(randint(29, 32)))
		card = [card_face, 8]
		return card

	elif card == 9:
		card_face = cards.get(str(randint(33, 36)))
		card = [card_face, 9]
		return card

	else:
		card_face = cards.get(str(randint(37, 52)))
		card = [card_face, 10]
		return card

