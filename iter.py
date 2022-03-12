nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    cursor = 0
    nest_cursor = 0

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.nest_cursor == len(self.nested_list[self.cursor]):
            self.nest_cursor = 0
            self.cursor += 1
        if self.cursor == len(self.nested_list):
            raise StopIteration
        item = self.nested_list[self.cursor][self.nest_cursor]
        self.nest_cursor += 1
        return item


if __name__ == '__main__':
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


