import firebase_admin
from firebase_admin import credentials, firestore

# Use the service account credentials JSON file you downloaded from Firebase
cred = credentials.Certificate('nba-history.json')
firebase_admin.initialize_app(cred)


# Access Firestore database
db = firestore.client()

# Reference to your collection
collection_ref = db.collection('games-23-24')  # Replace 'your_collection_name' with your actual collection name

# Retrieve documents from the collection
documents = collection_ref.stream()

# Extract gameID field from each document and store in a list
game_ids = [doc.to_dict().get('gameID') for doc in documents if doc.to_dict().get('gameID')]

# Write the game IDs to a text file
with open('game_ids.txt', 'w') as file:
    for game_id in game_ids:
        file.write(f"{game_id}\n")

print(game_ids)