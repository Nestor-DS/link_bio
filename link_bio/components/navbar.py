import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color
import link_bio.styles.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text(
                "Hello", color=Color.PRIMARY.value, style=styles.navbar_title_style
            ),
            rx.text(
                "There!", color=Color.SECONDARY.value, style=styles.navbar_title_style
            ),
        ),
        position="sticky",
        top=0,
        background_color=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        spacing="0",
    )
