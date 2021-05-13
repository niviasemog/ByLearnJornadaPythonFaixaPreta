# ByLearnJornadaPythonFaixaPreta
eu fiz o código sobre o horario e clima


horario = 'manha'
clima = 'chuvoso'
temperatura = 'ensolarado'

if horario == 'manhã' or horario == 'tarde':
   if clima == 'ensolarado' and temperatura == 'quente':
       print('Uma piscina cairia bem')

   if (clima == 'ensolarado' or clima == 'nublado') and (temperatura == 'amena' or temperatura == 'frio'):
       print('Será legal praticar algum esporte')

   if clima == 'chuvoso':
       print('Aproveite para treinar seu Python')
else:
    if clima == 'chuvoso':
        print('Que tal um filme, série ou jogatina?')
    else:
      print('Um jantar fora parece interessante...')   
