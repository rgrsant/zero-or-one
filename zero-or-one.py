'''
Zero ou Um
Jogo para três pessoas:
Jogador 1: Zero ou um; Jogador 2: Zero ou um; Jogador 3: Zero ou um;

Ganha o jogador que colocar um número diferente dos outros dois
'''

p1 = str(input("Nome do jogador 1:"))
p2 = str(input("Nome do jogador 2:"))
p3 = str(input("Nome do jogador 3:"))

print(p1,", escolha: 0 ou 1?")
p1p = int(input())
print(p2,", escolha: 0 ou 1?")
p2p = int(input())
print(p3,", escolha: 0 ou 1?")
p3p = int(input())


if ((p1p==0) and (p2p==0) and (p3p==1)) or ((p1p==1) and (p2p==1) and (p3p==0)):
  print(p3, "venceu!")
elif ((p1p==0) and (p2p==1) and (p3p==0)) or ((p1p==1) and (p2p==0) and (p3p==1)):
  print(p2, "venceu!")
elif ((p1p==1) and (p2p==0) and (p3p==0)) or ((p1p==0) and (p2p==1) and (p3p==1)):
  print(p1, "venceu!")
elif ((p1p==0) and (p2p==0) and (p3p==0)) or ((p1p==1) and (p2p==1) and (p3p==1)):
  print("Empate!")
else:
  print("Partida inválida.")