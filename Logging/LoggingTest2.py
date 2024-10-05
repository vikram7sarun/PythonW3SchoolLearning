import logging

logging.basicConfig(filename="C://SeleniumLogs//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt= '%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
