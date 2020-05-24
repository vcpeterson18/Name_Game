

from gtts import gTTS
import os
LANGUAGE = 'en'

VOWELS = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
GAME_STARTING_VOWELS = ["M","m","F","f","B","b"]
FIRST_TWO_H = ["ch","Ch","th","Th"]


def main():
	print("Let's play the name game!")
	print("\n")
	play_again = ""
	# get name from the user
	while play_again == "":
		your_name = input("What's your name? ")
		name_game_full = play_name_game(your_name)
		print(name_game_full)
		play_again = input("\n" + "Hit enter to play again or" + "\n" + "type 'quit' to exit: ")
		while play_again != 'quit' and play_again != "":
			print("I don't understand, do you want to play again or quit?")
			play_again = input("\n" + "Hit enter to play again or" + "\n" + "type 'quit' to exit:")

	
def play_name_game(name):
	
	name_base = name[1 : : ]
	first_char = name[0]
	# print(first_char)
	name_game_full = ""
	# print("name"+"!")
	name_game_full += name.capitalize() + "!"
	#repeat name twice
	name_game_full += "\n" + "\n" + name.capitalize() + " " + name.capitalize()
	# bo section
	name_game_full = bo_name(name,name_game_full)
	# add bonana fanna
	name_game_full += "\n" + "bonana fanna"
	# fo section
	name_game_full = fo_name(name,name_game_full)
	#fee fi 
	name_game_full += "\n" +"fi fi"
	#mo section
	name_game_full = mo_name(name, name_game_full)
	#repeat name
	name_game_full += "\n" + name.capitalize() + "!"
	play_out_loud = gTTS(text=name_game_full, lang=LANGUAGE, slow=False)
	play_out_loud.save("name_game_audio.mp3")
	# os.system("name_game_audio.mp3")
	return name_game_full

def bo_name(name,name_game_full):
	name_base = name[1 : : ]
	first_char = name[0]
	first_two = name[:2]
	ch_base = name[2:]
	th_base = name[2:]
	if first_two not in FIRST_TWO_H:
		if first_char in VOWELS:
			name_game_full += "\n" +"Bo-" + "b"+name.lower()
		else:
			if first_char == "b" or first_char == "B":
				name_game_full += "\n" +"Bo-" +name_base
			else:
				name_game_full += "\n" +"Bo-" + "b"+name_base
	else:
		name_game_full += "\n" + "Bo-" + "b" + ch_base
	return name_game_full

#handles the potential swear of a name like chuck or tucker
def fo_name(name,name_game_full):
	name_base = name[1 : : ]
	first_char = name[0]
	first_two = name[:2]
	ch_base = name[2:]
	th_base = name[2:]
	if first_two != 'th' and first_two != 'Th':
		if first_char in VOWELS:
			name_game_full += "\n" +"Fo-" + "f"+name.lower()
		else:
			if first_char == "f" or first_char == "F":
				name_game_full += "\n" +"Fo-" +name_base
			else:
				if name == "chuck" or name == "Chuck":
						name_game_full += "\n" + "Fo-" + "fl"+ch_base+"."
				else:
					if first_two not in FIRST_TWO_H:
						name_game_full += "\n" + "Fo-" + "f" + name_base + "."
					else:
						name_game_full += "\n" + "Fo-" + "f" + ch_base + "."
	else:
		name_game_full += "\n" + "Fo-" + "f" + ch_base
	return name_game_full

def mo_name(name,name_game_full):
	name_base = name[1 : : ]
	first_char = name[0]
	first_two = name[:2]
	ch_base = name[2:]
	th_base = name[2:]
	if first_two not in FIRST_TWO_H:
		if first_char in VOWELS:
			name_game_full += "\n" +"Mo-" + "m"+name.lower()
		else:
			if first_char == "m" or first_char == "M":
				name_game_full += "\n" +"Mo-" +name_base
			else:
				name_game_full += "\n" +"Mo-" + "m"+name_base
	else:
		name_game_full += "\n" + "Mo-" + "m" + ch_base
	return name_game_full

	
"""
example name game:
Shirley! 
Shirley, Shirley
Bo-ber-ley, 
bo-na-na fanna
Fo-fer-ley. 
fee fi mo-mer-ley, 
Shirley!

"""
if __name__ == '__main__':
    main()