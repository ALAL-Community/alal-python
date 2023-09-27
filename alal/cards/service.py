from alal.base import Alal, pagination_filter
from .model import Card

class Card(Alal): 
    """
        Cards class
    """

    def __generate_card_object(self, data):
        return Card(
            balance = data["balance"],
            cardType = data["cardType"], 
            cardBrand = data["cardBrand"], 
            last_four = data["last_four"],
            reference = data["reference"],
            status = data["status"],
        )


    def createCard(self, body:dict):
        """
            create card on alal platform
            body = {
                "card_brand": "Visa",
                "card_type": "virtual",
                "cardUserReference": "d282e4a6-1fb6-4827-a6ae-a780263287d7",
            }

            POST request 
        """
        required_data = ["cardType", "cardBrand", "cardUserReference"]
        self.checkRequiredData(required_data, body) 

        response = self.sendRequest("POST", "cards/create", json=body)
        return self.__generate_card_object(data=response.get("data"))
    
    def listCard(self, **kwargs):
        """
            list all cards 
            GET request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(kwargs=kwargs)
        response = self.sendRequest("GET", f"cards/?{url_params}")
        data = response["data"]
        return [self.__generate_card_object(card_data) for card_data in data]
    
    def showCard(self, reference):
        """
            show card details
            GET request
        """
        response = self.sendRequest("GET", f"cards/?{reference}")
        return self.__generate_card_object(data=response.get("data"))
    
    def getAccessToken(self, body):
        """
            create card access token 
            body = {
                css_url = "style.css",
                reference = "d282e4a6-1fb6-4827-a6ae-a780263287d7"
            }
            POST request
        """
        required_data = ["css_url", "reference"]
        self.checkRequiredData(required_data, body)

        response = self.sendRequest("POST", "cards/auth/acess_token", json=body)
        return response.get("data")

        
  