"""
	Faculdade: IPESU/FAREC
	Curso: Bacharelado em Ciência da Computação
	Disciplina: Paradigmas de Linguagens
	Professor: Tennyson Accetti Resende Filho	
	Período/Turno: 2º e 3º/Noite
	Grupo: Arthur Yure dos Santos, Josuel Soares da Silva e Matheus Johann Araújo	
"""

print("\n SELECIONE O SGBD")
print("\n> Digite 1 para usar o SQLite")
print("\n> Digite 2 para usar o MySQL")
sgbd = int(input("\n> Opção: "))
if(sgbd == 1):
	def conexaoBanco():
		try:
			import sqlite3
			conexao = sqlite3.connect("meubanco.sqlite")
		except:
			print("\n > Erro na conexão com o banco de dados!")
			return false
		else:
			print("\n > Conexão com banco de dados efetuada com sucesso!")
			return conexao		

	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS `cliente` (`cpf` CHAR(11) PRIMARY KEY, `nome` TEXT NOT NULL, `rua` TEXT NOT NULL, `cidade` TEXT NOT NULL)")
		cursor.execute("CREATE TABLE IF NOT EXISTS `conta` (`cpf` CHAR(11) PRIMARY KEY, `tipo` CHAR(3) NOT NULL, `valor` TEXT NOT NULL)")
	except:
		print("\n > Banco e tabela - Erro")
	else:
		print("\n > Banco e tabela - OK")
	finally:
		conexao.close()
	
elif(sgbd == 2):
	def conexaoBanco():
		try:
			#pip install pymysql
			import pymysql
			conexao = pymysql.connect("localhost", "root", "")
		except:
			print("\n > Erro na conexão com o banco de dados!")
			return false
		else:
			print("\n > Conexão com banco de dados efetuada com sucesso!")
			return conexao		

	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("CREATE DATABASE IF NOT EXISTS `meubanco`")
		cursor.execute("USE `meubanco`")
		cursor.execute("CREATE TABLE IF NOT EXISTS `cliente` (`cpf` CHAR(11) PRIMARY KEY, `nome` TEXT NOT NULL, `rua` TEXT NOT NULL, `cidade` TEXT NOT NULL)")
		cursor.execute("CREATE TABLE IF NOT EXISTS `conta` (`cpf` CHAR(11) PRIMARY KEY, `tipo` CHAR(3) NOT NULL, `valor` TEXT NOT NULL)")
	except:
		print("\n > Banco e tabela - Erro")
	else:
		print("\n > Banco e tabela - OK")
	finally:
		conexao.close()

else:
	import sys
	sys.exit(0)
	
def insertCliente(cpf, nome, rua, cidade):
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("INSERT INTO `cliente` VALUES ('" + cpf + "','" + nome + "','" + rua + "','" + cidade + "')")
		conexao.commit()
	except:
		print("\n > Erro ao efetuar cadastro de cliente!")
	else:
		print("\n > Cliente cadastrado com sucesso!")
	finally:
		conexao.close()
		
def insertConta(cpf, tipo, valor):
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("INSERT INTO `conta` VALUES ('" + cpf + "','" + tipo + "','" + valor + "')")
		conexao.commit()
	except:
		print("\n > Erro ao efetuar cadastro de conta!")
	else:
		print("\n > Conta cadastrada com sucesso!")
	finally:
		conexao.close()
		
def updateCliente(cpf, nome, rua, cidade):
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("UPDATE `cliente` SET `nome` = '" + nome + "', `rua` = '" + rua + "', `cidade` = '" + cidade + "' WHERE `cpf` = '" + cpf + "'")
		conexao.commit()
	except:
		print("\n > Erro na atualização do cadastro de cliente!")
	else:
		print("\n > Atualização cadastral de cliente efetuada com sucesso!")       
	finally:
		conexao.close()
		
def updateConta(cpf, tipo, valor):
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("UPDATE `conta` SET `tipo` = '" + tipo + "', `valor` = '" + valor + "' WHERE `cpf` = '" + cpf + "'")
		conexao.commit()
	except:
		print("\n > Erro na atualização do cadastro da conta!")
	else:
		print("\n > Atualização cadastral da conta efetuada com sucesso!")
	finally:
		conexao.close()
		
def deleteCliente(cpf):
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("DELETE FROM `cliente` WHERE `cpf` = '" + cpf + "'")
		conexao.commit()
	except:
		print("\n > Erro ao deletar cliente!")
	else:
		print("\n > Cliente deletado com sucesso!")
	finally:
		conexao.close()
		
def deleteConta(cpf):
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("DELETE FROM `conta` WHERE `cpf` = '" + cpf + "'")
		conexao.commit()
	except:
		print("\n > Erro ao deletar conta!")
	else:
		print("\n > Conta deletada com sucesso!")
	finally:
		conexao.close()

