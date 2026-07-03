'''
Um bloco de Comentarios
Para explicar o que o código faz, ou para deixar anotações para o programador.
>>projeto barbearia:

>PO (Como dono do negocio: Quero um sistema de agendamento de horários para cortar o cabelo, fazer a barba e
sombrancelha de meus clientes, diferenciando cada um dos pedidos e armazenando seus dados.)

>QA (Como cliente: Quero um sistema de agendamento de horários, para que eu possa agendar meus horários
disponíveis de forma rápida e fácil)
 
 >Tech (Como programador: Quero um sistema de agendamento de horários para minha barbearia, para que eu possa
 desenvolver um software eficiente e funcional para o negócio.)
 
 >Dev (Como programador: Quero um sistema de agendamento de horários para minha barbearia, para que eu possa
 implementar as funcionalidades necessárias para atender as necessidades do negócio e dos clientes.)

 >UX (Como designer de experiência do usuário: Quero um sistema de agendamento de horários para minha barbearia,
 para que eu possa criar uma interface intuitiva e agradável para os usuários, garantindo uma experiência de
 agendamento satisfatório.)

 >IA (Como analista de dados: Quero um sistema de agendamento de horários para minha barbearia, para que eu possa
 coletar e analisar os dados armazenados, ajudando a identificar um padrão de cada cliente e otimizar as estratégias de marketing.)

 # Isso é um comentário de linha única
 print('Olá, Mundo!')

'''


print('\n----------------------------------\n')
print('Bem-vindo ao projeto de desenvolvimento de um sistema de agendamentos de horários para uma barbearia!\n')
print('1 - Selecionar sua necessidade')
print('2 - Escolher seu melhor horário')
print('3 - Realizar agendamento')
print('0 - sair')
print('\n--------------------------------------------------\n')

opcao = input('Digite a opção desejada:')

~print('\n----------------------------------\n')
if opcao == '1':
    print('Opção 1 - Selecionar sua necessidade')
elif opcao == '2':
    print('Opção 2 - Escolher seu melhor horário')
elif opcao == '3':
    print('Opção 3 - Realizar agendamento')
elif opcao == '0':
    print ('Opção 0 - sair')
    # break

else:
    print('Opção inválida')               