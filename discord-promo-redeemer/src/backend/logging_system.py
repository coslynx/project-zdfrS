import logging

class LoggingSystem:
    def __init__(self):
        logging.basicConfig(filename='redeemer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_successful_redemption(self, code):
        logging.info(f"Promo code {code} successfully redeemed.")

    def log_failed_redemption(self, code, error):
        logging.error(f"Failed to redeem promo code {code}. Error: {error}")

    def log_general_error(self, error):
        logging.error(f"An error occurred: {error}")