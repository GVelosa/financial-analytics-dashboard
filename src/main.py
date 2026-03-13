import flet as ft

from components.appbar import appbar_create

from theme import colors

from pages.login import login
from pages.signup import signup
from pages.dashboard import dashboard
from pages.add_transaction import add_transaction



def main(page: ft.Page):
    page.title = "Financial Analytics"
    page.window.width = 1792
    page.window.height = 1008
    page.window.alignment = ft.Alignment.CENTER

    def route_change():
        print("Route change:", page.route)
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar= None,
                bgcolor = colors.WHITE,
                controls=[
                    login(page)
                ],
            )
        )
        if page.route == "/signup":
            page.views.append(
                ft.View(
                    route="/signup",
                    appbar= None,
                    bgcolor = colors.WHITE,
                    controls=[
                        signup(page)
                    ],
                )
            )
        if page.route == "/add_transaction":
            page.views.append(
                ft.View(
                    route="/add_transaction",
                    appbar= appbar_create(page),
                    bgcolor = colors.WHITE,
                    controls=[
                        add_transaction(page)
                    ],
                )
            )
        if page.route == "/dashboard":
            page.views.append(
                ft.View(
                    route="/dashboard",
                    appbar= appbar_create(page),
                    bgcolor = colors.WHITE,
                    controls=[
                        dashboard(page)
                    ],
                )
            )
        page.update()
    async def view_pop(e):
        if e.view is not None:
            print("View pop:", e.view)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

if __name__ == "__main__":
    ft.run(main)
