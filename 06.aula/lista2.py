lista_produtos = ['Noteboks', 'Mouse', 'Teclado', 'Monitor']
print(lista_produtos)

lista_produtos[0] = 'PC' #altera na posição
print(lista_produtos)

lista_produtos.append("WebCam") #adiciona no final
print(lista_produtos)

lista_produtos.insert(2, "Headset") #altera onde eu quero
print(lista_produtos)

lista_produtos.pop() #remove o último
print(lista_produtos)

lista_produtos.remove("Mouse") #remove o que vc quiser
print(lista_produtos)

lista_produtos.clear() #limpa toda a lista
print(lista_produtos)

# del lista_produtos[0] não é método da lista
# print(lista_produtos)