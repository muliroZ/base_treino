from repository.dao_entity import DAOEntity
from entities.entity import Entity

class Services:

    def __init__(self, repository: DAOEntity):
        self.repository = repository

    def create(self, nome: str, capacidade: int | None):
        # Validar dados (MUITO IMPORTANTE!!!!!)
        # Criar entidade
        # Solicitar persistência
        if len(nome.strip()) == 0 or nome is None:
            raise Exception("nome obrigatorio")

        try:
            sessao = Entity(nome=nome, capacidade=capacidade)
            sessao_id = self.repository.create(sessao)

            print("operacao bem-sucedida")
            print(f"id da sessao: #{sessao_id}")
        except Exception:
            print("operacao falhou")
            raise

    def list(self):
        pass

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass