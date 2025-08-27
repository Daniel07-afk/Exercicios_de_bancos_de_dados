import sqlite3

#Criamos a conexao com o banco e guardamos na variavel 'Banco'
banco = sqlite3.connect('loja.db')

#Criamos a variavel cursos e colocamos em uma variavel 
cursor = banco.cursor()

#enviando os dados
banco.commit()

#printar a informação
cursor.execute('SELECT preco_unitario FROM vendas WHERE preco_unitario > 50')
print(cursor.fetchall())
