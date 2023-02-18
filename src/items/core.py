import logging

from .models import Item


logger = logging.getLogger(__name__)


def create_items():
    logger.info("Creating items")
    items = [
        Item("Gold", "A shiny gold coin", 100),
        Item("Potion", "A healing potion", 10),
        Item("Sword", "A sharp sword", 20),
        Item("Shield", "A sturdy shield", 20),
    ]
    logger.info("Created %s items", len(items))
    return items