from json import load


def main():
    with open("random.json", "r") as raw_file:
        data = load(raw_file)
        length_of_list = len(data["random"])

        for item_1 in range(length_of_list):
            for item_2 in range(length_of_list):
                if data["random"][item_1] < data["random"][item_2]:
                    data["random"][item_1], data["random"][item_2] = swap(
                        item_2, item_1
                    )
            print(item_1)


def swap(x, y):
    tmp = x
    x = y
    y = tmp
    del tmp
    return x, y


if __name__ == "__main__":
    main()
