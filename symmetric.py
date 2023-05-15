import logging
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


logger = logging.getLogger()
logger.setLevel("INFO")


def symmetric_key_generation() -> bytes:
    """Generating a key for a symmetric encryption algorithm
    Returns:
        bytes: key for symmetric encryption algorithm.
    """
    key = os.urandom(16)
    logging.info("Symmetric key successfully generated!")
    return key
