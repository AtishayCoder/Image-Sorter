import flet as ft
import ui.ext_org as ext_org
import ui.img_org as img_org

def main(page: ft.Page):
    # Display layout according to platform
    # platform = page.platform

    # if platform.name.lower() in ["android", "ios"]:
    #     ext_org.organize_by_ext(page)
    # elif platform.name.lower() in ["windows", "macos", "linux"]:
    #     img_org.organize_by_img(page)
    # else:
    #     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #     page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #     page.add(
    #         ft.Text(
    #             size=42.5,
    #             value="Unsupported Platform"
    #         )
    #     )
    ext_org.organize_by_ext()

ft.app(target=main)
