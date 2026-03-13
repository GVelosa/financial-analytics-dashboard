import flet as ft
import datetime

def datepicker(page):
    date = ft.Text("Select a Date")
    selected_date = {"value": None}

    def handle_change(e: ft.Event[ft.DatePicker]):
        selected_date["value"] = e.control.value.strftime("%Y-%m-%d")
        date.value = f"{e.control.value.strftime('%d/%m/%Y')}"
        page.update()

    def handle_dismissal(e: ft.Event[ft.DialogControl]):
        date.value = "DatePicker dismissed"
        page.update()

    today = datetime.datetime.now()

    picker = ft.DatePicker(
        first_date=datetime.datetime(year=today.year - 1, month=1, day=1),
        last_date=datetime.datetime(year=today.year + 1, month=today.month, day=20),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
    )

    datepicker = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,controls=[ft.IconButton(
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.show_dialog(picker),
        ), date])
    return datepicker, selected_date