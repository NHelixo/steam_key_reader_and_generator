from random import choice
import string

keys_num = int(input("Number of keys: "))

def load_keys():
    try:
        with open("keys_list", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_keys(keys):
    keys = list(set(keys))
    keys.sort()
    with open("keys_list", "w") as f:
        for key in keys:
            f.write(key + "\n")

def generator(keys_num, keys):
    symbols = list(string.ascii_uppercase + string.digits)
    num = 15

    keys_num += len(keys)
    while len(keys) < keys_num:
        lis = []
        for i in range(num):
            ran = choice(symbols)
            lis.append(ran)

            if (i+1) % 5 == 0 and i + 1 != num:
                lis.append("-")

            if i + 1 == num and "".join(lis) not in keys:
                keys.append("".join(lis))
                break

    save_keys(keys)
    print(f"Generated keys:\n{keys}")

keys = load_keys()
generator(keys_num, keys)
