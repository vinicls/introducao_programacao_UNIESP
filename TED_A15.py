#TED AULA 15

control = 1
dados = dict()

while control != 0:
    print ('-' *50)
    print ("1 - Cadastrar Funcionário")
    print ("2 - Alterar Funcionário")
    print ("3 - Listar todos os Funcionários") # IMPRIMIR
    print ("4 - Excluir um Funcionário")
    print ("5 - Adicionar um aumento de salário")
    print ("0 - Sair")
    print ('-' *300)
    control = int(input("Digite a opção: "))

#Cadastros
    if control == 1:

        dados_auxiliar = {}

        dados_auxiliar['codigo'] = int(input("Qual o seu código : "))
        dados_auxiliar['nome'] = str(input("Qual o seu nome: "))
        dados_auxiliar['email'] = input("Qual o seu email: ")  
        dados_auxiliar['data'] = str(input("Qual a data de admissão: "))
        dados_auxiliar['salario'] = int(input("Qual o seu salário: "))
        print("Cadastro executado com sucesso")
        dados.update(dados_auxiliar)
        
      
#Alterar funcionario
    # if control == 2:


# listar Funcionário
    elif control == 3:
        
        if dados is None:
            
            print("Não temos registros")
        
        else: 
            print(dados)


# apagar funcionário
    if control == 4:
        func = int(input("Digite o código do Funcionário que dejeja deletar: "))
        del(dados[int(func)])


print("FIM")
