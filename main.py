import flet as ft

class App:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = 'Habits App'
        self.page.padding = ft.padding.all(30)
        self.page.bgcolor = ft.colors.BLACK
        self.main()

    def main(self):

        def change(e = None):
            if e:
                for hl in habits_list:
                    if hl['title'] == e.control.label:
                        hl['done'] = e.control.value
            
            done = list(filter(lambda x: x['done'], habits_list))
            total = len(done) / len(habits_list)
            progress_bar.value = round(total, 2)
            progress_text.value = f'{total:.0%}'
            progress_bar.update()
            progress_text.update()
        
        def add_habit(e):
            habits_list.append({'title': e.control.value, 'done': False})
            habits.content.controls = [
                ft.Checkbox(
                    label = hl['title'], 
                    value = hl['done'], 
                    on_change = change) 
                    for hl in habits_list
            ]
            habits.update()
            e.control.value = ''
            e.control.update()
            change()

        habits_list = [
            {'title': 'Estudar Python', 'done': False},
            {'title': 'Praticar Html', 'done': False},
            {'title': 'Estudar Css', 'done': False},
            {'title': 'Estudar Js', 'done': False},
        ]

        layout = ft.Column(
            spacing = 0,
            expand = True,
            controls = [
                ft.Text(value = 'Que bom ter você aqui', size = 24, color = ft.colors.WHITE),
                ft.Text(value = 'Como estão seus hábitos hoje', size = 16, color = ft.colors.GREY),
                
                ft.Container(
                    padding = ft.padding.all(30),
                    bgcolor = ft.colors.INDIGO,
                    border_radius = ft.border_radius.all(20),
                    margin = ft.margin.symmetric(vertical = 10),
                    content = ft.Column(
                        controls = [
                            ft.Text(value = 'Sua evolução hoje', size = 16, color = ft.colors.WHITE),
                            progress_text := ft.Text(value = '0%', size = 50, color = ft.colors.WHITE),
                            progress_bar := ft.ProgressBar(value = 0, color = ft.colors.INDIGO_900, bgcolor = ft.colors.INDIGO_100, height = 20),
                        ],
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                    ),
                ),

                ft.Text(value = 'Hábitos de hoje', size = 16, weight = ft.FontWeight.BOLD, color = ft.colors.WHITE),
                ft.Text(value = 'Marcar suas tarefas como concluído te motiva a ficar focado', size = 12, color = ft.colors.WHITE),

                habits := ft.Container(
                    expand = True,
                    padding = ft.padding.all(30),
                    bgcolor = ft.colors.GREY_900,
                    border_radius = ft.border_radius.all(20),
                    margin = ft.margin.symmetric(vertical = 20),
                    content = ft.Column(
                        expand = True,
                        scroll = ft.ScrollMode.ALWAYS,
                        spacing = 10,
                        controls = [
                            ft.Checkbox(
                                label = hl['title'], 
                                value = hl['done'], 
                                on_change = change) 
                                for hl in habits_list
                        ],
                    ),
                ),

                ft.Text(value = 'Adicionar novo hábito', size = 16, color = ft.colors.WHITE),
                ft.TextField(hint_text = 'Escreva um hábito...', border = ft.InputBorder.UNDERLINE, on_submit = add_habit),
            ],
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target = App, assets_dir = 'assets')
