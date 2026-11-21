from database.connection import get_connection
from entities.entity import Entity

class DAOEntity:
    def __init__(self):
        self.conn = get_connection()

    def create(self, sessao: Entity) -> int:
        # Inserir no banco
        try:
            cursor = self.conn.cursor()

            cursor.execute(f"""
                INSERT INTO sessao (nome, capacidade)
                VALUES ('{sessao.nome}', {sessao.capacidade});
            """)

            cursor.execute(f"SELECT sessao_id FROM sessao WHERE nome = '{sessao.nome}';")
            sessao_id = cursor.fetchone()[0]

            self.conn.commit()
            return sessao_id

        except Exception:
            self.conn.rollback()

        finally:
            self.conn.close()

    def find_all(self):
        # Consultar todas as entidades
        try:
            cursor = self.conn.cursor()

            cursor.execute("SELECT * FROM sessao")
            registros = cursor.fetchall()

            return registros

        except Exception:
            raise

    def find_by_id(self, task_id):
        # Consultar pelo ID
        pass

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass