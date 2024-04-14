def number_cart_mask(number: str) -> str:
    return f"{number[:4]} {number[5:7]}** **** {number[-4:]}"


def last_four(number: str) -> str:
    return f"**{number[-4:]}"
