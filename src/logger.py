import logging

logger = logging.getLogger("src")

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler = logging.StreamHandler()

handler.setFormatter(formatter)

handler.setLevel(logging.DEBUG)

logger.addHandler(handler)