nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


class FlatGenerator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        for inner_list in self.nested_list:
            for list_item in inner_list:
                yield list_item
        return


if __name__ == '__main__':
    flat_list = [item for item in FlatGenerator(nested_list)]
    print(flat_list)

