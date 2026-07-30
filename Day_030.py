from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def process(self, amount: float) -> dict:
        pass

    @abstractmethod
    def validate(self, data: dict) -> bool:
        pass

    def receipt(self, result: dict) -> str:
        return (
            f"Receipt\n"
            f"Status : {result['status']}\n"
            f"Method : {result['method']}\n"
            f"Amount : ₹{result['amount']}"
        )


class UPIProcessor(PaymentProcessor):

    def validate(self, data: dict) -> bool:
        upi_id = data.get("upi_id", "")
        return "@" in upi_id

    def process(self, amount: float) -> dict:
        return {
            "status": "success",
            "method": "UPI",
            "amount": amount
        }


class CardProcessor(PaymentProcessor):

    def validate(self, data: dict) -> bool:
        card_number = data.get("card_number", "")
        return card_number.isdigit() and len(card_number) == 16

    def process(self, amount: float) -> dict:
        return {
            "status": "success",
            "method": "Card",
            "amount": amount
        }


class CashProcessor(PaymentProcessor):

    def validate(self, data: dict) -> bool:
        return True

    def process(self, amount: float) -> dict:
        return {
            "status": "success",
            "method": "Cash",
            "amount": amount
        }


# Example Usage

upi = UPIProcessor()

if upi.validate({"upi_id": "avinash@ybl"}):
    result = upi.process(1000)
    print(upi.receipt(result))
else:
    print("Invalid UPI ID")
