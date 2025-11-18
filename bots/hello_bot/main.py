import logging
# Bot report // what is the bot doing?

logging.basicConfig(
    level = logging.INFO,
    # to use the format and structure
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    logging.info("Bot has stated.")
    logging.info("Bot finished succesfully.")


if __name__ == "__main__":
    run()