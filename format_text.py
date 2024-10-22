def center_text(text, width=50):
    return text.center(width)

def underline_text(text, width=50):
    border = "-" * width
    return text + "\n" + border

def border_text(text, width=50):
    centered_text = center_text(text, width - 2)
    centered_text = "*" + centered_text + "*"
    border = "*" * width
    return border + "\n" + centered_text + "\n" + border