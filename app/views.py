import json
from app import app
from flask_restful import Api, Resource, reqparse
from flask import request, jsonify
import requests
import os
from intents.Greeting_Intent import Greeting_Intent

api = Api(app)


class RecommendationAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', location='json', required=True, help="id is required")
        self.parser.add_argument('category', type=dict, location='json', required=True, help="category is required and it has to be of type dict")
        self.parser.add_argument('name', location='json', required=True, help="name is required")
        self.parser.add_argument('photoUrls', location='json', action='append', required=True, help="photoUrls is required")
        self.parser.add_argument('tags', type=dict, location='json', action='append', required=True, help="tags is required and it has to be of type dict")
        self.parser.add_argument('status', location='json', required=True, help="status is required")

    def get(self):
        user_id = request.args.get("user_id")
        message = request.args.get("message")
        
        print("user id ", user_id)
        print("message ", message)
        greeting_intent = Greeting_Intent.check(user_id, message)
        if(greeting_intent == None):
            return "Please say Hi", 200
        
        return greeting_intent.reply(), 200

# api.add_resource(PetImageAPI, '/pet/<string:id>/uploadImage', endpoint = 'PetImageAPI')
api.add_resource(RecommendationAPI, '/recommendation', endpoint = 'RecommendationAPI')


