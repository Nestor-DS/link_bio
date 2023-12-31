import reflex as rx
from link_bio.styles.styles import Size
from link_bio.components.title import title

def link_sponsor (image: str, alt: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image, 
            height=Size.VERY_BIG.value, 
            border_radius=Size.MEDIUM.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )