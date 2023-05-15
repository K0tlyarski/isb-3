import logging

from cryptography.hazmat.primitives import serialization

logger = logging.getLogger()
logger.setLevel("INFO")


def byte_write_text(text: bytes, file_name: str) -> None:
    """Writing text as bytes.

    Args:
        text (bytes): text for writing.
        file_name (str): name of .txt file.
    """
    try:
        with open(file_name, "wb") as text_file:
            text_file.write(text)
        logging.info(f"Text was successfully written to file {file_name}!")
    except OSError as err:
        logging.warning(f"Text was not written to file {file_name}\n{err}!")
