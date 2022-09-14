import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main(event, context):
    logger.info('Event: ' + json.dumps(event, indent=2))
