import requests
from colorama import Fore, init

init()

dev = " 	 		 		 		 			Developer: Darth diX"
asci = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |   ______     | || |     ____     | || |  ___  ____   | || |  _________   | |
| | |_  _||_  _| | || |  |_   __ \   | || |   .'    `.   | || | |_  ||_  _|  | || | |_   ___  |  | |
| |   \ \  / /   | || |    | |__) |  | || |  /  .--.  \  | || |   | |_/ /    | || |   | |_  \_|  | |
| |    > `' <    | || |    |  ___/   | || |  | |    | |  | || |   |  __'.    | || |   |  _|  _   | |
| |  _/ /'`\ \_  | || |   _| |_      | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___/ |  | |
| | |____||____| | || |  |_____|     | || |   `.____.'   | || | |____||____| | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

print(Fore.LIGHTYELLOW_EX + asci)
print(Fore.YELLOW + dev)
print('\033[39m')



def id(poke):
	print(Fore.RED + F'\nNúmero do {pokemon} na Pokédex')
	print('\033[39m')
	for i in poke['id']:
		print(['id'])

def catch(poke):
	print(Fore.RED + f'\nHabilidades do {pokemon}')
	print('\033[39m')
	for i in poke['abilities']:
		print(i['ability']['name'])


def inf(poke):
	print(Fore.RED + f'\nTipo do {pokemon}')
	print('\033[39m')
	for i in poke['types']:
		print(i['type']['name'])


def stats(poke):
	print(Fore.RED + f'\nStatus do {pokemon}')
	print('\033[39m')
	for i in poke['stats']:
		print(i['stat']['name'])
		print(i['base_stat'])

def games(poke):
	print(Fore.RED + F'\nJogos onde é possivel capturar {pokemon}')
	print('\033[39m')
	for i in poke['game_indices']:
		print(i['version']['name'])



def main():
	global pokemon
	pokemon = str(input('Pokemon: '))
	api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
	res = requests.get(api)
	poke = res.json()

	catch(poke)
	inf(poke)
	stats(poke)
	games(poke)



if __name__ == '__main__':
	main()

