import sqlite3

# Realiza conexão com o banco de dados e cria um arquivo se não tiver
con = sqlite3.connect("tutorial.db")

# Cria um cursor que serve como uma ponte entre o banco de dados e o código, permitindo realizar interações
cur = con.cursor()

# Com a função cur.execute conseguimos executar as interações com o banco de dados, como criar tabelas, adicionar, deletar, editar e atualizar dados.
# Comandos como criar uma tabela devem ser usados apenas uma vez para não gerar erro nas próximas execuções
# cur.execute("CREATE TABLE movie(title, year, score)")

# Criando uma variável result podemos executar uma consulta para verificar os nomes das tabelas dentro do banco de dados e usando um loop for podemos iterar e acessar cada nome
result = cur.execute("SELECT name FROM sqlite_master")
for resultado in result:
    print(resultado)

# Abaixo, temos um simples comando para adicionar dados a tabela movie.
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5),
        ('How I was before you', 2010, 8.5)
""")

# Os dados também podem ser armazenados em uma lista de tuplas e inseridos no banco de dados com o método executemany()
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

# O metódo executemany executa várias vezes o comando execute, o que é mais eficiente. Os ? ? ? é cada valor da tupla que será substituido.
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)

# Esse comando é fundamental para as alterações serem salvas no banco de dados
con.commit()

# Agora, podemos armazenar o resultado com uma váriável, usando um consulta SELECT *.
rows = cur.execute("SELECT * FROM movie")

# Loop para exibir cada item na tabela
for row in rows:
    print(row)

