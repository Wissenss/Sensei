import logging

logging.basicConfig(level=logging.INFO, format=" [\033[36m%(levelname)s\033[0m] %(message)s")

if __name__ == "__main__":
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")