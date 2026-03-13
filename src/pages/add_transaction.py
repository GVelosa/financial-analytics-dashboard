import flet as ft

from components.datepicker import datepicker
from components.auth_card import auth_card
from components.basic_button import basic_button

def add_transaction(page: ft.Page):
    def save_transaction():
        transaction = {
            "name": name.value,
            "notes": notes.value,
            "value": value.value,
            "date": date_value["value"],
            "type": type.value,
            "category": category.value,
            "tags": tags.value,
            "recurring": recurring.value
        }
        print(transaction)

    name = ft.TextField(label = "Name")
    notes = ft.TextField(label ="Notes", multiline=True)
    value = ft.TextField(label ="Value")
    date_picker, date_value = datepicker(page)
    type = ft.Dropdown(
                    label="Type",
                    options=[
                        ft.dropdown.Option("Income"),
                        ft.dropdown.Option("Expense"),
                        ft.dropdown.Option("Investment"),
                    ],
                )
    category = ft.Dropdown(
                    label="Category",
                    options=[
                        ft.dropdown.Option("Food"),
                        ft.dropdown.Option("Transport"),
                        ft.dropdown.Option("Rent"),
                        ft.dropdown.Option("Salary"),
                        ft.dropdown.Option("Entertainment"),
                    ],
                )
    tags = ft.Dropdown(
                    label="Tags",
                    options=[
                        ft.dropdown.Option("Trip"),
                        ft.dropdown.Option("Work"),
                        ft.dropdown.Option("Health"),
                        ft.dropdown.Option("Family"),
                    ],
                )
    recurring = ft.Switch(label="Recurring transaction")
    save = basic_button("Save", save_transaction)
    register = auth_card(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Add Infomations", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                name,
                notes,
                value,
                date_picker,
                type,
                category,
                tags,
                recurring,
                save
            ]),ft.MainAxisAlignment.START
    )
    return register
