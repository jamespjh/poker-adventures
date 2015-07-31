"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

from pylons import url
from datetime import datetime, timedelta

def card_url(card):
	suit_name_table = {
		'C' : 'clubs',
		'D' : 'diamonds',
		'H' : 'hearts',
		'S' : 'spades'
  	}
	  
	picture_name_table = {
		'A' : 'ace',
		'K' : 'king',
		'Q' : 'queen',
		'J' : 'jack'
	}
	
	suit = card[1]
	number = card[0]
	suit_name = suit_name_table[suit]
	card_name = picture_name_table.get(number, number)
	
	image_file = card_name+"_of_"+suit_name+'.png'
	return url('/cards/'+image_file)
	
def now():
	return datetime.now().strftime('%I:%M %p')
	
def after(minutes):
	now = datetime.now()
	then = now+timedelta(minutes=minutes)
	return then.strftime('%I:%M %p')