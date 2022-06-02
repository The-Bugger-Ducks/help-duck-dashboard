from datetime import datetime

def execute(cursorTicket):
  
  for ticket in cursorTicket:
    reservedAt = datetime.timestamp(ticket["reservedAt"])
    createdAt = datetime.timestamp(ticket["createdAt"])

    time = createdAt - reservedAt
    
    
  return {}