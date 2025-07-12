from bson import ObjectId
from posts.domain.repositories import PostRepositoryInterface

class PostRepository(PostRepositoryInterface):
    def __init__(self, db):
        self.collection = db["posts"]
    
    def create(self, post_data):
        result = self.collection.insert_one(post_data)
        post_data["_id"] = result.inserted_id
        return post_data

    def update(self, post_data):
        post_id = post_data["_id"]
        self.collection.replace_one({"_id": post_id}, post_data)
        return post_data

    def find_by_id(self, post_id):
        return self.collection.find_one({"_id": ObjectId(post_id)})
    
    def delete(self, post_id):
        self.collection.delete_one({"_id": ObjectId(post_id)})

    def find_pending(self):
        return list(self.collection.find({"is_approved": False}))
    
    def find_approved(self):
        return list(self.collection.find({"is_approved": True}))
    
    def find_by_email(self, email):
        return list(self.collection.find({"contact_email": email}))


