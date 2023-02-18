import logging


logger = logging.getLogger(__name__)


class User:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.name=})>"

    def save(self):
        logger.info("Saving User to file: %s", self.name)

    def add_item(self, item):
        logger.info("Adding %s to user: %s", item, self)
        self.items.append(item)
