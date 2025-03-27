import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        if cg.value:
            t.value = cg.value
            img.src = images[cg.value]
            page.update()

    images = {
        "May your dreams be bigger than your fears": "gringo.jpg",
        "Que tus sueños sean más grandes que tus miedos": "nick.jpg",
        "Che i tuoi sogni siano più grandi delle tue paure": "italiano.jpg"
    }

    t = ft.Text()
    img = ft.Image(width=300, height=200, fit=ft.ImageFit.COVER)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    cg = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="May your dreams be bigger than your fears", label="Inglés"),
            ft.Radio(value="Que tus sueños sean más grandes que tus miedos", label="Español"),
            ft.Radio(value="Che i tuoi sogni siano più grandi delle tue paure", label="Italiano")
        ])
    )

    page.add(
        ft.Text("Cambia el idioma de la frase: 'Que tus sueños sean más grandes que tus miedos'"),
        cg, b, t, img
    )

ft.app(target=main, assets_dir="assets")
