# def print_hi(name):
#     print(f'Hi, {name}')

# get number of people. input each username with their fav genres. list all the genres with its popularity.
def input_username():
    pass


def genres():
    return ['Horror', 'Romance', 'Comedy', 'History', 'Adventure', 'Action']


def genre(index: int) -> str:
    return genres()[index]


if __name__ == '__main__':
    print(genre(3))
