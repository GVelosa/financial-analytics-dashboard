import flet as ft

from theme import colors

def auth_card(content, side):
    return ft.Row(
        expand=True,
        alignment=side,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Card(
                bgcolor = colors.GREEN_DARK,
                elevation=45,
                content=ft.Container(
                    width=875,
                    padding=20,
                    content=content
                )
            )
        ]
    )