import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, as_="span", font_weight="bold", color=Color.PRIMARY.value),
        rx.text(
            f" {body}",
            as_="span",
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value,
        ),
    )
