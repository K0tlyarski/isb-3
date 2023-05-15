import logging

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

logger = logging.getLogger()
logger.setLevel("INFO")


def asymmetric_keys_generation() -> tuple:
    """Private and public key generation.

    Returns:
        tuple: tuple with private and public keys.
    """
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    logging.info(f"Asymmetric keys successfully generated!")
    return (private_key, public_key)