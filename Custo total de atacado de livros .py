#Inserindo variáveis

valor_da_capa_do_livro = float(input('Digite o valor  da capa: ')) 
desconto_do_livro = float(input('Digite o valor  o valor do desconto: ')) 
frete_do_livro = float(input('Digite o valor  do frete: ')) 
numero_de_exemplares = float(input('Digite o valor  do numero de exemplares: ')) 

#Inserindo fórmula

custo_total = (valor_da_capa_do_livro*(desconto_do_livro/100)) + (frete_do_livro*numero_de_exemplares+0.75)

#Imprimindo Custo total

print(f'o valor do custo total é : {custo_total} R$')