import simplejson as json

import src.connectDb as connectDb

db = connectDb.connect()
userCollection = db.user

def index():
    print(userCollection)
    return json.dumps({"ok": "ok"})