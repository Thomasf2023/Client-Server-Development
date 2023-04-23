from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username == "accuser" and password == "Helloworld":
            print("The Username and Password are:", username, password)
            self.client = MongoClient('mongodb://%s:%s@localhost:54196/AAC' % (username, password))
            self.database = self.client['AAC']
            print("Connection sucessful")
       
        

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
                  if data:
                      self.database.animals.insert_one(data)
                      return True
                  else:
                      return False
                  

# Create method to implement the R in CRUD. 
    def read(self, key):
        
        readResult = self.database.animals.find(key, {"_id":False})
        
        return readResult
        
# Create Method to implment U in CRUD
    def update(self, key, value, changeKey, newValue):
        updateResult = self.database.animals.update_one({key: value}, {"$set": {changeKey: newValue}})
        print(updateResult)
        
# Create method to implment D in CRUD.
    def delete(self, key, value):
        deleteResult = self.database.animals.deleteOne({key:value})
        print(deleteResult)
        
        
        