def selectCliente(cpf):
	contador = 0
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("SELECT * FROM `cliente` WHERE `cpf` = '" + cpf + "'")
		for row in cursor.fetchall():
			print("\n Cliente: " + str(row))
			contador += 1
	except:
		print("\n > Erro ao listar cliente!")
	finally:
		conexao.close()
	if contador == 0:
		print("\n > CPF não encontrado!")
    
def selectConta(cpf):
	contador = 0
	try:
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("SELECT * FROM `conta` WHERE `cpf` = '" + cpf + "'")
		for row in cursor.fetchall():
			print("\n Conta: " + str(row))
			contador += 1
	except:
		print("\n > Erro ao listar conta!")
	finally:
		conexao.close()
	if contador == 0:
		print("\n > CPF não encontrado!")

def selectClientesContas():
	contador = 0
	try:
		print("\n Clientes e Contas:")
		conexao = conexaoBanco()
		cursor = conexao.cursor()
		cursor.execute("SELECT * FROM `cliente`")
		for row in cursor.fetchall():
		    print("\n Cliente: " + str(row))
		    contador += 1
		cursor.execute("SELECT * FROM `conta`")
		for row in cursor.fetchall():
		    print("\n Conta: " + str(row))
		    contador += 1
	except:
		print("\n > Erro ao listar clientes e contas")
	finally:
		conexao.close()
	if contador == 0:
		print("\n > Não foi encontrado clientes e contas")
	elif contador >= 1:
		print("\n > Fim da lista!")

while(1 > 0):
    print("\n Cadastrar dados do cliente -----------> 0")
    print(" Cadastrar dados da conta -------------> 1")
    print(" Atualizar dados de cliente -----------> 2")
    print(" Atualizar dados da conta -------------> 3")
    print(" Deletar dados do cliente -------------> 4")
    print(" Deletar dados da conta ---------------> 5")
    print(" Listar dados do cliente --------------> 6")
    print(" Listar dados da conta ----------------> 7")
    print(" Listar dados do cliente e da conta ---> 8")
    print(" Listar clientes e contas -------------> 9")
    
    opcao = int(input(" Opção: "))

    if opcao == 0:
        print("\n Cadastrar cliente:\n")
        cpf = str(input(" Informe o CPF: "))
        nome = str(input(" Informe o nome do cliente: "))
        rua = str(input(" Informe a rua do cliente: "))
        cidade = str(input(" Informe a cidade do cliente: "))
       	insertCliente(cpf, nome, rua, cidade)

    elif opcao == 1:
        print("\n Cadastrar conta:\n")
        cpf = str(int(input(" Informe o CPF: ")))
        print(" Conta Corrente --------> 001")
        print(" Conta Poupança --------> 002")
        tipo = str(input(" Informe o tipo da conta: "))
        valor = str(float(input(" Informe o valor na conta: ")))
        insertConta(cpf, tipo, valor)
            
    elif opcao == 2:
    	print("\n Atualizar dados do cliente:\n")
    	cpf = str(int(input(" Informe o CPF: ")))
    	nome = str(input(" Informe o nome do cliente: "))
    	rua = str(input(" Informe a rua do cliente: "))
    	cidade = str(input(" Informe a cidade do cliente: "))
    	updateCliente(cpf, nome, rua, cidade)

    elif opcao == 3:
    	print("\n Atualizar dados da conta:\n")
    	cpf = str(int(input(" Informe o CPF: ")))
    	print(" Conta Corrente ---------> 001")
    	print(" Conta Poupança ---------> 002")
    	tipo = str(input(" Informe o tipo da conta: "))
    	valor = str(float(input(" Informe o valor na conta: ")))
    	updateConta(cpf, tipo, valor)

    elif opcao == 4:
    	print("\n Deletar dados do cliente:\n")
    	cpf = str(int(input(" Informe o CPF: ")))
    	deleteCliente(cpf)

    elif opcao == 5:
    	print("\n Deletar dados de conta:\n")
    	cpf = str(int(input(" Informe o CPF: ")))
    	deleteConta(cpf)

    elif opcao == 6:
    	print("\n Listar dados do cliente:\n")
    	cpf = str(int(input(" Informe o CPF: ")))
    	selectCliente(cpf)

    elif opcao == 7:
    	print("\n Listar dados da conta:\n")
    	cpf = str(int(input(" Informe o CPF: ")))
    	selectConta(cpf)

    elif opcao == 8:
    	print("\n Listar dados do cliente e da conta:\n")
    	cpf = str(int(input(" Informe o CPF: ")))
    	selectCliente(cpf)
    	selectConta(cpf)

    elif opcao == 9:
    	selectClientesContas()