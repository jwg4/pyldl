from sample.credentials import token

from pyldb import get_board


if __name__ == '__main__':
    db = get_board("NWD", token)
    print(db)