def process_items(item_t: tuple[int, int, str], item_s: set[bytes]):
    return item_t, item_s

item_t = (1, 2, "3")
item_s = {71, 72, 73}

print(process_items(item_t, item_s))


