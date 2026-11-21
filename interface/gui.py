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
        6. alterar andamento
        """)

        opc = int(input("escolha (1-6): "))
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

            case 3:
                sessao_id = int(input("insira o id: "))
                sessao = self.services.get(sessao_id)

                print("=" * 50 + "\nSessão:\n" + "=" * 50)
                if sessao is None:
                    print("Sem sessões com esse ID")
                else:
                    print(sessao)
                print("=" * 50)

            case 4:
                sessao_id = int(input("insira o id da sessao: "))

                nome = input("insira o novo nome (enter para pular): ")
                cap = input("insira a nova capacidade (enter para pular): ")

                try:
                    if self.services.update(sessao_id, nome, int(cap) if cap != "" else None):
                        print("atualizado com sucesso")
                    else:
                        print("sessao nao existe")
                except Exception:
                    print("nao atualizado")

            case 5:
                sessao_id = int(input("insira o id da sessao: "))

                confirmacao = True if input("confirma? (s/N): ").lower() == "s" else False
                if confirmacao:
                    print(self.services.delete(sessao_id))
                else:
                    print("operacao cancelada.")

            case 6:
                sessao_id = int(input("insira o id da sessao: "))
                opc = input("para abrir a sessao, digite 'S', para fechar, digite 'n' (S/n): ").lower()

                if opc == "n":
                    resultado = self.services.alterar_andamento(sessao_id, True)
                    print(resultado)
                else:
                    resultado = self.services.alterar_andamento(sessao_id, False)
                    print(resultado)
