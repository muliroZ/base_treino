from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessao (
                sessao_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR UNIQUE NOT NULL,
                capacidade INTEGER NULL,
                em_andamento BOOLEAN DEFAULT FALSE
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM sessao")

        if cursor.fetchone()[0] == 0:
            cursor.executemany("""
                INSERT INTO sessao (nome, capacidade, em_andamento)
                VALUES (?, ?, ?)
            """, [
                ("sala-vingadores", 60, False),
                ("sala-interestelar", 40, True),
                ("sala-avatar", 50, False)
            ])

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")