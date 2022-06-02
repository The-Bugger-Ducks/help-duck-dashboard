import simplejson as json

import src.connectDb as connectDb
import src.models.users.countUsers as countUsers
import src.models.tickets.countTickets as countTickets
import src.models.tickets.ticketsPerProblem as ticketsPerProblem
import src.models.tickets.timeToReserveTicket as timeToReserveTicket

db = connectDb.connect()
userCollection = db.user
ticketCollection = db.ticket

def report():
  cursorUser = userCollection.find()
  cursorTicket = ticketCollection.find()
  cursorProblem = ticketCollection.find()
  cursorTimeReserve = ticketCollection.find({'reservedAt': {'$exists': True}})

  organizedJson = {
    "users": countUsers.execute(cursorUser),
    "tickets": countTickets.execute(cursorTicket),
    "tickets_per_problem": ticketsPerProblem.execute(cursorProblem),
    "tickets_time_to_reserve": timeToReserveTicket.execute(cursorTimeReserve)
  }

  return json.dumps(organizedJson)