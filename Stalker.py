
import sys, os
#import json
#from  Intel_Feeds import open_source_lists as feeds
from Database import database as dbupdate
from Stalk import stalk_prey as stalk
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

################################################################################################################################

def main():

	# Bring the Menu UP
	choise = menu()

	while choise != 4:
		if choise == 1:
			#print ("Update Database\n")
			cls()
			dbupdate.dbMenu()
		elif choise == 2:
			stalk.spMenu()	
		elif choise == 3:
			print ("This has not been implemented.")
			input()
		else:
			print ("Invalid number. Get some coffee and try again...")
			input()
			
		choise = menu()
	cls()
	print ("Stalk you later!! ( ° ͜ʖ °)  \n")

##############################################################################################################################

def cls(): 
	#try:
	#	os.system('cls') # For windows
	#except Exception as e: return
	try:
		os.system('clear') # For Linux
	except Exception: return

##############################################################################################################################

def menu():

	cls()
	print ("""
________________________________________________________________________________________________________________________

   d888888o.   8888888 8888888888          .8.          8 8888         8 8888     ,88' 8 8888888888   8 888888888o.
 .`8888:' `88.       8 8888               .888.         8 8888         8 8888    ,88'  8 8888         8 8888    `88.
 8.`8888.   Y8       8 8888              :88888.        8 8888         8 8888   ,88'   8 8888         8 8888     `88
 `8.`8888.           8 8888             . `88888.       8 8888         8 8888  ,88'    8 8888         8 8888     ,88
  `8.`8888.          8 8888            .8. `88888.      8 8888         8 8888 ,88'     8 888888888888 8 8888.   ,88'
   `8.`8888.         8 8888           .8`8. `88888.     8 8888         8 8888 88'      8 8888         8 888888888P'
    `8.`8888.        8 8888          .8' `8. `88888.    8 8888         8 888888<       8 8888         8 8888`8b
8b   `8.`8888.       8 8888         .8'   `8. `88888.   8 8888         8 8888 `Y8.     8 8888         8 8888 `8b.
`8b.  ;8.`8888       8 8888        .888888888. `88888.  8 8888         8 8888   `Y8.   8 8888         8 8888   `8b.
 `Y8888P ,88P'       8 8888       .8'       `8. `88888. 8 888888888888 8 8888     `Y8. 8 888888888888 8 8888     `88.
________________________________________________________________________________________________________________________

[1] Database.
[2] Stalk. 
[3] Modules.

[4] Quit

""")
	try:
		ans = input('Lets start stalking, Enter your choise [1-4]: ')
		return (int(ans))
	except Exception as e:
		print ("Was that even a number!? \n", e)
		pass



if __name__ == '__main__':
	main()
	#print (Updatedb.basic_intel())
	#masterfeed = feed.fetch_feeds()
	#for key, value in feeds.fetch_feeds().items():
	#	print ('IP = ', key)
	#	print ('Intel = ', value)
	#print (feeds.fetch_feeds())

