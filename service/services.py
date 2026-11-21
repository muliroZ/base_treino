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

    def update(self, sessao_id, nome: str, capacidade: int):
        if nome.strip() == "" or nome is None:
            raise Exception("nome invalido")

        if capacidade <= 0 and capacidade is not None:
            raise Exception("capacidade invalida")

        sessao = Entity(sessao_id, nome, capacidade, None)
        return self.repository.update(sessao)

    def delete(self, sessao_id):
        if self.repository.find_by_id(sessao_id) is None:
            return "sessao nao existe"

        try:
            self.repository.delete(sessao_id)
            return "excluido com sucesso"
        except Exception:
            return "erro ao exluir"

    def alterar_andamento(self, sessao_id, fechar=False):
        if self.repository.find_by_id(sessao_id) is None:
            return "sessao nao existe"

        try:
            self.repository.alterar_andamento(sessao_id, fechar)
            return f"alterado com sucesso => sessao {sessao_id} {"em andamento" if not fechar else "fechada"}"
        except Exception:
            return "erro na operacao"