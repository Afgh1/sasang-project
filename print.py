
def upper_everything(elements: list[str]) -> list[str]:
    return [elements.upper() for elements in elements]


def main() -> None:
    loud_list: list[str] = upper_everything(['Mario', 'James', 'Sandra'])
    # loud_list: list[int] = upper_everything(['Mairo', 'Janmes', 'Sandra']

    print(loud_list)


if __name__ == '__main__':
    main()
