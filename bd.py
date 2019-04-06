def get_nome(cursor,nome):
    cursor.execute(f'select nome from professor where nome = "{nome}')

    nome= cursos.fetchone()

    cursor.close()

    return nome[0]

def get_detalhes(cursor):
    cursor.execute(f'select nome,nomemae,datanasc,titulacao from professor')

    detalhes=cursor.fetchall()

    cursor.close

    return detalhes
