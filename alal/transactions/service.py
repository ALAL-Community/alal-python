from alal.base import Alal, pagination_filter
from .model import Transactions

class Transaction(Alal): 
    """
        transaction class
    """

    def __generate_transaction_objects(self, data):
        return Transactions(
            amount= data["amount"], 
            card_reference= data["card_reference"], 
            created_at= data["created_at"], 
            kind= ["kind"], 
            merchant= ["merchant"], 
            reference= data["reference"],
            status= data["status"],
            slug= data["slug"]
        )

    def createTransaction(self, body):
        """
            create card transaction 
            body = {
                "action" = "recharge",
                "amount" = "2000"
                card_reference = "9c54515e-7890-44f9-8cc2-a85b80322b98"
            }
            POST request
        """

        required_data = ["action", "amount", "card_reference"]
        self.checkRequiredData(required_data, body)

        response = self.sendRequest("POST", "transactions/create", json=body)
        return self.__generate_transaction_objects(data=response.get("data"))
    

    def listTransaction(self, **kwargs):
        """
            list all card transaction
            GET request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(kwargs=kwargs)
        response = self.sendRequest("GET", f"transactions/?{url_params}")
        data = response["data"]
        return [self.__generate_transaction_object(transaction_data) for transaction_data in data]

    def showCard(self, reference):
        """
            show transaction details
            GET request
        """
        response = self.sendRequest("GET", f"transactions/{reference}")
        return self.__generate_card_object(data=response.get("data"))