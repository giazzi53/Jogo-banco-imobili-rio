import random
import sys

inicio = 0
prisao = 8

sorte1 = 4
sorte2 = 12

'''ppr1 = 1
ppr2 = 3
ppr3 = 6
ppr4 = 7
ppr5 = 9
ppr6 = 11
ppr7 = 14
ppr8 = 15'''
ppr1 = ""
ppr2 = ""
ppr3 = ""
ppr4 = ""
ppr5 = ""
ppr6 = ""
ppr7 = ""
ppr8 = ""

emprego1 = ""
emprego2 = ""

imposto1 = 2
imposto2 = 10

nomejog1 = input("Digite o nome do jogador 1: ")
jogador1 = 3000
posjog1 = 0
tentjog1 = 0
presojog1 = False
faliujog1 = False

nomejog2 = input("Digite o nome do jogador 2: ")
jogador2 = 3000
posjog2 = 0
tentjog2 = 0
presojog2 = False
faliujog2 = False

nomejog3 = input("Digite o nome do jogador 3: ")
jogador3 = 3000
posjog3 = 0
tentjog3 = 0
presojog3 = False
faliujog3 = False

nomejog4 = input("Digite o nome do jogador 4: ")
jogador4 = 3000
posjog4 = 0
tentjog4 = 0
presojog4 = False
faliujog4 = False

quant_jogs = 0
if nomejog1 != "":
    quant_jogs += 1
else:
    faliujog1 = True
if nomejog2 != "":
    quant_jogs += 1
else:
    faliujog2 = True
if nomejog3 != "":
    quant_jogs += 1
else:
    faliujog3 = True
if nomejog4 != "":
    quant_jogs += 1
else:
    faliujog4 = True

if quant_jogs < 2:
    print("Não é possivel jogar com menos de 2 jogadores!")
    sys.exit()

