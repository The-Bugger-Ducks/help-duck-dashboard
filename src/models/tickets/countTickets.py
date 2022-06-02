def execute(cursorTicket):

  numberOfTickets = 0  
  numberOfTicketAwaiting = 0  
  numberOfTicketUnderAnalysis = 0  
  numberOfTicketDone = 0  

  for ticket in cursorTicket:
    numberOfTickets += 0

    if ticket["status"] == "awaiting":
      numberOfTicketAwaiting+=1
    if ticket["status"] == "underAnalysis":
      numberOfTicketUnderAnalysis+=1
    if ticket["status"] == "done":
      numberOfTicketDone+=1

  return {
    "total_tickets": numberOfTickets,
    "total_awaiting": numberOfTicketAwaiting,
    "total_underAnalysis": numberOfTicketUnderAnalysis,
    "total_done": numberOfTicketDone
  }
