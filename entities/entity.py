class Entity:
    def __init__(self, sessao_id: int | None = None, nome: str = "", capacidade: str = "", em_andamento: bool = False):
        self.id = sessao_id
        self.nome = nome
        self.capacidade = capacidade
        self.em_andamento = em_andamento
