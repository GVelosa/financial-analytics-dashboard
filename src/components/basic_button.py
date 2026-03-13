import flet as ft

from theme import colors

def basic_button(text_label, action):
    return ft.Button(
        f"{text_label}", 
        width=250,
        height=35,
        bgcolor=colors.GREEN_DARKEST,
        style=ft.ButtonStyle(
            color=colors.ACCENT,
            text_style=ft.TextStyle(
                size=18,
                weight=ft.FontWeight.BOLD,     
            ),
            side=ft.BorderSide(
            width=2,
            color=colors.ACCENT
            )
        ),
        on_click=action
    )