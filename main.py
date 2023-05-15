import argparse

from asymmetric import (asymmetric_key_decryption, asymmetric_key_encryption,
                        asymmetric_keys_generation)
from read_functions import (byte_read_text, read_private_key, read_settings,)
from symmetric import (symmetric_key_generation,
                       symmetric_decryption, symmetric_encryption)
from write_functions import (byte_write_text, write_private_key)

SETTINGS_FILE = "files/settings.json"


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument('-gen','--generation',help='Запускает режим генерации ключей')
group.add_argument('-enc','--encryption',help='Запускает режим шифрования')
group.add_argument('-dec','--decryption',help='Запускает режим дешифрования')

args = parser.parse_args()
if args.generation is not None:
  # генерируем ключи
else if args.encryption is not None:
  # шифруем
else:
  # дешифруем