import simplejson as json

import src.connectDb as connectDb
import src.models.users.countUsers as countUsers
import src.models.tickets.countTickets as countTickets
import src.models.tickets.ticketsPerProblem as ticketsPerProblem
import src.models.tickets.timeToDone as timeToDone

db = connectDb.connect()
userCollection = db.user
ticketCollection = db.ticket

def report():
  cursorUser = userCollection.find()
  cursorTicket = ticketCollection.find()
  cursorProblem = ticketCollection.find()
  cursorTimeToDone = ticketCollection.find({"status":"done"})

  organizedJson = {
    "users": countUsers.execute(cursorUser),
    "tickets": countTickets.execute(cursorTicket),
    "tickets_per_problem": ticketsPerProblem.execute(cursorProblem),
    "timeToDone": timeToDone.execute(cursorTimeToDone)
  }

  return json.dumps(organizedJson)