import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size
import link_bio.constants as constants


def links () -> rx.Component:
    return rx.vstack(
        title("Links"),
        link_button(
            "GitHub",
            "Te invito a ver mis proyectos",
            constants.GITHUB_ICO,
            constants.GITHUB_URL
        ),
        link_button(
            "Linkedin",
            "Perfil profesional",
            constants.LINKEDIN_ICO,
            constants.LINKEDIN_URL
        ),
        link_button(
            "Instagram",
            "Un poco sobre mi",
            constants.INSTAGRAM_ICO,
            constants.INSTAGRAM_URL
        ),
        link_button(
            "Youtube",
            "Videos de programación",
            constants.YOUTUBE_ICO,
            constants.YOUTUBE_URL
        ),
        link_button(
            "Email",
            "nestorduhamel18@outlook.es",
            constants.MAIL_ICO,
            constants.MAIL_URL),
        
        # title("Links"),
        
        # link_button(
        #     "Twitter",
        #     "¡Descubre mis pensamientos más ingeniosos!",
        #     constants.TWITCH_ICO,
        #     constants.TWITTER_URL
        # ),
        # link_button(
        #     "Twitch",
        #     "Canal primario",
        #     constants.TWITCH_ICO,
        #     constants.TWITCH_URL
        # ),
        
        width="100%",
        spacing=Size.DEFAULT.value,
    )