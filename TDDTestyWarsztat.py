#TDD: Tests are written before implementing functionality, driving the development of PaymentProcessor. 
#For each method, we create test cases for both positive and negative scenarios, validating input handling and exception management.
import unittest
from unittest.mock import MagicMock, patch

#Mocks and Stubs: We use MagicMock to simulate PaymentGateway responses, such as successful transactions and exceptions (e.g., NetworkException). 
#This allows us to test PaymentProcessor without needing an actual external payment system.

#Spies: The patch decorator captures log calls, verifying that PaymentProcessor 
#logs correctly for successes, warnings, and errors.

#Exception Handling: We test each method’s response to different exceptions, 
#checking that PaymentProcessor handles these gracefully without crashing and logs appropriate error messages.
class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.gateway = MagicMock(spec=PaymentGateway)
        self.processor = PaymentProcessor(self.gateway)

    @patch("logging.Logger.info")
    def test_process_payment_success(self, mock_log):
        self.gateway.charge.return_value = TransactionResult(success=True, transaction_id="123", message="Success")
        result = self.processor.process_payment("user123", 100)
        
        self.assertTrue(result.success)
        self.gateway.charge.assert_called_once_with("user123", 100)
        mock_log.assert_called_with("Payment processed successfully for user user123 with transaction ID 123.")

    def test_process_payment_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment("user123", -50)

    def test_process_payment_network_exception(self):
        self.gateway.charge.side_effect = NetworkException("Network Error")
        result = self.processor.process_payment("user123", 100)
        
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Network Error")

    @patch("logging.Logger.error")
    def test_refund_payment_success(self, mock_log):
        self.gateway.refund.return_value = TransactionResult(success=True, transaction_id="123", message="Refund Success")
        result = self.processor.refund_payment("123")
        
        self.assertTrue(result.success)
        self.gateway.refund.assert_called_once_with("123")
        mock_log.assert_called_with("Refund processed successfully for transaction ID 123.")

    def test_refund_payment_invalid_transaction_id(self):
        with self.assertRaises(ValueError):
            self.processor.refund_payment("")

    @patch("logging.Logger.warning")
    def test_get_payment_status_pending(self, mock_log):
        self.gateway.get_status.return_value = TransactionStatus.PENDING
        status = self.processor.get_payment_status("123")
        
        self.assertEqual(status, TransactionStatus.PENDING)
        self.gateway.get_status.assert_called_once_with("123")

    def test_get_payment_status_network_exception(self):
        self.gateway.get_status.side_effect = NetworkException("Network Error")
        status = self.processor.get_payment_status("123")
        
        self.assertEqual(status, TransactionStatus.FAILED)
