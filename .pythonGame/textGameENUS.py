import textGameModuleENUS

nickname = input("Enter a nickname: ")
print(f"Hey, {nickname} Welcome to the text game. I hope you enjoy it :) \n {nickname}, Our Game will be about: THOR \n")
interactingWithThePlayer = input("Do you know something about Thor? \n")

if interactingWithThePlayer == "yes":
    print("Ohh, Nice! But stay here that im sure that you will enjoy it \n")
else:
    print("No problem, You will know more about him Today!! Stay There! \n")

def readyOrNot():
	readyOrNot = input("""
[1] Keep Going
[2] I need a minute to breathe ;)
	""")
	if readyOrNot == "1":
	    print("So... Lets Go... \n")
	else:
	    print("No problem, take a breathe and then come back :) \n")
	    exit()
readyOrNot()
textGameModuleENUS.question1()

answer = "associated with thunder, lightning, storms, sacred groves and trees, strength, the protection of mankind and also hallowing and fertility."
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("In Germanic mythology, Thor (/θɔːr/; from Old Norse: Þórr, runic ᚦᚢᚱ þur) is a hammer-wielding god associated to what? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The right answer is: thunder, lightning, storms, sacred groves and trees, strength, the protection of mankind and also hallowing and fertility \n")
else:
	print(f"{nickname} YOU WIN!!\n")

readyOrNot()
textGameModuleENUS.question2()

answer = "throughout the recorded history of the Germanic peoples, from the Roman occupation of regions of Germania, to the tribal expansions of the Migration Period, to his high popularity during the Viking Age"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Thor is a prominently mentioned god throughout what? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The right answer is:  Throughout the recorded history of the Germanic peoples, from the Roman occupation of regions of Germania, to the tribal expansions of the Migration Period, to his high popularity during the Viking Age \n")
else:
	print(f"{nickname}, YOU WIN!!")

print(f"Hey, {nickname} I can see that you got at here, You are smart (if you just anwered worng, dont worry we have more levels for you.")
readyOrNot()
textGameModuleENUS.question3()

answer = "throughout the recorded history of the Germanic peoples, from the Roman occupation of regions of Germania, to the tribal expansions of the Migration Period, to his high popularity during the Viking Age"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Thor is a prominently mentioned god throughout what? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: throughout the recorded history of the Germanic peoples, from the Roman occupation of regions of Germania, to the tribal expansions of the Migration Period, to his high popularity during the Viking Age \n")
else:
	print(f"{nickname}, YOU WIN!!")

print(f"Hello, {nickname}, I can see that you got at here, You are smart (if you just anwered worng, dont worry we have more levels for you. \n")
readyOrNot()
textGameModuleENUS.question4()

answer = "Thor has inspired numerous works of art and references to Thor appear in modern popular culture."
guess = ""
guess_count = 0
guess_limit = 1
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("What Thor had Inspired? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: Thor has inspired numerous works of art and references to Thor appear in modern popular culture. \n")
else:
	print(f"{nickname}, YOU WIN!!\n")

print("Hey, This question was really easy, isnt? haha... Lets go to the next. I promisse that the next question will need more knowledge of you. \n")
readyOrNot()
textGameModuleENUS.question5()

answer = "Thors Hammer"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("What is Mjölnir ?\n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: Thors Hammer \n")
else:
	print(f"{nickname}, YOU WIN!!\n")

readyOrNot()
textGameModuleENUS.question6()

answer = "he went to retrieve it by dressing as a bride to be married to one of the giants"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("What Thor did to get back his hammer? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: He went to retrieve it by dressing as a bride to be married to one of the giants. \n")
else:
	print(f"{nickname}, YOU WIN!!\n")

readyOrNot()
textGameModuleENUS.question7()

answer = "Þrymskviða"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("What is the Title of the poem cited on the text? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: Þrymskviða \n")
else:
	print(f"{nickname}, YOU WIN!!\n")

readyOrNot()
textGameModuleENUS.question8()

answer = "Thor is imprisoned by the fire demon Surtur"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("What Happened Two years after the battle of Sokovia? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: Thor is imprisoned by the fire demon Surtur \n")
else:
	print(f"{nickname}, YOU WIN!!\n")

readyOrNot()
textGameModuleENUS.question9()

answer = "Hela was the leader of Asgard's armies, conquering the Nine Realms with Odin"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("What Hela was? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: Hela was the leader of Asgard's armies, conquering the Nine Realms with Odin \n")
else:
	print(f"{nickname}, YOU WIN!!\n")

readyOrNot()
textGameModuleENUS.question10()

answer = "It sates itself on the life-blood   \n of fated men, paints red the powers' homes\n   with crimson gore. Black become the sun's beams\n   in the summers that follow, weathers all treacherous.\n   Do you still seek to know? And what? "
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != answer and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Who wrote this poem? \n")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Oh Noo :( The Right Answer is: It sates itself on the life-blood   of fated men, paints red the powers' homes   with crimson gore. Black become the sun's beams   in the summers that follow, weathers all treacherous.   Do you still seek to know? And what? \n")
else:
	print(f"{nickname}, YOU WIN!!\n")
