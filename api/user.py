import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required
from AIcodebyme.generate import generate
from AIcodebyme.aienglishprediction import aienglishprediction
from AIcodebyme.encryption import encrypter
from AIcodebyme.aienglish import aienglish
from model.users import User,Binary

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

class UserAPI:        
    class _CRUD(Resource):  # User API operation for Create, Read.  THe Update, Delete methods need to be implemeented
        def post(self): # Create method
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 400
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 400
            password = body.get('password')
            dob = body.get('dob')
            uo = User(name=name, 
                      uid=uid)
            if password is not None:
                uo.set_password(password)
            if dob is not None:
                try:
                    uo.dob = datetime.strptime(dob, '%Y-%m-%d').date()
                except:
                    return {'message': f'Date of birth format error {dob}, must be mm-dd-yyyy'}, 400
            
            ''' #2: Key Code block to add user to database '''
            user = uo.create()
            if user:
                return jsonify(user.read())
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 400

        @token_required()
        def get(self, _): 
            users = User.query.all()    
            json_ready = [user.read() for user in users]  
            return jsonify(json_ready) 
   
        @token_required("Admin")
        def delete(self, _): 
            body = request.get_json()
            uid = body.get('uid')
            user = User.query.filter_by(_uid=uid).first()
            if user is None:
                return {'message': f'User {uid} not found'}, 404
            json = user.read()
            user.delete() 
            return f"Deleted user: {json}", 204 
    class Images(Resource):
        @token_required()
        def post(self,_): # this function is uploading the image to the database
            print('here1')
            token = request.cookies.get("jwt")
            cur_user = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])['_uid'] # getting the current user 
            body=request.get_json()
            print('here')
            base64=body.get("Image")
            if not base64:
                return {'message': 'Message content is missing'},400
            users = User.query.all()
            for user in users:
                if user.uid == cur_user: # looping to check when we have found the current user and then updating the image
                    user.updatepfp(base64)
            print("succesful")
        @token_required()
        def get(self,_):
            print("here")
            token = request.cookies.get("jwt")
            cur_user = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])['_uid'] # current user
            users = User.query.all()
            for user in users:
                if user.uid == cur_user: # looping through all users till reaching the curent user and updating profile picture 
                    # print(type(user))
                    # print(jsonify(user.getProfile()))
                    return jsonify(user.getprofile())
    class _BinaryCipher(Resource):
        @token_required()
        def post(self, _): #Encrypting/Decrypting
            print('here')
            randomnumber=generate() # generating the random number for rotating binary digits
            shift=randomnumber.getrandom(1)
            body=request.get_json()
            text=body.get("Text")
            thenenc=encrypter(text) # creating the encryption of the text 
            encrypttext=thenenc.encrypt() 
            print(encrypttext,'before')     
            encrypttext=encrypttext[int(shift[0]):]+encrypttext[:int(shift[0])] # Actual rotation of the text
            
            token = request.cookies.get("jwt")
            cur_user = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])['_uid']
            thedata=Binary(cur_user,encrypttext,text,int(shift[0]))
            thedata.create()
            
            return jsonify(encrypttext)
        
        @token_required()
        def get(self, _):# this is the preivous encryptions function
            token = request.cookies.get("jwt")
            cur_user = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])['_uid']# getting the current user 
            texts= Binary.query.all()  
            encryptedtexts=[]
            
            for text in texts:
                if(text.read()['userid']==cur_user):
                    print(text,cur_user,text.read()['userid'])  
                    encryptedtexts.append(text.read()) # creating a list of all encryption queries made by the specific user
            return jsonify(encryptedtexts)
        def put(self): # this is the decryption function
            body=request.get_json()
            text=body.get("Text")
            predictor=aienglishprediction()
            allshifts=[]
            confidences=[]
            mydecrypter=encrypter("temp") # I pass through a random string but this creates an object of the encrypter class to perform binary->character conversion
            length=len(text)
            for i in range(length+100): # iterating through all of the binary digits 
                unshiftedtext=mydecrypter.decrypt(text) # trying decrypting the text for the current rotation 
                if(unshiftedtext==''):
                    text=text[1:]+text[:1]
                    continue
                confidences.append(predictor.predict(unshiftedtext)) # append the confidence that the current rotation is the correct decryption 
                allshifts.append(unshiftedtext)
                text=text[1:]+text[:1] # if unable to find correct english from this rotation rotate once again 
                
            maxconfidence=max(confidences)
            indexconf=-1
            for i in range(len(confidences)): # finding the rotation text where it is most confident
                if(confidences[i]==maxconfidence):
                    indexconf=i
            print(allshifts[i])
            return jsonify(allshifts[i])
            
        
            
            
            

            
            
            
    class _Security(Resource):
        def post(self):
            try:
                body = request.get_json()
                if not body:
                    return {
                        "message": "Please provide user details",
                        "data": None,
                        "error": "Bad request"
                    }, 400
                ''' Get Data '''
                uid = body.get('uid')
                if uid is None:
                    return {'message': f'User ID is missing'}, 401
                password = body.get('password')
                
                ''' Find user '''
                user = User.query.filter_by(_uid=uid).first()
                if user is None or not user.is_password(password):
                    return {'message': f"Invalid user id or password"}, 401
                if user:
                    try:
                        token = jwt.encode(
                            {"_uid": user._uid},
                            current_app.config["SECRET_KEY"],
                            algorithm="HS256"
                        )
                        resp = Response("Authentication for %s successful" % (user._uid))
                        resp.set_cookie("jwt", token,
                                max_age=3600,
                                secure=True,
                                httponly=True,
                                path='/',
                                samesite='None'
                                )
                        return resp
                    except Exception as e:
                        return {
                            "error": "Something went wrong",
                            "message": str(e)
                        }, 500
                return {
                    "message": "Error fetching auth token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 404
            except Exception as e:
                return {
                        "message": "Something went wrong!",
                        "error": str(e),
                        "data": None
                }, 500

            
    api.add_resource(_CRUD, '/')
    api.add_resource(_Security, '/authenticate')
    api.add_resource(_BinaryCipher,'/binary')
    api.add_resource(Images,'/images')
    