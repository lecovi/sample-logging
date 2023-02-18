import logging

from .models import User


logger = logging.getLogger(__name__)
print(f"===== {__name__}")


def create_users():
    print("===== Creating Users")
    logger.info("Creating users")
    users = [
        User("Bob"),
        User("Alice"),
        User("John"),
    ]
    print("===== Created %s users" % len(users))
    logger.info("Created %s users", len(users))
    return users