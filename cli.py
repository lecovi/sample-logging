from src.logger import logger
from src.items import create_items
from src.users import create_users
from src.helpers import alert_special_items


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