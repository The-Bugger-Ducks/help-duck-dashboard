import simplejson as json

import src.connectDb as connectDb
import src.models.users.countUsers as countUsers

db = connectDb.connect()
userCollection = db.user

def report():
  cursorUser = userCollection.find()

  organizedJson = {
    "users": countUsers.execute(cursorUser)
  }

  return json.dumps(organizedJson)