# Um professor precisa organizar rapidamente o resultado final de seus alunos após duas avaliações.
# Para isso é preciso desenvolver um programa, que registre as notas de 4 provas para 15 estudantes e calcule a média de cada um. 

# Ao final, o sistema deve apresentar o resultado individual de cada estudante, 
# informando a média obtida e se ele foi aprovado ou reprovado, considerando média mínima de 7,0 para aprovação. 


# Armazenar as médias dos estudantes em uma lista. 

# Calcular a média de cada estudante. 

# Verificar se a média é maior igual a 7 (aprovado ou reprovado). 

# Exibir os resultados para cada estudante. 

medias = []
contador = 0

for i in range(15):
    notas = []
    contador += 1

    for nota in range(4):
        entrada_notas = float(input(f"Insira a nota {nota + 1}: "))
        notas.append(entrada_notas)
         
    media = sum(notas) / 4
    medias.append(media)

    print("\n=====Resultado=====")
    print(f'Aluno {contador} | Média {media}')

    if media >= 7:
        print("Aprovado\n")
    else:
        print("Reprovado\n")
    
    print()

print(medias)    

