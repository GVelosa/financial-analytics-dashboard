import flet as ft

from components.auth_card import auth_card
from components.basic_button import basic_button

def signup(page: ft.Page):
    #Functions
    async def open_add_transaction(e):
        await page.push_route("/add_transaction")

    async def open_login(e):
        await page.push_route("/")

    #Itens
    user = ft.TextField(label="User")
    email = ft.TextField(label="Email")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    confirm_password = ft.TextField(label="Confirm Password", password=True, can_reveal_password=True)
    enter_text =  ft.Text("Already have an account?")
    enter = ft.TextButton("Click Here!", on_click= open_login)
    signup = basic_button("Register", open_add_transaction)
    login = ft.Row(alignment= ft.MainAxisAlignment.CENTER,controls=[enter_text, enter])

    signup_card = auth_card(
        ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        user,
                        email,
                        password,
                        confirm_password,
                        signup,
                        login
                    ]
                ), ft.MainAxisAlignment.END
            )
    return signup_card