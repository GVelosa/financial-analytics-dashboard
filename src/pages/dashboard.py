import flet as ft

def dashboard(page: ft.Page):
    dashboard = ft.Row(
        controls=[
            ft.Column(controls=[
                ft.Text("Add Infomations"),
                ft.TextField(""),
            ]),
            ft.Column(controls=[

            ]),
        ]
    )
    return dashboard

