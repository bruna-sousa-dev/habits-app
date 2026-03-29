import flet as ft


class App:
    def __init__(self, page: ft.Page) -> None:
        # Guarda a referência da página principal do Flet
        self.page = page

        # Define o título da janela/aplicação
        self.page.title = "Habits App"

        # Remove o padding padrão da página
        self.page.padding = 0

        # Define a cor de fundo base da página
        self.page.bgcolor = ft.Colors.BLACK

        # Chama o método principal que monta toda a interface
        self.main()

    def main(self):
        # =========================
        # ESTADO DA APLICAÇÃO
        # =========================
        # Lista principal de hábitos.
        # Cada hábito é representado por um dicionário com:
        # - title: nome do hábito
        # - done: se o hábito foi concluído ou não
        habits_list = [
            {"title": "Estudar Python", "done": False},
        ]

        # =========================
        # COMPONENTES DE PROGRESSO
        # =========================
        # Texto que exibirá o percentual de progresso
        progress_text = ft.Text("0%", size=50, color=ft.Colors.WHITE)

        # Barra de progresso visual
        progress_bar = ft.ProgressBar(
            value=0,  # valor inicial
            color=ft.Colors.AMBER_900,   # cor da barra preenchida
            bgcolor=ft.Colors.AMBER_100, # cor do fundo da barra
            height=20,
        )

        # =========================
        # FUNÇÃO: change
        # =========================
        # Responsável por:
        # 1. Atualizar o estado de um hábito ao marcar/desmarcar o checkbox
        # 2. Recalcular o progresso total
        # 3. Atualizar os componentes visuais de progresso
        def change(e=None):
            # Se a função foi chamada por um evento de checkbox,
            # atualiza o item correspondente na lista de hábitos
            if e:
                for hl in habits_list:
                    if hl["title"] == e.control.label:
                        hl["done"] = e.control.value

            # Filtra apenas os hábitos concluídos
            done = [item for item in habits_list if item["done"]]

            # Calcula o percentual de progresso
            # O "if habits_list else 0" evita divisão por zero
            total = len(done) / len(habits_list) if habits_list else 0

            # Atualiza a barra de progresso
            progress_bar.value = round(total, 2)

            # Atualiza o texto percentual
            progress_text.value = f"{total:.0%}"

            # Atualiza a página para refletir as mudanças na interface
            self.page.update()

        # =========================
        # FUNÇÃO: rebuild_habits
        # =========================
        # Reconstrói a lista de checkboxes com base no estado atual.
        # Sempre que um novo hábito for adicionado, essa função é usada
        # para redesenhar a área dos hábitos.
        def rebuild_habits():
            habits.content.controls = [
                ft.Checkbox(
                    label=hl["title"],   # nome do hábito
                    value=hl["done"],    # status atual
                    on_change=change,    # função chamada ao marcar/desmarcar
                )
                for hl in habits_list
            ]

        # =========================
        # FUNÇÃO: add_habit
        # =========================
        # Adiciona um novo hábito digitado pelo usuário.
        def add_habit(e):
            # Obtém o texto digitado e remove espaços extras
            value = (e.control.value or "").strip()

            # Se estiver vazio, não adiciona nada
            if not value:
                return

            # Adiciona um novo hábito com status inicial False
            habits_list.append({"title": value, "done": False})

            # Reconstrói a lista de checkboxes
            rebuild_habits()

            # Limpa o campo de texto
            e.control.value = ""

            # Recalcula o progresso e atualiza a tela
            change()

        # =========================
        # LAYOUT PRINCIPAL DA TELA
        # =========================
        # A coluna organiza os elementos verticalmente
        coluna = ft.Column(
            spacing=0,
            expand=True,
            controls=[
                # Título principal da tela
                ft.Text(
                    value="Que bom ter você aqui",
                    size=24,
                    color=ft.Colors.WHITE,
                ),

                # Subtítulo
                ft.Text(
                    value="Como estão seus hábitos hoje",
                    size=16,
                    color=ft.Colors.GREY,
                ),

                # =========================
                # CARD DE PROGRESSO
                # =========================
                ft.Container(
                    padding=30,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.CENTER_LEFT,
                        end=ft.Alignment.CENTER_RIGHT,
                        colors=["#991b1b", "#ca8a04", "#eab308"],
                        stops=[0, 0.9, 1],
                    ),
                    border_radius=20,
                    margin=ft.margin.symmetric(vertical=10),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="Sua evolução hoje",
                                size=16,
                                color=ft.Colors.WHITE,
                            ),
                            progress_text,  # texto percentual
                            progress_bar,   # barra de progresso
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),

                # Título da seção de hábitos
                ft.Text(
                    value="Hábitos de hoje",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),

                # Texto auxiliar
                ft.Text(
                    value="Marcar suas tarefas como concluído te motiva a ficar focado",
                    size=12,
                    color=ft.Colors.WHITE,
                ),

                # =========================
                # ÁREA DOS HÁBITOS
                # =========================
                # Container que receberá dinamicamente os checkboxes
                (habits := ft.Container(
                    expand=True,
                    padding=30,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.CENTER_LEFT,
                        end=ft.Alignment.CENTER_RIGHT,
                        colors=["#991b1b", "#ca8a04", "#eab308"],
                        stops=[0, 0.9, 1],
                    ),
                    border_radius=20,
                    margin=ft.margin.symmetric(vertical=20),
                    content=ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.ALWAYS,
                        spacing=10,
                        controls=[],  # começa vazio e será preenchido por rebuild_habits()
                    ),
                )),

                # Título da área de adicionar novo hábito
                ft.Text(
                    value="Adicionar novo hábito",
                    size=16,
                    color=ft.Colors.WHITE,
                ),

                # Campo de texto para adicionar um novo hábito
                ft.TextField(
                    hint_text="Escreva um hábito...",
                    border=ft.InputBorder.UNDERLINE,
                    on_submit=add_habit,  # chama add_habit ao pressionar Enter
                ),
            ],
        )

        # Monta inicialmente a lista de hábitos na interface
        rebuild_habits()

        # Calcula e exibe o progresso inicial
        change()

        # =========================
        # CONTAINER FINAL DA TELA
        # =========================
        # Esse container aplica espaçamento e gradiente de fundo
        layout = ft.Container(
            content=coluna,
            expand=True,
            padding=ft.padding.symmetric(horizontal=20, vertical=60),
            gradient=ft.LinearGradient(
                begin=ft.Alignment.CENTER_LEFT,
                end=ft.Alignment.CENTER_RIGHT,
                colors=["#374151", "#111827", "#000000"],
                stops=[0, 0.5, 1],
            ),
        )

        # Adiciona o layout final na página
        self.page.add(layout)


# Função principal exigida pelo Flet
def main(page: ft.Page):
    App(page)


# Ponto de entrada da aplicação
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
