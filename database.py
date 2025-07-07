from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["xauusd_ss"]
collection = db["snapshots"]

def save_snapshot(entry, sl, tp, rr_ratio, img_path):
    data = {
        "entry": entry,
        "stop_loss": sl,
        "take_profit": tp,
        "rr_ratio": rr_ratio,
        "timestamp": datetime.utcnow(),
        "image_path": img_path
    }
    collection.insert_one(data)
