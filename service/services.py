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
        registros: list = self.repository.find_all()

        sessoes: list[Entity] = []
        for s in map(lambda r: Entity(r[0], r[1], r[2], r[3]), registros):
            sessoes.append(s)

        return sessoes

    def get(self, sessao_id: int):
        if sessao_id is None or sessao_id <= 0 or not isinstance(sessao_id, int):
            raise Exception("id invalido")

        s = self.repository.find_by_id(sessao_id)
        sessao = Entity(s[0], s[1], s[2], s[3])

        return sessao

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass