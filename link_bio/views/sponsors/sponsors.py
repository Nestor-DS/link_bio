import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
import link_bio.constants as constants
from link_bio.styles.styles import Size

def sponsors () -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.responsive_grid(
            link_sponsor(
                constants.SPONSOR1, 
                "El Gato",
                constants.EL_GATO
            ),
            link_sponsor(
                constants.SPONSOR2, 
                "Rust",
                constants.RUST
            ),
            spacing=Size.BIG.value,
            columns=[1, 2]
        ),
        width="100%",
        align_items="start"
    )