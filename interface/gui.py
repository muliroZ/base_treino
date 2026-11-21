from service.services import Services

class UI:

    def __init__(self, services: Services):
        self.services = services

    def show_principal_menu(self):
        # Exibir opções
        # Receber escolha do usuário
        # Chamar os métodos do service
        print("""
        Sessoes:
        1. criar sessao
        2. listar sessoes
        3. buscar sessao (por id)
        4. atualizar sessao
        5. excluir sessao
        """)

        opc = int(input("escolha (1-5): "))
        match opc:
            case 1:
                nome = input("insira o nome: ")
                cap = int(input("insira a capacidade: "))

                self.services.create(nome, cap)

            case 2:
                sessoes = self.services.list()

                print("=" * 50 + "\nSessoes:\n" + "=" * 50)
                if len(sessoes) == 0:
                    print("Sem sessões cadastradas")
                    return

                for s in sessoes:
                    print(f"{s}\n")
                print("=" * 50)