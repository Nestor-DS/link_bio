import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

MAX_WIDTH = "600px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "4"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "size": "lg",
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.LARGE.value,
        "white_space": "normal",
        "text_align": "start",
        "background_color": Color.CONTENT.value,
        "text_color": TextColor.HEADER.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "text_color": TextColor.HEADER.value,
        },
    },
    rx.link: {
        
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "text_color": TextColor.HEADER.value,
        },
    },
}
navbar_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size="16px",
    margin_y=Size.SMALL.value,
)


title_style = dict(
    width="100%",
    size="2",
    padding_top=Size.BIG.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
)
