from loguru import logger
from mnemonic import Mnemonic
from openpyxl import Workbook
from web3 import Web3

from config import WALLETS_EXPORT_PATH
from constants import EVM_DERIVATION_PATH

web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()


def export_json(data, destination):
    try:
        logger.info(f'Saving wallets to {WALLETS_EXPORT_PATH}')

        workbook = Workbook()
        sheet = workbook.active

        headers = ["Address", "Private key"]
        sheet.append(headers)

        for key, value in data.items():
            sheet.append([key, value])

        workbook.save(destination)

    except Exception as e:
        logger.error(f"Encountered an error while exporting to Excel: {str(e)}")
        exit()


def generate_mnemonic():
    try:
        mnemonic = Mnemonic()
        words = mnemonic.generate(strength=128)
        if len(words.split(' ')) < 12:
            raise Exception('words length is not satisfy requirements. Regenerating...')

        return words
    except Exception:
        logger.error('Words length is not satisfy requirements. Regenerating..')


def generate_account():
    mnemonic = generate_mnemonic()
    account = web3.eth.account.from_mnemonic(mnemonic, account_path=EVM_DERIVATION_PATH)
    private_key, address = web3.to_hex(account._private_key), account.address

    return private_key, address


def batch_generate_accounts(count):
    accounts = {}
    for i in range(count):
        private_key, address = generate_account()
        accounts[address] = private_key

    if len(accounts.keys()) != count:
        logger.error('Generated accounts is less than required. Check the output')

    logger.info(f'Total generated wallets: {len(accounts.keys())}/{count}')
    export_json(accounts, WALLETS_EXPORT_PATH)

    return accounts


def print_greeting_msg():
    start_message = r"""
                   __    _ __                        __                  
       _______  __/ /_  (_) /  _   __   ____  ____ _/ /______  ____  ___ 
      / ___/ / / / __ \/ / /  | | / /  /_  / / __ `/ //_/ __ \/ __ \/ _ \
     (__  ) /_/ / /_/ / / /   | |/ /    / /_/ /_/ / ,< / /_/ / / / /  __/   
    /____/\__, /_.___/_/_/    |___/    /___/\__,_/_/|_|\____/_/ /_/\___/ 
         /____/      """

    logger.success(start_message)
