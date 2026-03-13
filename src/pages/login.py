import flet as ft

from theme import colors

from components.auth_card import auth_card
from components.basic_button import basic_button

def login(page: ft.Page):

    async def open_add_transaction(e):
        await page.push_route("/add_transaction")

    async def open_signup(e):
        await page.push_route("/signup")

    user = ft.TextField(label="User or Email")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    loguin = basic_button("Enter", open_add_transaction)
    signup_text = ft.Text("Don't have an Account?")
    signup = ft.TextButton("Register Now!", on_click=open_signup, style=ft.ButtonStyle(color=colors.GREEN_LIGHT))
    register = ft.Row(alignment= ft.MainAxisAlignment.CENTER, controls=[signup_text, signup])
    login_card = auth_card(ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[user, password, loguin, register]
    ), ft.MainAxisAlignment.START)
    return login_card