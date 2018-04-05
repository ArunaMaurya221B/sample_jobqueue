import logging as l

logger = l.getLogger(__name__)
logger.setLevel(l.INFO);

#creating a file handler
handler = l.FileHandler('CLI.log')
handler.setLevel(l.INFO);

#creating a logging format
formatter = l.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

#add the handler to the logger
logger.addHandler(handler)