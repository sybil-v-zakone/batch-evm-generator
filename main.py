from config import WALLET_COUNT
from utils import (
    batch_generate_accounts,
    print_greeting_msg,
)


def main():
    print_greeting_msg()
    batch_generate_accounts(WALLET_COUNT)


if __name__ == "__main__":
    main()
