def mask_info(input_string):
    parts = input_string.split()
    if len(parts) == 2:
        return f"{parts[0]} {parts[1][:6]}******{parts[1][-4:]}"
    elif len(parts) == 3:
        return f"{parts[0]} {parts[1]} {parts[2][:6]}******{parts[2][-4:]}"
    elif parts[0] == "Счет":
        return f"Счет **{input_string[-4:]}"


print(mask_info(input()))
