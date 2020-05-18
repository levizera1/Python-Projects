import textGameModulePTBR

def text_game_ptbr():
	nickname = input("Insira seu nickname: ")
	print(f"Eai, {nickname} Seja muito bem-vindo(a) ao jogo de perguntas. Espero que curta nosso jogo :) \n {nickname}, O tema do nosso jogo é: THOR \n")
	interactingWithThePlayer = input("Você Conhece o THOR? \n")
	if interactingWithThePlayer == "sim":
		print("Nossa, Que demais kkk Mas fique aqui que tenho certeza que você vai gostar \n")
	else:
		print("Sem problemas, você vai saber mais sobre ele hoje !! Continue aí! \n")

	def readyOrNot():
		readyOrNot = input("""
	[1] Continuar
	[2] Preciso de um minutinho para me preparar
		""")
		if readyOrNot == "1":
			print("Então vamos lá... \n")
		else:
			print("Sem problemas, Pode tirar um minutinho para se preparar :) \n")
			exit()
	readyOrNot()
	textGameModulePTBR.question1()

	answer = "associado a trovões, raios, tempestades, bosques e árvores sagrados, força, proteção da humanidade e santificação e fertilidade"
	guess = ""
	guess_count = 0
	guess_limit = 4
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("Na mitologia germânica, Thor (/ θɔːr /; do nórdico antigo: rórr, runic ᚦᚢᚱur) é um deus empunhando um martelo associado a quê? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: associado a trovões, raios, tempestades, bosques e árvores sagrados, força, proteção da humanidade e santificação e fertilidade \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!\n")

	readyOrNot()
	textGameModulePTBR.question2()

	answer = "povos germânicos"
	guess = ""
	guess_count = 0
	guess_limit = 4
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("Thor é um deus de destaque na história registrada de quais povos?\n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: povos germânicos \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!")

	readyOrNot()
	textGameModulePTBR.question3()

	answer = "Þjálfi e Röskva"
	guess = ""
	guess_count = 0
	guess_limit = 4
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("Quais são os nomes dos servos de Thor? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: Þjálfi e Röskva \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!")

	print(f"Olá, {nickname}, Você chegou aqui até que rápido. Você faz parte dos 5% Players mais inteligêntes desse jogo. Parabéns!! Mas vamos lá pra proxima pergunta... \n")
	readyOrNot()
	textGameModulePTBR.question4()

	answer = "Thor inspirou inúmeras obras de arte e referências a Thor aparecem na cultura popular moderna"
	guess = ""
	guess_count = 0
	guess_limit = 1
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("O que Thor Ispirou? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: Thor inspirou inúmeras obras de arte e referências a Thor aparecem na cultura popular moderna \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!\n")

	print("Eai, Essa quetão foi facilzinha né?Eu fiz assim pq as anteriores tinham sido um pouco mais dificeis. Lets Go pra proxima pergunta!! \n")
	readyOrNot()
	textGameModulePTBR.question5()

	answer = "Martelo do Thor"
	guess = ""
	guess_count = 0
	guess_limit = 3
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("O que é Mjölnir ?\n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: Martelo do Thor \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!\n")

	readyOrNot()
	textGameModulePTBR.question6()

	answer = "ele foi recuperá-lo, vestindo-se como uma noiva para se casar com um dos gigantes"
	guess = ""
	guess_count = 0
	guess_limit = 3
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("O que Thor fez pra conseguir seu martelo de volta? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: ele foi recuperá-lo, vestindo-se como uma noiva para se casar com um dos gigantes \n")
	else:
		print(f"{nickname}, VOCÊ GANHOU!!\n")

	readyOrNot()
	textGameModulePTBR.question7()

	answer = "Þrymskviða"
	guess = ""
	guess_count = 0
	guess_limit = 3
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("Qual o titulo do poema citado acima? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: Þrymskviða \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!\n")

	readyOrNot()
	textGameModulePTBR.question8()

	answer = "Thor é preso pelo demônio do fogo Surtur"
	guess = ""
	guess_count = 0
	guess_limit = 3
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("O que aconteceu 2 anos depois da batalha de Sokovia? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: Thor é preso pelo demônio do fogo Surtur \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!\n")

	readyOrNot()
	textGameModulePTBR.question9()

	answer = "Hela era o líder dos exércitos de Asgard"
	guess = ""
	guess_count = 0
	guess_limit = 3
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("O que Hela era? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: Hela era o líder dos exércitos de Asgard \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!\n")

	readyOrNot()
	textGameModulePTBR.question10()

	answer = "Poetic Edda "
	guess = ""
	guess_count = 0
	guess_limit = 3
	out_of_guesses = False

	while guess != answer and not(out_of_guesses):
		if guess_count < guess_limit:
			guess = input("Quem escreveu esse poema? \n")
			guess_count += 1
		else:
			out_of_guesses = True

	if out_of_guesses:
		print("RESPOSTA ERRADA!! A resposta certa é: Poetic Edda \n")
	else:
		print(f"{nickname}, VOCÊ VENCEU!!\n")
