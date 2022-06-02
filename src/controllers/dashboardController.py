import simplejson as json

import src.connectDb as connectDb
import src.models.users.countUsers as countUsers
import src.models.tickets.ticketsPerProblem as ticketsPerProblem

db = connectDb.connect()
userCollection = db.user
ticketsCollection = db.ticket

def report():
  cursorUser = userCollection.find()
  cursorTickets = ticketsCollection.find()

  organizedJson = {
    "users": countUsers.execute(cursorUser),
    "tickets_per_problem": ticketsPerProblem.execute(cursorTickets)
  }

  return json.dumps(organizedJson)