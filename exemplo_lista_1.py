numeros = [1, 2, 3, 4, 5]
nomes = ['joaquim', 'maria', 'ana', 'brenda', 'sofia,' 'bruna']

print(numeros)
print(nomes)

print(nomes[0]) # acesse o primeiro da lista
print(nomes[1]) # acesse o primeiro da lista
print(nomes[2]) # acesse o primeiro da lista

nomes[0] = "joao" # estava joaquim
 
print(nomes [0])
print(nomes [1])
print(nomes [2])

nomes[1] = "maria" 

print(nomes [1])
print(nomes [2])
print(nomes [3])
print(nomes [4])
print(nomes [5])

nomes[2] = "ana"

print(nomes [3])
print(nomes [4])
print(nomes [5])

nomes[3] = "brenda"

print(nomes [4]) 
print(nomes [5])

nomes[4] = 'sofia'

print(nomes [5])

nomes[5] = 'bruna'

# Removendo elementos
del nomes[3] # Remove o elemento no indice 3
print("após del:", nomes)

nomes.remove("maria") # Remove a primeira ocorrencia de "maria"
print("apos remove:, nomes")

removido = nomes.pop(2) # Remove e retorna o elemento no indice 2
print (f"Apos pop removido  ('[removido])'):", nomes)

nomes.clear() # Esvazia a lista
print("apos clear:", nomes)