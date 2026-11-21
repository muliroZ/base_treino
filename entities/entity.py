class Entity:
    def __init__(self, sessao_id: int | None = None, nome: str = "", capacidade: str = "", em_andamento: bool = False):
        self.id = sessao_id
        self.nome = nome
        self.capacidade = capacidade
        self.em_andamento = em_andamento

    def __repr__(self) -> str:
        return f"Id: {self.id}\nNome: {self.nome}\nCapacidade: {self.capacidade}\nEm andamento?: {'Sim' if self.em_andamento else 'Não'}"