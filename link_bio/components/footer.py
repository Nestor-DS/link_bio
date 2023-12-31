import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as constants

def footer () -> rx.Component:
    return rx.vstack(
        rx.image(
            src=constants.MY_ICON, 
            height=Size.VERY_BIG.value, 
            border_radius=Size.MEDIUM.value,
            alt="N's icon"
            ),
        rx.link(
            f"© 2023 - {datetime.date.today().year} Nestor",
            # Cambiar por pagina personal
            href=constants.GITHUB_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
            
        ),
        rx.text(
            "Made with Reflex 🐍",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
            ),
        margin_buttom = Size.BIG.value,
        color = TextColor.FOOTER.value,
        padding_buttom = Size.BIG.value,
        padding_x = Size.BIG.value,
    )