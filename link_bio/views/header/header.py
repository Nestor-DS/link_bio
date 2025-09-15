import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size
import link_bio.constants as constants
from link_bio.styles.colors import TextColor, Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src=constants.MY_PHOTO,
                name="Cat photo",
                color=TextColor.HEADER.value,
                bg=Color.BACKGROUND.value,
                size="6",
                style={
                    "padding": "2px",
                    "borderWidth": "4px",
                    "borderColor": Color.PRIMARY.value,
                    "borderStyle": "solid",
                    "borderRadius": "100%",
                },
                alt="Nestor's photo",
            ),
            rx.vstack(
                rx.heading("Hi, I'm Nestor 👾"),
                rx.text(
                    "Backend Developer",
                    margin_top=Size.ZERO.value,
                    color=TextColor.HEADER.value,
                    font_size=Size.DEFAULT.value,
                ),
                rx.hstack(
                    link_icon(
                        constants.GITHUB_ICO, "Github icon", constants.GITHUB_URL
                    ),
                    link_icon(constants.X_ICO, "Email icon", constants.X_URL),
                    link_icon(
                        constants.LINKEDIN_ICO, "LinkedIn icon", constants.LINKEDIN_URL
                    ),
                    spacing=Size.DEFAULT.value,
                ),
                align_items="start",
            ),
            spacing=Size.DEFAULT.value,
        ),
        rx.flex(
            info_text("2", "Years of experience"),
            rx.spacer(),
            info_text("Java", "Core Language"),
            rx.spacer(),
            width="100%",
        ),
        rx.text(
            "I'm a backend developer specialized in Java and Spring Boot. "
            "I create robust and scalable REST APIs, handle database operations, "
            "and implement business logic. Always learning new backend technologies.",
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value,
        ),
        spacing="6",
        align_items="start",
    )
