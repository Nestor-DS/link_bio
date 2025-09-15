import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title,
                ),
                rx.vstack(
                    rx.text(title, sx=styles.button_title_style),
                    rx.text(body, sx=styles.button_body_style),
                    align_items="start",
                    spacing="1",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                width="100%",
            )
        ),
        href=url,
        is_external=True,
        width="100%",
        border_radius=Size.SMALL.value,
    )
