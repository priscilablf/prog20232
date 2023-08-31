listaInterna = ["lista",1]
compras = ["priscila", 1234, 1.2, listaInterna, 122]
print(compras[3][1]) #elemento 1 dentro do 3
compras[3]= 51 #substituiu o elemento 3 (de listaInterna para 51)
print(compras[0:len(compras):2]) #len significa considerar o tamanho inteiro da lista


