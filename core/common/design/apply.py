import ttkbootstrap as tb
from .components import Components


def apply_design():
    style = tb.Style()
    Components.apply(style)
    return style
