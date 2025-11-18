import logging 

logging.basicConfig(
    level = logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    logging.info("Bot has stated.")
    logging.info("Bot finished succesfully.")



if __name__ == "__main__":
    run()