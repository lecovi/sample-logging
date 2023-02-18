import logging

from .models import User


logger = logging.getLogger(__name__)


def create_users():
    logger.info("Creating users")
    users = [
        User("Bob"),
        User("Alice"),
        User("John"),
    ]
    logger.info("Created %s users", len(users))
    return users