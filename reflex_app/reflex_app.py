import reflex as rx
from rxconfig import config


def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="/Black and Red Modern Automotive Car Services Logo.png", width="80px"),
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
        rx.icon(tag="user", size=24),
        padding="1em",
        bg="white",
        shadow="md",
        position="sticky",
        top="0",
        z_index="999",
        spacing="4",
    )

# Creamos un helper para la tarjeta.
def auto_card(
    titulo: str,
    precio: str,
    detalles: str,
    imagen_url: str = "https://via.placeholder.com/300x180"
) -> rx.Component:
    return rx.box(
        rx.image(src=imagen_url, border_radius="lg"),
        rx.text(titulo, font_weight="bold", font_size="1.1em"),
        rx.text(precio),
        rx.text(detalles, font_size="0.9em", color="gray"),
        padding="1em",
        box_shadow="md",
        border_radius="xl",
        bg="white",
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
                            ),
                        ),
                        rx.accordion.item(
                            rx.accordion.trigger("Precio"),
                            rx.accordion.content(
                                rx.checkbox("$0 - $200,000"),
                                rx.checkbox("$200,000 - $400,000"),
                                rx.checkbox("Más de $400,000"),
                            ),
                        ),
                        type="multiple",
                        width="100%",
                    ),
                    spacing="3",
                    padding="1em",
                ),
                width="20%",
                bg="#f2f2f2",
                height="100%",
                padding="1em",
            ),
            rx.box(
                rx.input(placeholder="Buscar modelo, año, precio, etc.", width="100%"),
                width="80%",
                padding="2em",
            ),
            align="start",
            width="100%",
        ),
        rx.box(
            # Aquí construimos la cuadrícula "manual" usando display="grid".
            auto_card(
                titulo="Nissan Kicks",
                precio="$247,999.00",
                detalles="2018 · Automático · 18,000 km · Nuevo",
            ),
            auto_card(
                titulo="SENSE MT '25",
                precio="$353,900.00",
                detalles="2019 · Manual · 16,000 km · Nuevo",
            ),
            # ...Puedes añadir más tarjetas
            display="grid",                      # cuadrícula
            grid_template_columns="repeat(3, 1fr)",
            gap="1.5em",
            width="100%",
            padding="2em",
        ),
        bg="#f5f5f5",
        min_height="100vh",
        padding="0",
    )

app = rx.App()
app.add_page(index, title="Catálogo de Autos | Jesús")
