from alal.base import Alal, pagination_filter
from .model import Disputes

class Dispute(Alal):
    """
        Dispute class
    """

    def __generate_dispute_objects(self, data):
        return Disputes(
            explanation= data["explanation"], 
            reason= data["reason"],
            reference= data["reference"], 
            status= data["status"],
            transaction_reference= data["transaction_reference"]
        )
    

    def createDispute(self, body):
        """
            create dispute on alal platform 
            body = {
                "explanation" = "No real explanation even now", 
                "reason" = "duplicate", 
                "transaction_reference" = "962b954d-bbd3-4b03-8a70"
            }

            POST request 
        """

        required_data = ["explanation", "reason", "transaction_reference"]
        self.checkRequiredData(required_data, body)

        response = self.sendRequest("POST", "disputes/create", json=body)
        return self.__generate_dispute_objects(data=response.get("data"))
    
    def listDispute(self, **kwargs): 
        """
            list all disputes
            GET request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(kwargs=kwargs)
        response = self.sendRequest("GET", f"disputes/?{url_params}")
        data = response["data"]
        return [self.__generate_dispute_object(dispute_data) for dispute_data in data] 
    

    def showCardUser(self, reference):
        """
            show disputes details
            GET request
        """
        response = self.sendRequest("GET", f"disputes/{reference}")
        return self.__generate_dispute_object(data=response.get("data"))
    
    def updateDispute(self, body, reference):
        """
            update dispute on alal platform 
            body = {
                "explanation" = "No real explanation even now", 
                "reason" = "fraudulent", 
                "transaction_reference" = "962b954d-bbd3-4b03-8a12"
            }

            POST request 
        """

        required_data = ["explanation", "reason", "transaction_reference"]
        self.checkRequiredData(required_data, body)

        response = self.sendRequest("POST", f"disputes/update/{reference}", json=body)
        return self.__generate_dispute_objects(data=response.get("data"))