#Juego de piedra papel o tijera
import random
import os
options=('piedra', 'papel', 'tijera')
rounds=1
computer_wins=0
user_wins=0
while rounds>0:
  print(f"Round: {rounds}\nUser wins: {user_wins}\nComputer wins: {computer_wins}\n")
  user_input = input('Piedra, papel o tijera => ')
  user_option = user_input.lower()
  if not user_option in options:
    print('Opcion invalida')
  else:
    computer_option = random.choice(options)
    print(f"\nUser option: {user_option.capitalize()}\nComputer option:   {computer_option.capitalize()}\n")
    if user_option == computer_option:
      print ('Empate!')
    elif user_option == 'piedra':
      if computer_option == 'tijera':
        print('Piedra gana a tijera.\nUser gano!')
        user_wins+=1
      else: 
        print('Papel gana a piedra.\nComputer gano!')
        computer_wins+=1
    elif user_option == 'papel':
      if computer_option == 'tijera':
        print('Tijera gana a papel\nComputer gano!')
        computer_wins+=1
      else:
        print('Papel gana a piedra. User gano!')
        user_wins+=1
    elif user_option == 'tijera':
      if computer_option == 'piedra':
        print('Piedra gana a tijera.\nComputer gano!')
        computer_wins+=1
      else:
        print('Tijera gana a papel.\nUser gano!')
        user_wins+=1
    if user_wins==2:
      print("User ha ganado la ronda!")
    elif computer_wins==2:
      print("Computer ha ganado la ronda!")
    if user_wins==2 or computer_wins==2:
      user_wins=0
      computer_wins=0
      rounds+=1
      res_options=('yes', 'no')
      res=input("Jugar otra ronda? => ")
      res=res.lower()
      while not res in res_options:
        print("Opcion invalida!")
        res=input("Jugar otra ronda? => ")
        res=res.lower()
      if res == 'no':
        print("Adios!")
        break
  res=input("\nPresiona una tecla...") 
  os.system("clear")