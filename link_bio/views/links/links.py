import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        title("Links"),
        link_button(
            "Web Portfolio",
            "Check out my projects",
            constants.PORTFOLIO_ICO,
            constants.PORTFOLIO_URL,
        ),
        link_button(
            "LinkedIn",
            "Professional profile",
            constants.LINKEDIN_ICO,
            constants.LINKEDIN_URL,
        ),
        link_button(
            "Instagram",
            "A bit about me",
            constants.INSTAGRAM_ICO,
            constants.INSTAGRAM_URL,
        ),
        link_button(
            "Youtube",
            "Programming videos",
            constants.YOUTUBE_ICO,
            constants.YOUTUBE_URL,
        ),
        link_button(
            "Email",
            "nestorduhamel18@outlook.es",
            constants.MAIL_ICO,
            constants.MAIL_URL,
        ),
        width="100%",
        spacing="2",
    )
