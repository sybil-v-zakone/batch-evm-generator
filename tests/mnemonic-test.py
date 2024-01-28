# This file contains code to own check random generated words for no-repeating
from mnemonic import Mnemonic


def generate_mnemonic():
    try:
        mnemonic = Mnemonic()
        words = mnemonic.generate(strength=128)
        if len(words.split(' ')) < 12:
            raise Exception('words length is not satisfy requirements. Regenerating...')

        return words
    except Exception:
        logger.error('Words length is not satisfy requirements. Regenerating..')


for i in range(1, 50):
    words = generate_mnemonic()
    print(words)
