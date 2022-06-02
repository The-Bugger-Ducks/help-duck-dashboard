import simplejson as json

import src.connectDb as connectDb
import src.models.users.countUsers as countUsers
import src.models.tickets.countTickets as countTickets

db = connectDb.connect()
userCollection = db.user
ticketCollection = db.ticket

def report():
  cursorUser = userCollection.find()
  cursorTicket = ticketCollection.find()

  organizedJson = {
    "users": countUsers.execute(cursorUser),
    "tickets": countTickets.execute(cursorTicket)
  }

  return json.dumps(organizedJson)