import logging


logger = logging.getLogger(__name__)


def alert_special_items(item):
    if item.value > 50:
        logger.info("Found special item: %s", item.name)