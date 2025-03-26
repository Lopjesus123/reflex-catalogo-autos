
import reflex as rx
from rxconfig import config  
def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="/logo.png", width="80px"),
        rx.spacer(),
        rx.link("Pago a meses", href="#"),
        rx.link("Compra ahora mismo", href="#"),
        rx.link("Sucursales", href="#"),
        rx.link("Contacto", href="#"),
        rx.link("Accesorios", href="#"),
        rx.menu.root(
            rx.menu.trigger(rx.text("Nosotros ▾")),
            rx.menu.content(
                rx.menu.item("Quiénes somos"),
                rx.menu.item("Misión y visión"),
            ),
        ),
        # ¡Usa "tag" en lugar de "name"!
        rx.icon(tag="user", size=24),
        padding="1em",
        bg="white",
        shadow="md",
        position="sticky",
        top="0",
        z_index="999",
        spacing="4"
    )

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.text("Filtros", font_weight="bold", font_size="1.2em"),
                    rx.accordion.root(
                        rx.accordion.item(
                            rx.accordion.trigger("Marca"),
                            rx.accordion.content(
                                rx.checkbox("Nissan"),
                                rx.checkbox("Volkswagen"),
                                rx.checkbox("Chevrolet"),
                            )
                        ),
                        rx.accordion.item(
                            rx.accordion.trigger("Precio"),
                            rx.accordion.content(
                                rx.checkbox("$0 - $200,000"),
                                rx.checkbox("$200,000 - $400,000"),
                                rx.checkbox("Más de $400,000"),
                            )
                        ),
                        type="multiple",
                        width="100%"
                    ),
                    spacing="3",
                    padding="1em"
                ),
                width="20%",
                bg="#f2f2f2",
                height="100%",
                padding="1em"
            ),
            rx.box(
                rx.input(placeholder="Buscar modelo, año, precio, etc.", width="100%"),
                rx.text("Aquí aparecerán los resultados", padding_top="1em"),
                width="80%",
                padding="2em"
            ),
            align="start",
            width="100%"
        ),
        bg="#f5f5f5",
        min_height="100vh",
        padding="0"
    )

app = rx.App()
app.add_page(index, title="Catálogo de Autos | Jesús")



