import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#Logging Setup: Configures logging to record timestamps, log levels, and messages.

#PaymentProcessor Class:

#processPayment: Checks if the payment amount is valid. If valid, it attempts to process the payment through gateway.charge(), logging success or failure.
#refundPayment: Attempts to refund a payment using gateway.refund(), logging the outcome.
#getPaymentStatus: Retrieves the payment status via gateway.getStatus() and logs it. Logs an error if there’s a network issue.
#Supporting Classes:

#PaymentGateway: Defines methods for charging, refunding, and checking status.
#TransactionResult: Holds transaction success, ID, and message.
#TransactionStatus: Contains COMPLETED and FAILED statuses.
#Exceptions: Define specific errors like NetworkException, PaymentException, and RefundException.
#In short, PaymentProcessor handles payment, refund, and status operations while logging and managing exceptions.

class PaymentProcessor:
    def __init__(self, gateway):
        self.gateway = gateway
        logging.info("PaymentProcessor initialized with gateway.")

    def processPayment(self, user, amount):
        logging.info(f"Processing payment for user: {user}, amount: {amount}")
        if amount <= 0:
            logging.warning("Invalid amount provided for payment.")
            return TransactionResult(success=False, message="Invalid input parameters")
        try:
            result = self.gateway.charge(user, amount)
            logging.info(f"Payment processed successfully for user: {user}, transaction ID: {result.transactionId}")
            return result
        except PaymentException as e:
            logging.error(f"Payment failed for user: {user} with exception: {e}")
            return TransactionResult(success=False, message=str(e))

    def refundPayment(self, transaction_id):
        logging.info(f"Processing refund for transaction ID: {transaction_id}")
        try:
            result = self.gateway.refund(transaction_id)
            logging.info(f"Refund processed successfully for transaction ID: {transaction_id}")
            return result
        except RefundException as e:
            logging.error(f"Refund failed for transaction ID: {transaction_id} with exception: {e}")
            return TransactionResult(success=False, message=str(e))

    def getPaymentStatus(self, transaction_id):
        logging.info(f"Retrieving payment status for transaction ID: {transaction_id}")
        try:
            status = self.gateway.getStatus(transaction_id)
            logging.info(f"Payment status for transaction ID: {transaction_id} is {status}")
            return status
        except NetworkException:
            logging.error("Network exception occurred while retrieving payment status.")
            return TransactionStatus.FAILED

# Define other classes and exceptions as in the previous example.
class PaymentGateway:
    def charge(self, user, amount):
        pass

    def refund(self, transaction_id):
        pass

    def getStatus(self, transaction_id):
        pass

class TransactionResult:
    def __init__(self, success, transactionId=None, message=""):
        self.success = success
        self.transactionId = transactionId
        self.message = message

class TransactionStatus:
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class NetworkException(Exception):
    pass

class PaymentException(Exception):
    pass

class RefundException(Exception):
    pass
