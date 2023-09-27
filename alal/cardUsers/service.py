from alal.base import Alal, pagination_filter
from .model import CardUser

class CardUser(Alal):
    """
        CardUser class
    """

    def __generate_cardUser_object(self, data):
        return CardUser(
            address = data["address"], 
            created_at = data["created_at"], 
            email  = data["email"],
            first_name = data["first_name"],
            last_name = data["last_name"],
            id_no = data["id_no"],
            phone = data["phone"],
            reference = data["reference"],
            status = data["status"],
        )

    
    def createCardUser(self, body): 
        """
            create card user on alal platform 
            body = {
                    "address": "rue ng 59 grand ngor",
                    "email": "ndiayendeyengone99@gmail.com",
                    "first_name": "ndeye ngone",
                    "id_no": "20119991010000621",
                    "last_name": "ndiaye",
                    "phone": "774964996",
                    "reference": "88c2f29c-2fba-40f1-a303-b33008e42fe9", 
                    "id_image": "image.jpeg", 
                    "selfie_image": "selfie.jpeg"
            }
            POST request
        """
        required_data = ["address", "back_id_image", "email", "first_name", "last_name", "id_image", "id_no", "phone", "selfie_image"]
        self.checkRequiredData(required_data, body)

        response = self.sendRequest("POST", "crad-users/create", json=body)
        return self.__generate_cardUser_object(data=response.get("data"))
    

    def listCardUser(self, **kwargs): 
        """
            list all card user
            GET request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(kwargs=kwargs)
        response = self.sendRequest("GET", f"card-users/?{url_params}")
        data = response["data"]
        return [self.__generate_cardUser_object(cardUser_data) for cardUser_data in data]   
    
    def showCardUser(self, reference):
        """
            show card user details
            GET request
        """
        response = self.sendRequest("GET", f"card-users/?{reference}")
        return self.__generate_cardUser_object(data=response.get("data"))
    