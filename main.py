import flet as ft
from ChecklistB738 import checklists as checklistsB738
from ChecklistA320 import checklists as checklistsA320

def main(page: ft.Page):
    page.title = "✈️ Aircraft Checklist"
    page.window_width = 900
    page.window_height = 600
    page.window_resizable = False
    page.bgcolor = ft.Colors.LIGHT_BLUE_50

    checklist_switch_b738 = ft.Switch(value=False)
    checklist_switch_a320 = ft.Switch(value=False)

    label_b738 = ft.Text("Boeing 737-800", size=20, weight=ft.FontWeight.BOLD)
    label_a320 = ft.Text("Airbus A320", size=20, weight=ft.FontWeight.BOLD)

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Checklist", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
        content=ft.Column([], spacing=5),
        actions=[
            ft.TextButton("Checklist Complete", on_click=lambda e: page.close(dlg))
        ],
        actions_alignment=ft.MainAxisAlignment.END,  # Кнопка справа
    )

    def open_dialog(e, checklist_type, aircraft):
        if aircraft == "B738" and not checklist_switch_b738.value:
            return
        if aircraft == "A320" and not checklist_switch_a320.value:
            return

        checklist_data = checklistsB738 if aircraft == "B738" else checklistsA320
        checklist = checklist_data.get(checklist_type, [])

        if not checklist:  # Обработка пустого чек-листа
            dlg.title = ft.Text("Ошибка", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.RED)
            dlg.content = ft.Text("Чек-лист пуст или не найден!", font_family="Courier New", size=18, color=ft.Colors.BLACK)
            page.open(dlg)
            return

        checklist_title = checklist_type.replace("_", " ").title()
        dlg.title = ft.Text(checklist_title, size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)

        task_list = []
        for item in checklist:
            formatted_text = ft.Row([
                ft.Text(f"{item['task'].ljust(30, '.')} {item['response']}", font_family="Courier New", size=18),
                ft.Checkbox(value=False, scale=0.9)  # Чекбокс справа, слегка уменьшен для аккуратности
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

            task_list.append(formatted_text)

        dlg.content = ft.Column(task_list, spacing=5)
        page.open(dlg)

    def create_button(name, aircraft):
        return ft.ElevatedButton(
            text=name.replace("_", " ").capitalize(),
            on_click=lambda e: open_dialog(e, name, aircraft),
            disabled=True,
            width=200,
            height=50,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=16)
            )
        )

    buttons_b738 = [create_button(name, "B738") for name in checklistsB738.keys()]
    buttons_a320 = [create_button(name, "A320") for name in checklistsA320.keys()]

    def update_buttons(e):
        for btn in buttons_b738:
            btn.disabled = not checklist_switch_b738.value
        for btn in buttons_a320:
            btn.disabled = not checklist_switch_a320.value
        page.update()

    checklist_switch_b738.on_change = update_buttons
    checklist_switch_a320.on_change = update_buttons

    page.add(
        ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Container(content=label_b738, alignment=ft.alignment.center),
                        ft.Container(content=checklist_switch_b738, alignment=ft.alignment.center)
                    ], spacing=5),
                    width=200
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Container(content=label_a320, alignment=ft.alignment.center),
                        ft.Container(content=checklist_switch_a320, alignment=ft.alignment.center)
                    ], spacing=5),
                    width=200
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=50),
            ft.Row([
                ft.Container(
                    content=ft.Column(buttons_b738, alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                    expand=True,
                    padding=ft.padding.only(left=60, right=30)
                ),
                ft.Container(
                    content=ft.Column(buttons_a320, alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                    expand=True,
                    padding=ft.padding.only(left=30, right=60)
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=50)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
