import logging


from src.items import create_items
from src.users import create_users
from src.helpers import alert_special_items


logger = logging.getLogger("src")
print(f"===== {__name__}")

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler = logging.StreamHandler()

handler.setFormatter(formatter)

handler.setLevel(logging.DEBUG)

logger.addHandler(handler)


if __name__ == "__main__":
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    users = create_users()
    for user in users:
        items = create_items()
        for item in items:
            alert_special_items(item)
            item.save()
            user.add_item(item)
        user.save()

    logger.info("Done")