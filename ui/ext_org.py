import flet as ft

def organize_by_ext(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.add(
        ft.SafeArea(
            content=ft.Container(
                bgcolor=ft.colors.BLUE_GREY_200,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text("This text is inside the Safe Area.", size=20),
                        ft.ElevatedButton("A Button", on_click=lambda _: print("Clicked!")),
                    ]
                ),
            ),
        )
    )