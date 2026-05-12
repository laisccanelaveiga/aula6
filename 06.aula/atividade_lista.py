# 10 vendedores - qtd vendas realizadas - valor de cada venda efetuada 
# total vendido e a média das vendas por vendedor
# analisar resultado meta mínima 1000 abaixo da meta 700
media_vendas = []
total_vendas = []

for i in range (2):
    print(f'\nVendedor {i + 1}')
    qtd_vendas = int(input("Qual a quantidade de vendas deste vendedor: "))
    vendas = []
    
    for venda in range(qtd_vendas):
        vlr_venda = float(input(f"Qual o valor da venda {venda + 1}: "))
        vendas.append(vlr_venda)

    total = sum(vendas)
    media = total / qtd_vendas

    total_vendas.append(total)
    media_vendas.append(media)

META = 1000
META_MINIMA = 700



print("\nResultado")
for i, media in enumerate(media_vendas):
    print(f'\nVendedor {i+1} vendeu {total_vendas[i]}')
    print(f'Média das vendas {media}')

    if media >= META:
        print(f'Meta de R$ {META} atingida')
    elif media >= META_MINIMA:
        print(f'Atingiu a meta mínima R$ {META_MINIMA}')
    else:
        print("Abaixo da meta")
print()
    


        
