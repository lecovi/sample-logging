import logging


logger = logging.getLogger(__name__)
print(f"===== {__name__}")


class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.name=}, {self.description=}, {self.value=})>"

    def save(self):
        print("===== Saving item to file: %s" % self)

        logger.info("Saving item to file: %s", self)
