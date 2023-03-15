from Herança import Mae, Filha, Neta

print('Criando objeto de Mae...')
mae = Mae(1)

print('\nCriando objeto de Filha...')
filha = Filha(1,2)

print('\nCriando objeto de Neta...')
neta = Neta(1,2,3)


print('\nVisualizando os objetos')
print(f'Mãe:{vars(mae)}\nFilha:{vars(filha)}\nNeta:{vars(neta)}')