while int(not faliujog1) + int(not faliujog2) + int(not faliujog3) + int(not faliujog4) > 1:
    
    if not faliujog1 and nomejog1 != "":
        print("\n------------------------------------------------")
        print("|                  Jogador 1                   |")
        print("------------------------------------------------")
        print("|      Formação       |        Salário         |")
        print("------------------------------------------------")
        
        if emprego1 == nomejog1:
            print("|     ENGENHEIRO      |        R$100,00        |")
        if emprego2 == nomejog1:
            print("|      MEDICINA       |        R$200,00        |")
            
        print("------------------------------------------------")
        print("|        Casas        |        Aluguel         |")
        print("------------------------------------------------")
        if ppr1 == nomejog1:
            print("|      Itaquera       |        R$80,00         |")
            print("------------------------------------------------")
        if ppr2 == nomejog1:
            print("|       Penha         |        R$100,00        |")
            print("------------------------------------------------")
        if ppr3 == nomejog1:
            print("|       Osasco        |        R$130,00        |")
            print("------------------------------------------------")
        if ppr4 == nomejog1:
            print("|       Barueri       |        R$150,00        |")
            print("------------------------------------------------")
        if ppr5 == nomejog1:
            print("|      Pinheiros      |        R$170,00        |")
            print("------------------------------------------------")
        if ppr6 == nomejog1:
            print("|       Augusta       |        R$190,00        |")
            print("------------------------------------------------")
        if ppr7 == nomejog1:
            print("|  Jardim Paulista    |        R$240,00        |")
            print("------------------------------------------------")
        if ppr8 == nomejog1:
            print("|      Brooklin       |        R$280,00        |")
            print("------------------------------------------------")    
        if presojog1:
            tentjog1 += 1
            print("\nVocê está preso", nomejog1, "você precisa tirar abaixo de 3 para sair")
            print("Você está na tentativa:",tentjog1)
            input("Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
          
            print("Você tirou",dado)
            if dado < 3:
                print("Você saiu da prisão!")
                presojog1 = False
                tentjog1 = 0
            else:
                print("Você não tirou o número certo, tente na próxima rodada")
                if tentjog1 == 3:
                    print("\n" + str(nomejog1) + " você estourou o limite de tentativas para sair da prisão, você terá que pagar R$400,00")
                    print(str(nomejog1) + " seu saldo é R$" + format(jogador1, '.2f'))
                    jogador1 -= 400
                    presojog1 = False
                    tentjog1 = 0
                if jogador1 < 0:
                    print(nomejog1, " você faliu, que pena!")
                    faliujog1 = True
            
        else:
            print(str(nomejog1) + " você está na casa: " + str(posjog1))
            print(str(nomejog1) + " você possui em conta R$" + format(jogador1, '.2f'))
            input("\n" + str(nomejog1) + ": Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
            print("valor do dado:",dado)
            posjog1 += dado
            
            if posjog1 > 15:
                dado = posjog1 - 15
                posjog1 = dado - 1
                jogador1 += 200
                print(nomejog1, "você recebeu R$200,00 por passar no inicio")
                if emprego1 == nomejog1:
                    print(nomejog1, "você recebeu R$100,00 pelo seu salário de Engenheiro")
                    jogador1 += 100
                    print(nomejog1 + " você está com R$" + format(jogador1, '.2f'))
                elif emprego2 == nomejog1:
                    print(nomejog1 ,"você recebeu R$200,00 pelo seu salário de Médico")
                    jogador1 += 200
                    print(nomejog1 + " você está com R$" + format(jogador1, '.2f'))

            print(str(nomejog1) + " você foi para a casa: " + str(posjog1))

            if posjog1 == 1:
                if ppr1 == "":
                    if jogador1 >= 400:
                        compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 400
                            ppr1 = nomejog1
                            print(str(nomejog1) + " comprou a propriedade em Itaquera")
                            print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Itaquera")
                elif ppr1 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade em Itaquera")
                else:
                    if ppr1 == nomejog2:
                        jogador2 += 80
                        jogador1 -= 80
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$80,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr1 == nomejog3:
                        jogador3 += 80
                        jogador1 -= 80
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$80,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr1 == nomejog4:
                        jogador4 += 80
                        jogador1 -= 80
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$80,00 para o",nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                        
            elif posjog1 == 2:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador1*0.1, '.2f'));
                jogador1 -= float(format(jogador1*0.1, '.2f'))
                print(nomejog1, "possui em conta R$", format(jogador1, '.2f'))
                
            elif posjog1 == 3:
                if ppr2 == "":
                    if jogador1 >= 500:
                        compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n:")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 500
                            ppr2 = nomejog1
                            print(str(nomejog1) + " comprou a propriedade na Penha")
                            print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade na Penha")
                elif ppr2 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade na Penha")
                else:
                    if ppr2 == nomejog2:
                        jogador2 += 100
                        jogador1 -= 100
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$100,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr2 == nomejog3:
                        jogador3 += 100
                        jogador1 -= 100
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$100,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr2 == nomejog4:
                        jogador4 += 100
                        jogador1 -= 100
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$100,00 para o", nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                        
            elif posjog1 == 4:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog1 = 8
                    presojog1 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador1 += 200
                    
            elif posjog1 == 5:
                if emprego1 == "":
                    if jogador1 >= 1500:
                        print(nomejog1, "você caiu na faculdade de Engenharia, se formado você receberá R$100,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer == "S":
                            emprego1 = nomejog1
                            jogador1 -= 1500
                            print(str(nomejog1) + ", você se graduou em Engenharia")
                    else:
                        print("Você não possui dinheiro suficiente para pegar pelos estudos de Engenharia")
                        print("Você possui: R$", format(jogador1, '.2f'))
                        print("Para pagar a graduação em Engenharia é necessário ter no mínimo R$1500,00")
                else:
                    print("Você caiu na gradução de Engenharia mas ela não está mais disponível")

            elif posjog1 == 6:
                if ppr3 == "":
                    if jogador1 >= 650:
                        compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 650
                            ppr3 = nomejog1
                            print(str(nomejog1) + " comprou a propriedade em Osasco")
                            print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Osasco")
                elif ppr3 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade em Osasco")
                else:
                    if ppr3 == nomejog2:
                        jogador2 += 130
                        jogador1 -= 130
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$130,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr3 == nomejog3:
                        jogador3 += 130
                        jogador1 -= 130
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$130,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr3 == nomejog4:
                        jogador4 += 130
                        jogador1 -= 130
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$130,00 para o", nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))

            elif posjog1 == 7:
                if ppr4 == "":
                    if jogador1 >= 750:
                        compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 750
                            ppr4 = nomejog1
                            print(str(nomejog1) + " comprou a propriedade em Barueri")
                            print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Barueri")
                elif ppr4 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade em Barueri")
                else:
                    if ppr4 == nomejog2:
                        jogador2 += 150
                        jogador1 -= 150
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$150,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr4 == nomejog3:
                        jogador3 += 150
                        jogador1 -= 150
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$150,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr4 == nomejog4:
                        jogador4 += 150
                        jogador1 -= 150
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$150,00 para o", nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))

            elif posjog1 == 8:
                print(nomejog1, ", você está de visitante na prisão!")

            elif posjog1 == 9:
                if ppr5 == "":
                    if jogador1 >= 850:
                        compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 850
                            ppr5 = nomejog1
                            print(str(nomejog1) + " comprou a propriedade em Pinheiros")
                            print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Pinheiros")
                elif ppr5 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade em Pinheiros")
                else:
                    if ppr5 == nomejog2:
                        jogador2 += 170
                        jogador1 -= 170
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$170,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr5 == nomejog3:
                        jogador3 += 170
                        jogador1 -= 170
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$170,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr5 == nomejog4:
                        jogador4 += 170
                        jogador1 -= 170
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$170,00 para o", nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))

            elif posjog1 == 10:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador1*0.1, '.2f'));
                jogador1 -= float(format(jogador1*0.1, '.2f'))
                print(str(nomejog1), "possui em conta R$", format(jogador1, '.2f'))

            elif posjog1 == 11:
                if ppr6 == "":
                    if jogador1 >= 950:
                        compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 950
                            ppr6 = nomejog1
                            print(str(nomejog1) + " comprou a propriedade na Augusta")
                            print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade na Augusta")
                elif ppr6 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade na Augusta")
                else:
                    if ppr6 == nomejog2:
                        jogador2 += 190
                        jogador1 -= 190
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$190,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr6 == nomejog3:
                        jogador3 += 190
                        jogador1 -= 190
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$190,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr6 == nomejog4:
                        jogador4 += 190
                        jogador1 -= 190
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$190,00 para o", nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))

            elif posjog1 == 12:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog1 = 8
                    presojog1 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador1 += 200

            elif posjog1 == 13:
                if emprego2 == "":
                    if jogador1 >= 2000:
                        print(str(nomejog1) + " você caiu na faculdade de Medicina, se formando você receberá R$200,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer =="S":
                            emprego2 = nomejog1
                            jogador1 -= 2000
                            print(str(nomejog1) + ", você se graduou em Medicina")
                    else:
                        print("Você não possui dinheiro suficiente para pagar pelos estudos de Medicina")
                        print("Você possui: R$", format(jogador1, '.2f'))
                        print("Para pagar a graduação em Medicina é necessário ter no mínimo R$2000,00")
                else:
                    print("Você caiu na graduação de Medicina mas ela não está mais disponível")

            elif posjog1 == 14:
                if ppr7 == "":
                    if jogador1 >= 1200:
                        compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 1200
                            ppr7 = nomejog1
                            print(str(nomejog1) + " comprou a propriedade no Jardim Paulista")
                            print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Jardim Paulista")
                elif ppr7 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade no Jardim Paulista")
                else:
                    if ppr7 == nomejog2:
                        jogador2 += 240
                        jogador1 -= 240
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$240,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr7 == nomejog3:
                        jogador3 += 240
                        jogador1 -= 240
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$240,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr7 == nomejog4:
                        jogador4 += 240
                        jogador1 -= 240
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$240,00 para o", nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))

            elif posjog1 == 15:
                if ppr8 == "":
                    if jogador1 >= 1400: 
                        compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador1 -= 1400
                            ppr8 = nomejog1
                            print(str(nomejog1), " comprou a propriedade no Brooklin")
                            print(str(nomejog1), " possui em conta R$", format(jogador1, '.2f'))
                    else:
                        print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Brooklin")
                elif ppr8 == nomejog1:
                    print(str(nomejog1) + " você já possui a propriedade no Brooklin")
                else:
                    if ppr8 == nomejog2:
                        jogador2 += 280
                        jogador1 -= 280
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$280,00 para o", nomejog2)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr8 == nomejog3:
                        jogador3 += 280
                        jogador1 -= 280
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$280,00 para o", nomejog3)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                    elif ppr8 == nomejog4:
                        jogador4 += 280
                        jogador1 -= 280
                        print(str(nomejog1) + " você teve que pagar o aluguel de R$280,00 para o", nomejog4)
                        print(str(nomejog1) + " possui em conta R$", format(jogador1, '.2f'))
                        
            if jogador1 < 0:
                    print(str(nomejog1) + " faliu, que pena!")
                    faliujog1 = True


    if not faliujog2 and nomejog2 != "":
        print("\n------------------------------------------------")
        print("|                  Jogador 2                   |")
        print("------------------------------------------------")
        print("|      Formação       |        Salário         |")
        print("------------------------------------------------")
        
        if emprego1 == nomejog2:
            print("|     ENGENHEIRO      |        R$100,00        |")
        if emprego2 == nomejog2:
            print("|      MEDICINA       |        R$200,00        |")
            
        print("------------------------------------------------")
        print("|        Casas        |        Aluguel         |")
        print("------------------------------------------------")
        if ppr1 == nomejog2:
            print("|      Itaquera       |        R$80,00         |")
            print("------------------------------------------------")
        if ppr2 == nomejog2:
            print("|       Penha         |        R$100,00        |")
            print("------------------------------------------------")
        if ppr3 == nomejog2:
            print("|       Osasco        |        R$130,00        |")
            print("------------------------------------------------")
        if ppr4 == nomejog2:
            print("|       Barueri       |        R$150,00        |")
            print("------------------------------------------------")
        if ppr5 == nomejog2:
            print("|      Pinheiros      |        R$170,00        |")
            print("------------------------------------------------")
        if ppr6 == nomejog2:
            print("|       Augusta       |        R$190,00        |")
            print("------------------------------------------------")
        if ppr7 == nomejog2:
            print("|  Jardim Paulista    |        R$240,00        |")
            print("------------------------------------------------")
        if ppr8 == nomejog2:
            print("|      Brooklin       |        R$280,00        |")
            print("------------------------------------------------")
            
        if presojog2:
            tentjog2 += 1
            print("\nVocê está preso", nomejog2, "você precisa tirar abaixo de 3 para sair")
            print("Você está na tentativa:",tentjog2)
            input("Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
          
            print("Você tirou",dado)
            if dado < 3:
                print("Você saiu da prisão!")
                presojog2 = False
                tentjog2 = 0
            else:
                print("Você não tirou o número certo, tente na próxima rodada")
                if tentjog2 == 3:
                    print("\n" + str(nomejog2) + " você estourou o limite de tentativas para sair da prisão, você terá que pagar R$400,00")
                    print(str(nomejog2) + " seu saldo é R$" + format(jogador2, '.2f'))
                    jogador2 -= 400
                    presojog2 = False
                    tentjog2 = 0
                if jogador2 < 0:
                    print(nomejog2, " você faliu, que pena!")
                    faliujog2 = True
            
        else:
            print(str(nomejog2) + " você está na casa: " + str(posjog2))
            print(str(nomejog2) + " você possui em conta R$" + format(jogador2, '.2f'))
            input("\n" + str(nomejog2) + ": Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
            print("valor do dado:",dado)
            posjog2 += dado
            
            if posjog2 > 15:
                dado = posjog2 - 15
                posjog2 = dado - 1
                jogador2 += 200
                print(str(nomejog2) + " você foi para a casa: " + str(posjog2))
                print(nomejog2, "você recebeu R$200,00 por passar no inicio")
                if emprego2 == nomejog2:
                    print(nomejog2, "você recebeu R$100,00 pelo seu salário de Engenheiro")
                    jogador2 += 100
                elif emprego2 == nomejog2:
                    print(nomejog2 ,"você recebeu R$200,00 pelo seu salário de Médico")
                    jogador2 += 200

            if posjog2 == 1:
                if ppr1 == "":
                    if jogador2 >= 400:
                        compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 400
                            ppr1 = nomejog2
                            print(str(nomejog2) + " comprou a propriedade em Itaquera")
                            print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Itaquera")
                elif ppr1 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade em Itaquera")
                else:
                    if ppr1 == nomejog1:
                        jogador1 += 80
                        jogador2 -= 80
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$80,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr1 == nomejog3:
                        jogador3 += 80
                        jogador2 -= 80
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$80,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr1 == nomejog4:
                        jogador4 += 80
                        jogador2 -= 80
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$80,00 para o",nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                        
            elif posjog2 == 2:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador2*0.1, '.2f'));
                jogador2 -= float(format(jogador2*0.1, '.2f'))
                print(nomejog2, "possui em conta R$", format(jogador2, '.2f'))
                
            elif posjog2 == 3:
                if ppr2 == "":
                    if jogador2 >= 500:
                        compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n:")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 500
                            ppr2 = nomejog2
                            print(str(nomejog2) + " comprou a propriedade na Penha")
                            print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade na Penha")
                elif ppr2 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade na Penha")
                else:
                    if ppr2 == nomejog1:
                        jogador1 += 100
                        jogador2 -= 100
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$100,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr2 == nomejog3:
                        jogador3 += 100
                        jogador2 -= 100
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$100,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr2 == nomejog4:
                        jogador4 += 100
                        jogador2 -= 100
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$100,00 para o", nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                        
            elif posjog2 == 4:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog2 = 8
                    presojog2 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador2 += 200
                    
            elif posjog2 == 5:
                if emprego1 == "":
                    if jogador2 >= 1500:
                        print(nomejog2, "você caiu na faculdade de Engenharia, se formado você receberá R$100,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer =="S":
                            emprego1 = nomejog2
                            jogador2 -= 1500
                            print(str(nomejog2) + ", você se graduou em Engenharia")
                    else:
                        print("Você não possui dinheiro suficiente para pegar pelos estudos de Engenharia")
                        print("Você possui: R$", format(jogador2, '.2f'))
                        print("Para pagar a graduação em Engenharia é necessário ter no mínimo R$1500,00")
                else:
                    print("Você caiu na gradução de Engenharia mas ela não está mais disponível")

            elif posjog2 == 6:
                if ppr3 == "":
                    if jogador2 >= 650:
                        compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 650
                            ppr3 = nomejog2
                            print(str(nomejog2) + " comprou a propriedade em Osasco")
                            print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Osasco")
                elif ppr3 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade em Osasco")
                else:
                    if ppr3 == nomejog1:
                        jogador1 += 130
                        jogador2 -= 130
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$130,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr3 == nomejog3:
                        jogador3 += 130
                        jogador2 -= 130
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$130,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr3 == nomejog4:
                        jogador4 += 130
                        jogador2 -= 130
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$130,00 para o", nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))

            elif posjog2 == 7:
                if ppr4 == "":
                    if jogador2 >= 750:
                        compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 750
                            ppr4 = nomejog2
                            print(str(nomejog2) + " comprou a propriedade em Barueri")
                            print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Barueri")
                elif ppr4 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade em Barueri")
                else:
                    if ppr4 == nomejog1:
                        jogador1 += 150
                        jogador2 -= 150
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$150,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr4 == nomejog3:
                        jogador3 += 150
                        jogador2 -= 150
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$150,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr4 == nomejog4:
                        jogador4 += 150
                        jogador2 -= 150
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$150,00 para o", nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))

            elif posjog2 == 8:
                print(nomejog2, ", você está de visitante na prisão!")

            elif posjog2 == 9:
                if ppr5 == "":
                    if jogador2 >= 850:
                        compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 850
                            ppr5 = nomejog2
                            print(str(nomejog2) + " comprou a propriedade em Pinheiros")
                            print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Pinheiros")
                elif ppr5 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade em Pinheiros")
                else:
                    if ppr5 == nomejog1:
                        jogador1 += 170
                        jogador2 -= 170
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$170,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr5 == nomejog3:
                        jogador3 += 170
                        jogador2 -= 170
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$170,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr5 == nomejog4:
                        jogador4 += 170
                        jogador2 -= 170
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$170,00 para o", nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))

            elif posjog2 == 10:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador2*0.1, '.2f'));
                jogador2 -= float(format(jogador2*0.1, '.2f'))
                print(str(nomejog2), "possui em conta R$", format(jogador2, '.2f'))

            elif posjog2 == 11:
                if ppr6 == "":
                    if jogador2 >= 950:
                        compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 950
                            ppr6 = nomejog2
                            print(str(nomejog2) + " comprou a propriedade na Augusta")
                            print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade na Augusta")
                elif ppr6 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade na Augusta")
                else:
                    if ppr6 == nomejog1:
                        jogador1 += 190
                        jogador2 -= 190
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$190,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr6 == nomejog3:
                        jogador3 += 190
                        jogador2 -= 190
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$190,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr6 == nomejog4:
                        jogador4 += 190
                        jogador2 -= 190
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$190,00 para o", nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))

            elif posjog2 == 12:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog2 = 8
                    presojog2 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador2 += 200

            elif posjog2 == 13:
                if emprego2 == "":
                    if jogador2 >= 2000:
                        print(str(nomejog2) + " você caiu na faculdade de Medicina, se formando você receberá R$200,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer =="S":
                            emprego2 = nomejog2
                            jogador2 -= 2000
                            print(str(nomejog2) + ", você se graduou em Medicina")
                    else:
                        print("Você não possui dinheiro suficiente para pagar pelos estudos de Medicina")
                        print("Você possui: R$", format(jogador2, '.2f'))
                        print("Para pagar a graduação em Medicina é necessário ter no mínimo R$2000,00")
                else:
                    print("Você caiu na graduação de Medicina mas ela não está mais disponível")

            elif posjog2 == 14:
                if ppr7 == "":
                    if jogador2 >= 1200:
                        compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 1200
                            ppr7 = nomejog2
                            print(str(nomejog2) + " comprou a propriedade no Jardim Paulista")
                            print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Jardim Paulista")
                elif ppr7 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade no Jardim Paulista")
                else:
                    if ppr7 == nomejog1:
                        jogador1 += 240
                        jogador2 -= 240
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$240,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr7 == nomejog3:
                        jogador3 += 240
                        jogador2 -= 240
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$240,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr7 == nomejog4:
                        jogador4 += 240
                        jogador2 -= 240
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$240,00 para o", nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))

            elif posjog2 == 15:
                if ppr8 == "":
                    if jogador2 >= 1400: 
                        compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador2 -= 1400
                            ppr8 = nomejog2
                            print(str(nomejog2), " comprou a propriedade no Brooklin")
                            print(str(nomejog2), " possui em conta R$", format(jogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Brooklin")
                elif ppr8 == nomejog2:
                    print(str(nomejog2) + " você já possui a propriedade no Brooklin")
                else:
                    if ppr8 == nomejog2:
                        jogador1 += 280
                        jogador2 -= 280
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$280,00 para o", nomejog1)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr8 == nomejog3:
                        jogador3 += 280
                        jogador2 -= 280
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$280,00 para o", nomejog3)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                    elif ppr8 == nomejog4:
                        jogador4 += 280
                        jogador2 -= 280
                        print(str(nomejog2) + " você teve que pagar o aluguel de R$280,00 para o", nomejog4)
                        print(str(nomejog2) + " possui em conta R$", format(jogador2, '.2f'))
                        
            if jogador2 < 0:
                    print(str(nomejog2) + " faliu, que pena!")
                    faliujog2 = True

                    

    if not faliujog3 and nomejog3 != "":
        print("\n------------------------------------------------")
        print("|                  Jogador 3                   |")
        print("------------------------------------------------")
        print("|      Formação       |        Salário         |")
        print("------------------------------------------------")
        
        if emprego1 == nomejog3:
            print("|     ENGENHEIRO      |        R$100,00        |")
        if emprego2 == nomejog3:
            print("|      MEDICINA       |        R$200,00        |")
            
        print("------------------------------------------------")
        print("|        Casas        |        Aluguel         |")
        print("------------------------------------------------")
        if ppr1 == nomejog3:
            print("|      Itaquera       |        R$80,00         |")
            print("------------------------------------------------")
        if ppr2 == nomejog3:
            print("|       Penha         |        R$100,00        |")
            print("------------------------------------------------")
        if ppr3 == nomejog3:
            print("|       Osasco        |        R$130,00        |")
            print("------------------------------------------------")
        if ppr4 == nomejog3:
            print("|       Barueri       |        R$150,00        |")
            print("------------------------------------------------")
        if ppr5 == nomejog3:
            print("|      Pinheiros      |        R$170,00        |")
            print("------------------------------------------------")
        if ppr6 == nomejog3:
            print("|       Augusta       |        R$190,00        |")
            print("------------------------------------------------")
        if ppr7 == nomejog3:
            print("|  Jardim Paulista    |        R$240,00        |")
            print("------------------------------------------------")
        if ppr8 == nomejog3:
            print("|      Brooklin       |        R$280,00        |")
            print("------------------------------------------------")
                
        if presojog3:
            tentjog3 += 1
            print("\nVocê está preso", nomejog3, "você precisa tirar abaixo de 3 para sair")
            print("Você está na tentativa:",tentjog3)
            input("Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
          
            print("Você tirou",dado)
            if dado < 3:
                print("Você saiu da prisão!")
                presojog3 = False
                tentjog3 = 0
            else:
                print("Você não tirou o número certo, tente na próxima rodada")
                if tentjog3 == 3:
                    print("\n" + str(nomejog3) + " você estourou o limite de tentativas para sair da prisão, você terá que pagar R$400,00")
                    print(str(nomejog3) + " seu saldo é R$" + format(jogador3, '.2f'))
                    jogador3 -= 400
                    presojog3 = False
                    tentjog3 = 0
                if jogador3 < 0:
                    print(nomejog3, " você faliu, que pena!")
                    faliujog3 = True
                
        else:
            print(str(nomejog3) + " você está na casa: " + str(posjog3))
            print(str(nomejog3) + " você possui em conta R$" + format(jogador3, '.2f'))
            input("\n" + str(nomejog3) + ": Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
            print("valor do dado:",dado)
            posjog3 += dado
            
            if posjog3 > 15:
                dado = posjog3 - 15
                posjog3 = dado - 1
                jogador3 += 200
                print(str(nomejog3) + " você foi para a casa: " + str(posjog3))
                print(nomejog3, "você recebeu R$200,00 por passar no inicio")
                if emprego1 == nomejog3:
                    print(nomejog3, "você recebeu R$100,00 pelo seu salário de Engenheiro")
                    jogador3 += 100
                elif emprego2 == nomejog3:
                    print(nomejog3 ,"você recebeu R$200,00 pelo seu salário de Médico")
                    jogador3 += 200

            if posjog3 == 1:
                if ppr1 == "":
                    if jogador3 >= 400:
                        compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 400
                            ppr1 = nomejog3
                            print(str(nomejog3) + " comprou a propriedade em Itaquera")
                            print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Itaquera")
                elif ppr1 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade em Itaquera")
                else:
                    if ppr1 == nomejog1:
                        jogador1 += 80
                        jogador3 -= 80
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$80,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr1 == nomejog2:
                        jogador2 += 80
                        jogador3 -= 80
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$80,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr1 == nomejog4:
                        jogador4 += 80
                        jogador3 -= 80
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$80,00 para o",nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                        
            elif posjog3 == 2:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador3*0.1, '.2f'));
                jogador3 -= float(format(jogador3*0.1, '.2f'))
                print(nomejog3, "possui em conta R$", format(jogador3, '.2f'))
                
            elif posjog3 == 3:
                if ppr2 == "":
                    if jogador3 >= 500:
                        compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n:")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 500
                            ppr2 = nomejog3
                            print(str(nomejog3) + " comprou a propriedade na Penha")
                            print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade na Penha")
                elif ppr2 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade na Penha")
                else:
                    if ppr2 == nomejog2:
                        jogador2 += 100
                        jogador3 -= 100
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$100,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr2 == nomejog1:
                        jogador1 += 100
                        jogador3 -= 100
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$100,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr2 == nomejog4:
                        jogador4 += 100
                        jogador3 -= 100
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$100,00 para o", nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                        
            elif posjog3 == 4:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog3 = 8
                    presojog3 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador3 += 200
                    
            elif posjog3 == 5:
                if emprego1 == "":
                    if jogador3 >= 1500:
                        print(nomejog3, "você caiu na faculdade de Engenharia, se formado você receberá R$100,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer =="S":
                            emprego1 = nomejog3
                            jogador3 -= 1500
                            print(str(nomejog3) + ", você se graduou em Engenharia")
                    else:
                        print("Você não possui dinheiro suficiente para pegar pelos estudos de Engenharia")
                        print("Você possui: R$", format(jogador3, '.2f'))
                        print("Para pagar a graduação em Engenharia é necessário ter no mínimo R$1500,00")
                else:
                    print("Você caiu na gradução de Engenharia mas ela não está mais disponível")

            elif posjog3 == 6:
                if ppr3 == "":
                    if jogador3 >= 650:
                        compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 650
                            ppr3 = nomejog3
                            print(str(nomejog3) + " comprou a propriedade em Osasco")
                            print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Osasco")
                elif ppr3 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade em Osasco")
                else:
                    if ppr3 == nomejog2:
                        jogador2 += 130
                        jogador3 -= 130
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$130,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr3 == nomejog1:
                        jogador1 += 130
                        jogador3 -= 130
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$130,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr3 == nomejog4:
                        jogador4 += 130
                        jogador3 -= 130
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$130,00 para o", nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))

            elif posjog3 == 7:
                if ppr4 == "":
                    if jogador3 >= 750:
                        compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 750
                            ppr4 = nomejog3
                            print(str(nomejog3) + " comprou a propriedade em Barueri")
                            print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Barueri")
                elif ppr4 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade em Barueri")
                else:
                    if ppr4 == nomejog2:
                        jogador2 += 150
                        jogador3 -= 150
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$150,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr4 == nomejog1:
                        jogador1 += 150
                        jogador3 -= 150
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$150,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr4 == nomejog4:
                        jogador4 += 150
                        jogador3 -= 150
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$150,00 para o", nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))

            elif posjog3 == 8:
                print(nomejog3, ", você está de visitante na prisão!")

            elif posjog3 == 9:
                if ppr5 == "":
                    if jogador3 >= 850:
                        compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 850
                            ppr5 = nomejog3
                            print(str(nomejog3) + " comprou a propriedade em Pinheiros")
                            print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Pinheiros")
                elif ppr5 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade em Pinheiros")
                else:
                    if ppr5 == nomejog2:
                        jogador2 += 170
                        jogador3 -= 170
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$170,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr5 == nomejog1:
                        jogador1 += 170
                        jogador3 -= 170
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$170,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr5 == nomejog4:
                        jogador4 += 170
                        jogador3 -= 170
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$170,00 para o", nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))

            elif posjog3 == 10:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador3*0.1, '.2f'));
                jogador3 -= float(format(jogador3*0.1, '.2f'))
                print(str(nomejog3), "possui em conta R$", format(jogador3, '.2f'))

            elif posjog3 == 11:
                if ppr6 == "":
                    if jogador3 >= 950:
                        compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 950
                            ppr6 = nomejog3
                            print(str(nomejog3) + " comprou a propriedade na Augusta")
                            print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade na Augusta")
                elif ppr6 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade na Augusta")
                else:
                    if ppr6 == nomejog2:
                        jogador2 += 190
                        jogador3 -= 190
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$190,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr6 == nomejog1:
                        jogador1 += 190
                        jogador3 -= 190
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$190,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr6 == nomejog4:
                        jogador4 += 190
                        jogador3 -= 190
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$190,00 para o", nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))

            elif posjog3 == 12:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog3 = 8
                    presojog3 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador3 += 200

            elif posjog3 == 13:
                if emprego2 == "":
                    if jogador3 >= 2000:
                        print(str(nomejog3) + " você caiu na faculdade de Medicina, se formando você receberá R$200,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer =="S":
                            emprego2 = nomejog3
                            jogador3 -= 2000
                            print(str(nomejog3) + ", você se graduou em Medicina")
                    else:
                        print("Você não possui dinheiro suficiente para pagar pelos estudos de Medicina")
                        print("Você possui: R$", format(jogador3, '.2f'))
                        print("Para pagar a graduação em Medicina é necessário ter no mínimo R$2000,00")
                else:
                    print("Você caiu na graduação de Medicina mas ela não está mais disponível")

            elif posjog3 == 14:
                if ppr7 == "":
                    if jogador3 >= 1200:
                        compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 1200
                            ppr7 = nomejog3
                            print(str(nomejog3) + " comprou a propriedade no Jardim Paulista")
                            print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Jardim Paulista")
                elif ppr7 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade no Jardim Paulista")
                else:
                    if ppr7 == nomejog2:
                        jogador2 += 240
                        jogador3 -= 240
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$240,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr7 == nomejog1:
                        jogador1 += 240
                        jogador3 -= 240
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$240,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr7 == nomejog4:
                        jogador4 += 240
                        jogador3 -= 240
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$240,00 para o", nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))

            elif posjog3 == 15:
                if ppr8 == "":
                    if jogador3 >= 1400: 
                        compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador3 -= 1400
                            ppr8 = nomejog3
                            print(str(nomejog3), " comprou a propriedade no Brooklin")
                            print(str(nomejog3), " possui em conta R$", format(jogador3, '.2f'))
                    else:
                        print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Brooklin")
                elif ppr8 == nomejog3:
                    print(str(nomejog3) + " você já possui a propriedade no Brooklin")
                else:
                    if ppr8 == nomejog2:
                        jogador2 += 280
                        jogador3 -= 280
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$280,00 para o", nomejog2)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr8 == nomejog1:
                        jogador1 += 280
                        jogador3 -= 280
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$280,00 para o", nomejog1)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                    elif ppr8 == nomejog4:
                        jogador4 += 280
                        jogador3 -= 280
                        print(str(nomejog3) + " você teve que pagar o aluguel de R$280,00 para o", nomejog4)
                        print(str(nomejog3) + " possui em conta R$", format(jogador3, '.2f'))
                        
            if jogador3 < 0:
                    print(str(nomejog3) + " faliu, que pena!")
                    faliujog3 = True


                    
    if not faliujog4 and nomejog4 != "":
        print("\n------------------------------------------------")
        print("|                  Jogador 4                   |")
        print("------------------------------------------------")
        print("|      Formação       |        Salário         |")
        print("------------------------------------------------")
        
        if emprego1 == nomejog4:
            print("|     ENGENHEIRO      |        R$100,00        |")
        if emprego2 == nomejog4:
            print("|      MEDICINA       |        R$200,00        |")
            
        print("------------------------------------------------")
        print("|        Casas        |        Aluguel         |")
        print("------------------------------------------------")
        if ppr1 == nomejog4:
            print("|      Itaquera       |        R$80,00         |")
            print("------------------------------------------------")
        if ppr2 == nomejog4:
            print("|       Penha         |        R$100,00        |")
            print("------------------------------------------------")
        if ppr3 == nomejog4:
            print("|       Osasco        |        R$130,00        |")
            print("------------------------------------------------")
        if ppr4 == nomejog4:
            print("|       Barueri       |        R$150,00        |")
            print("------------------------------------------------")
        if ppr5 == nomejog4:
            print("|      Pinheiros      |        R$170,00        |")
            print("------------------------------------------------")
        if ppr6 == nomejog4:
            print("|       Augusta       |        R$190,00        |")
            print("------------------------------------------------")
        if ppr7 == nomejog4:
            print("|  Jardim Paulista    |        R$240,00        |")
            print("------------------------------------------------")
        if ppr8 == nomejog4:
            print("|      Brooklin       |        R$280,00        |")
            print("------------------------------------------------")
                
        if presojog4:
            tentjog4 += 1
            print("\nVocê está preso", nomejog4, "você precisa tirar abaixo de 3 para sair")
            print("Você está na tentativa:",tentjog4)
            input("Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
          
            print("Você tirou",dado)
            if dado < 3:
                print("Você saiu da prisão!")
                presojog4 = False
                tentjog4 = 0
            else:
                print("Você não tirou o número certo, tente na próxima rodada")
                if tentjog4 == 3:
                    print("\n" + str(nomejog4) + " você estourou o limite de tentativas para sair da prisão, você terá que pagar R$400,00")
                    print(str(nomejog4) + " seu saldo é R$" + format(jogador4, '.2f'))
                    jogador4 -= 400
                    presojog4 = False
                    tentjog4 = 0
                if jogador4 < 0:
                    print(nomejog4, " você faliu, que pena!")
                    faliujog4 = True
            
        else:
            print(str(nomejog4) + " você está na casa: " + str(posjog4))
            print(str(nomejog4) + " você possui em conta R$" + format(jogador4, '.2f'))
            input("\n" + str(nomejog4) + ": Aperte ENTER para jogar o dado")
            dado = random.randint(1,6)
            print("valor do dado:",dado)
            posjog4 += dado
            
            if posjog4 > 15:
                dado = posjog4 - 15
                posjog4 = dado - 1
                jogador4 += 200
                print(nomejog4, "você recebeu R$200,00 por passar no inicio")
                if emprego1 == nomejog4:
                    print(nomejog4, "você recebeu R$100,00 pelo seu salário de Engenheiro")
                    jogador4 += 100
                    print(nomejog4 + " você está com R$" + format(jogador4, '.2f'))
                elif emprego2 == nomejog4:
                    print(nomejog4 ,"você recebeu R$200,00 pelo seu salário de Médico")
                    jogador4 += 200
                    print(nomejog4 + " você está com R$" + format(jogador4, '.2f'))

            print(str(nomejog4) + " você foi para a casa: " + str(posjog4))

            if posjog4 == 1:
                if ppr1 == "":
                    if jogador4 >= 400:
                        compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Itaquera por R$400? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 400
                            ppr1 = nomejog4
                            print(str(nomejog4) + " comprou a propriedade em Itaquera")
                            print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Itaquera")
                elif ppr1 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade em Itaquera")
                else:
                    if ppr1 == nomejog2:
                        jogador2 += 80
                        jogador4 -= 80
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$80,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr1 == nomejog3:
                        jogador3 += 80
                        jogador4 -= 80
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$80,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr1 == nomejog1:
                        jogador1 += 80
                        jogador4 -= 80
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$80,00 para o",nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                        
            elif posjog4 == 2:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador4*0.1, '.2f'));
                jogador4 -= float(format(jogador4*0.1, '.2f'))
                print(nomejog4, "possui em conta R$", format(jogador4, '.2f'))
                
            elif posjog4 == 3:
                if ppr2 == "":
                    if jogador4 >= 500:
                        compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n:")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Penha por R$500? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 500
                            ppr2 = nomejog4
                            print(str(nomejog4) + " comprou a propriedade na Penha")
                            print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade na Penha")
                elif ppr2 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade na Penha")
                else:
                    if ppr2 == nomejog2:
                        jogador2 += 100
                        jogador4 -= 100
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$100,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr2 == nomejog3:
                        jogador3 += 100
                        jogador4 -= 100
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$100,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr2 == nomejog1:
                        jogador1 += 100
                        jogador4 -= 100
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$100,00 para o", nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                        
            elif posjog4 == 4:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog4 = 8
                    presojog4 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador4 += 200
                    
            elif posjog4 == 5:
                if emprego1 == "":
                    if jogador4 >= 1500:
                        print(nomejog4, "você caiu na faculdade de Engenharia, se formado você receberá R$100,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$1500,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer =="S":
                            emprego1 = nomejog4
                            jogador4 -= 1500
                            print(str(nomejog4) + ", você se graduou em Engenharia")
                    else:
                        print("Você não possui dinheiro suficiente para pegar pelos estudos de Engenharia")
                        print("Você possui: R$", format(jogador4, '.2f'))
                        print("Para pagar a graduação em Engenharia é necessário ter no mínimo R$1500,00")
                else:
                    print("Você caiu na gradução de Engenharia mas ela não está mais disponível")

            elif posjog4 == 6:
                if ppr3 == "":
                    if jogador4 >= 650:
                        compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Osasco por R$650? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 650
                            ppr3 = nomejog4
                            print(str(nomejog4) + " comprou a propriedade em Osasco")
                            print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Osasco")
                elif ppr3 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade em Osasco")
                else:
                    if ppr3 == nomejog2:
                        jogador2 += 130
                        jogador4 -= 130
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$130,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr3 == nomejog3:
                        jogador3 += 130
                        jogador4 -= 130
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$130,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr3 == nomejog1:
                        jogador1 += 130
                        jogador4 -= 130
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$130,00 para o", nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))

            elif posjog4 == 7:
                if ppr4 == "":
                    if jogador4 >= 750:
                        compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Barueri por R$750? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 750
                            ppr4 = nomejog4
                            print(str(nomejog4) + " comprou a propriedade em Barueri")
                            print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Barueri")
                elif ppr4 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade em Barueri")
                else:
                    if ppr4 == nomejog2:
                        jogador2 += 150
                        jogador4 -= 150
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$150,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr4 == nomejog3:
                        jogador3 += 150
                        jogador4 -= 150
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$150,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr4 == nomejog1:
                        jogador1 += 150
                        jogador4 -= 150
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$150,00 para o", nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))

            elif posjog4 == 8:
                print(nomejog4, ", você está de visitante na prisão!")

            elif posjog4 == 9:
                if ppr5 == "":
                    if jogador4 >= 850:
                        compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade em Pinheiros por R$850? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 850
                            ppr5 = nomejog4
                            print(str(nomejog4) + " comprou a propriedade em Pinheiros")
                            print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Pinheiros")
                elif ppr5 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade em Pinheiros")
                else:
                    if ppr5 == nomejog2:
                        jogador2 += 170
                        jogador4 -= 170
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$170,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr5 == nomejog3:
                        jogador3 += 170
                        jogador1 -= 170
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$170,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr5 == nomejog1:
                        jogador1 += 170
                        jogador4 -= 170
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$170,00 para o", nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))

            elif posjog4 == 10:
                print("Você caiu no Imposto e deve pagar 10% do valor que você possui: R$", format(jogador4*0.1, '.2f'));
                jogador4 -= float(format(jogador4*0.1, '.2f'))
                print(str(nomejog4), "possui em conta R$", format(jogador4, '.2f'))

            elif posjog4 == 11:
                if ppr6 == "":
                    if jogador4 >= 950:
                        compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade na Augusta por R$950? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 950
                            ppr6 = nomejog4
                            print(str(nomejog4) + " comprou a propriedade na Augusta")
                            print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade na Augusta")
                elif ppr6 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade na Augusta")
                else:
                    if ppr6 == nomejog2:
                        jogador2 += 190
                        jogador4 -= 190
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$190,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr6 == nomejog3:
                        jogador3 += 190
                        jogador4 -= 190
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$190,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr6 == nomejog1:
                        jogador1 += 190
                        jogador4 -= 190
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$190,00 para o", nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))

            elif posjog4 == 12:
                print("Sorte ou revés")
                sorte = random.randint(1,6)
                print("Número tirado: ", sorte)
                if sorte%2 == 0:
                    print("Você tirou um número par, irá para a prisão!")
                    posjog4 = 8
                    presojog4 = True
                else:
                    print("Você tirou um número ímpar, parabéns você ganhou R$200,00!")
                    jogador4 += 200

            elif posjog4 == 13:
                if emprego2 == "":
                    if jogador4 >= 2000:
                        print(str(nomejog4) + " você caiu na faculdade de Medicina, se formando você receberá R$200,00 por chegada ao inicio")
                        quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        while quer != "S" and quer != "s" and quer != "N" and quer != "n":
                            print("Digite uma resposta válida!")
                            quer = input("Deseja pagar R$2000,00 pelos estudos? S/s/N/n: ")
                        if quer == "s" or quer =="S":
                            emprego2 = nomejog4
                            jogador4 -= 2000
                            print(str(nomejog4) + ", você se graduou em Medicina")
                    else:
                        print("Você não possui dinheiro suficiente para pagar pelos estudos de Medicina")
                        print("Você possui: R$", format(jogador4, '.2f'))
                        print("Para pagar a graduação em Medicina é necessário ter no mínimo R$2000,00")
                else:
                    print("Você caiu na graduação de Medicina mas ela não está mais disponível")

            elif posjog4 == 14:
                if ppr7 == "":
                    if jogador4 >= 1200:
                        compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Jardim Paulista por R$1200,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 1200
                            ppr7 = nomejog4
                            print(str(nomejog4) + " comprou a propriedade no Jardim Paulista")
                            print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Jardim Paulista")
                elif ppr7 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade no Jardim Paulista")
                else:
                    if ppr7 == nomejog2:
                        jogador2 += 240
                        jogador4 -= 240
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$240,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr7 == nomejog3:
                        jogador3 += 240
                        jogador4 -= 240
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$240,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr7 == nomejog1:
                        jogador1 += 240
                        jogador4 -= 240
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$240,00 para o", nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))

            elif posjog4 == 15:
                if ppr8 == "":
                    if jogador4 >= 1400: 
                        compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        while compra != "S" and compra != "s" and compra != "N" and compra != "n":
                            print("Digite uma resposta válida")
                            compra=input("Deseja comprar a propriedade no Brooklin por R$1400,00? Digite S ou s, N ou n: ")
                        if compra == "S" or compra == "s":
                            jogador4 -= 1400
                            ppr8 = nomejog4
                            print(str(nomejog4), " comprou a propriedade no Brooklin")
                            print(str(nomejog4), " possui em conta R$", format(jogador4, '.2f'))
                    else:
                        print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Brooklin")
                elif ppr8 == nomejog4:
                    print(str(nomejog4) + " você já possui a propriedade no Brooklin")
                else:
                    if ppr8 == nomejog2:
                        jogador2 += 280
                        jogador4 -= 280
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$280,00 para o", nomejog2)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr8 == nomejog3:
                        jogador3 += 280
                        jogador4 -= 280
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$280,00 para o", nomejog3)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                    elif ppr8 == nomejog1:
                        jogador1 += 280
                        jogador4 -= 280
                        print(str(nomejog4) + " você teve que pagar o aluguel de R$280,00 para o", nomejog1)
                        print(str(nomejog4) + " possui em conta R$", format(jogador4, '.2f'))
                        
            if jogador4 < 0:
                    print(str(nomejog4) + " faliu, que pena!")
                    faliujog4 = True
                    

if(not faliujog1):
    print("\nPARABÉNS " + str(nomejog1) + ", VOCÊ GANHOU O JOGO !!!")
elif(not faliujog2):
    print("\nPARABÉNS " + str(nomejog2) + ", VOCÊ GANHOU O JOGO !!!")
elif(not faliujog3):
    print("\nPARABÉNS " + str(nomejog3) + ", VOCÊ GANHOU O JOGO !!!")
elif(not faliujog4):
    print("\nPARABÉNS " + str(nomejog4) + ", VOCÊ GANHOU O JOGO !!!")
