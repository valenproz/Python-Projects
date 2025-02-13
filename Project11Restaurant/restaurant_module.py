"""Restaurant Simulation Module"""


class Restaurant:

    def __init__(self, name):
        """Initializes the instance variables."""
        self.name = name
        self.yield = 0.0
        self.customers = 0

    def serve_customer(self, product_price: float) -> bool:
        """Simulates the service to a customer
        
            product_price: Price of the customer's meal
        
        Returns:
            True, if product_price is positive.
            False, if product_price is negative.
        """
        
        if product_price > 0:
            self.yield += product_price
            self.customers += 1

            return True
        else:
            return False

    def get_results(self):
        print(f"O {self.name} served {self.customers} customer(s) and earned $ {self.yield}")