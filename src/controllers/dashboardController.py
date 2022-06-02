import simplejson as json

import src.connectDb as connectDb
import src.models.users.countUsers as countUsers
import src.models.tickets.countTickets as countTickets
import src.models.tickets.ticketsPerProblem as ticketsPerProblem

db = connectDb.connect()
userCollection = db.user
ticketCollection = db.ticket

def report():
  cursorUser = userCollection.find()
  cursorTicket = ticketCollection.find()

  organizedJson = {
    "users": countUsers.execute(cursorUser),
    "tickets": countTickets.execute(cursorTicket),
    "tickets_per_problem": ticketsPerProblem.execute(cursorTickets)
  }

  return json.dumps(organizedJson)