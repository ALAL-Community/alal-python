
import os
import requests
import hmac
from hashlib import sha512
from requests.exceptions import HTTPError, ConnectionError
from .exceptions import exception_class, AlalUnauthorized, AlalBadRequest
class Alal:
    """
        Alal class

    """
    def __init__(self): 
        self.Alal_LIVE_URL = 'https://api.saalal.com/v1'
        self.Alal_SANDBOX_URL = 'https://api.sandbox.saalal.com/v1'
        self.api_key = os.environ.get('AlalApiKey')
        self.production = os.environ.get('Production')

        if self.api_key is None: 
            raise  AlalUnauthorized()
        backupUrl = (
           self.Alal_SANDBOX_URL if self.production.lower() is False else self.Alal_LIVE_URL
        )
        self.base_url = os.environ.get("ALAL_BASE_URL") or backupUrl
        setattr(self, "base_url", self.base_url)

    def sendRequest(self, method, path, **kwargs):
        """
        Create a request for alal 
        return data

        """
   
        options = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "PATCH": requests.patch,
            "DELETE": requests.delete,
        }
        url = "{}{}".format(self.base_url, path)
        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer {}".format(self.api_key),
        }
        try:
            response = options[method](url, headers=headers, **kwargs)
            data = response.json()
            try:
                data["statusCode"]
                exception = exception_class.get(data["statusCode"])
                raise exception(data["message"])
            except KeyError:
                return data
        except (HTTPError, ConnectionError) as e:
            return e
    
    def checkRequiredData(self, required_data, passed_param):
        """
        function to check required param

        """
        for key in required_data:
            if key not in passed_param.keys():
                added_message = "The following are required: " + ",".join(required_data)
                message = f'{key} is required! ' + added_message
                raise AlalBadRequest(message)


    def pagination_filter(**kwargs):
        return "&".join([f"{k}={v}" for k, v in kwargs.items()])


    def webhook_authentification(request):
        """Validate signed requests."""
        api_signature = request.headers.get("x-alal-signature")
        secret = os.environ.get("")
        computed_sig = hmac.new(
            key=secret.encode("utf-8"), msg=request.body, digestmod=sha512
        ).hexdigest()
        return computed_sig == api_signature




        


