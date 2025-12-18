from .base import Design
from .colors import Colors
from .padding import Padding
from .typography import Typography
from .components import Components

# Injeta como atributos do Design (namespace)
Design.Colors = Colors
Design.Padding = Padding
Design.Typography = Typography
Design.Components = Components

__all__ = ["Design"]
