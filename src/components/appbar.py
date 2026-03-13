import flet as ft

from components.basic_button import basic_button

def appbar_create(page):

    async def open_add_transaction(e):
        await page.push_route("/add_transaction")

    async def open_dashboard(e):
        await page.push_route("/dashboard")

    async def open_login(e):
        await page.push_route("/")

    user = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.ACCOUNT_BOX, icon_size=40),
                ft.Column(
                    controls=[
                        ft.Text("User Name"),
                        ft.Text("R$: Registered Values"),
                    ]
                )
            ]
        )
    )
    register = basic_button("Register", open_add_transaction)
    dashboard = basic_button("Data Visualization", open_dashboard)
    logoff = ft.IconButton(icon=ft.Icons.EXIT_TO_APP, icon_size=40, on_click=open_login)
    action_buttons = ft.Row(
        alignment= ft.MainAxisAlignment.CENTER,
        controls= [register, dashboard]
    )
    appbar = ft.AppBar(
        leading=user,
        title=action_buttons,
        bgcolor="#034040",
        actions=[logoff]
    )
    return appbar