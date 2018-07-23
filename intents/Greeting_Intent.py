from random import randint
import requests

class Greeting_Intent:
    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message
        self.response = ["hello", "a5bark", "a7walk"]

    @staticmethod
    def check(user_id, message):
        print("message value = ", message)
        if(message == "Hi"):
            return Greeting_Intent(user_id, message)
        else:
            return None


    def reply(self):
        data = {'user_id': self.user_id}
        res = requests.post('https://goachievenow.com/admin/api/User/searchuserdetail', data)
        dictFromServer = res.json()
        name = dictFromServer['message']

        
        index = randint(0, len(self.response)-1)
        return self.response[index]