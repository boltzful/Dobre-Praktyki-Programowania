import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Exceptions
#Exceptions: NetworkException, PaymentException, and RefundException represent various issues that might arise during payment processing.
class NetworkException(Exception):
    pass

class PaymentException(Exception):
    pass

class RefundException(Exception):
    pass

# Enum for transaction status
class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

# Transaction result
#TransactionStatus: An enumeration representing the transaction status (PENDING, COMPLETED, FAILED).
class TransactionResult:
    def __init__(self, success, transaction_id, message=""):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message

#TransactionResult: A class used to store information about the outcome of a transaction, 
#such as success (a boolean), transaction_id (a unique identifier for the transaction), and message.

# PaymentGateway interface
class PaymentGateway:
    def charge(self, user_id, amount):
        raise NotImplementedError

    def refund(self, transaction_id):
        raise NotImplementedError

    def get_status(self, transaction_id):
        raise NotImplementedError
    
#process_payment: Attempts to charge the user via PaymentGateway. 
#It validates inputs, catches exceptions from the gateway, and logs the outcome (success or error).
class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def process_payment(self, user_id, amount):
        if not user_id or amount <= 0:
            logger.error("Invalid user_id or amount.")
            raise ValueError("Invalid user_id or amount.")
        
        try:
            result = self.gateway.charge(user_id, amount)
            if result.success:
                logger.info(f"Payment processed successfully for user {user_id} with transaction ID {result.transaction_id}.")
            else:
                logger.warning(f"Payment failed for user {user_id}. Message: {result.message}")
            return result
        except (NetworkException, PaymentException) as e:
            logger.error(f"Error processing payment for user {user_id}: {e}")
            # Optional: retry logic
            return TransactionResult(success=False, transaction_id=None, message=str(e))

#refund_payment: Initiates a refund for a transaction. It checks if transaction_id is valid, handles exceptions, and logs the result.
    def refund_payment(self, transaction_id):
        if not transaction_id:
            logger.error("Invalid transaction_id.")
            raise ValueError("Invalid transaction_id.")
        
        try:
            result = self.gateway.refund(transaction_id)
            if result.success:
                logger.info(f"Refund processed successfully for transaction ID {transaction_id}.")
            else:
                logger.warning(f"Refund failed for transaction ID {transaction_id}. Message: {result.message}")
            return result
        except (NetworkException, RefundException) as e:
            logger.error(f"Error processing refund for transaction ID {transaction_id}: {e}")
            return TransactionResult(success=False, transaction_id=transaction_id, message=str(e))
#get_payment_status: Fetches the status of a transaction, logs it, and handles any network exceptions.
    def get_payment_status(self, transaction_id):
        if not transaction_id:
            logger.error("Invalid transaction_id.")
            raise ValueError("Invalid transaction_id.")
        
        try:
            status = self.gateway.get_status(transaction_id)
            logger.info(f"Transaction {transaction_id} status retrieved: {status}.")
            return status
        except NetworkException as e:
            logger.error(f"Error retrieving status for transaction ID {transaction_id}: {e}")
            return TransactionStatus.FAILED
