import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size
import link_bio.constants as constants
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src=constants.MY_PHOTO,
                size="xl",
                name="Foto de gato",
                color=TextColor.HEADER.value,
                bg=Color.BACKGROUND.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
                alt="Foto de Nestor"
            ),
            rx.vstack(
                rx.heading(
                    "Hola, soy Nestor 👾"
                ),
                rx.text(
                    "Desarrollador de software en proceso",
                    margin_top=Size.ZERO.value
                ),
                rx.hstack(  
                    link_icon(
                        constants.GITHUB_ICO,
                        "Github icon",
                        constants.GITHUB_URL),
                    link_icon(
                        constants.X_ICO,
                        "Email icon",
                        constants.X_URL),
                    link_icon(
                        constants.LINKEDIN_ICO,
                        "Spotify icon",
                        constants.LINKEDIN_URL),
                    spacing=Size.DEFAULT.value,  
                ),
                align_items="start",
                   
            ),
            spacing=Size.DEFAULT.value,
            color=TextColor.HEADER.value
        ),
        rx.flex(
            info_text("+1", "Años de experiencia"),
            rx.spacer(),
            info_text("Python", "Lenguaje favorito"),
            rx.spacer(),
            #info_text("0s", "Seguidores"),
            width="100%"
        ),
        rx.text("""Soy un desarrollador de software, mi lenguaje favorito es Python, 
            actualmente estoy aprendiendo ML, me interesa aprender más sobre el mundo del desarrollo web y movil.""",
                font_size = Size.MEDIUM.value,
                color = TextColor.BODY.value
                ),
        spacing=Size.BIG.value,
        align_items = "start"
    )