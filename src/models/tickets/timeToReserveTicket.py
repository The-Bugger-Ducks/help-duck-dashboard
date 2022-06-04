from datetime import datetime

def execute(cursorTicket):
  
  sumReservedAtTimestamp= 0
  sumCreatedTimestamp= 0

  diff = 0
  media = 0
  size = 0

  for ticket in cursorTicket:
    size+=1
    sumCreatedTimestamp += datetime.timestamp(ticket["createdAt"]) 
    sumReservedAtTimestamp += datetime.timestamp(ticket["reservedAt"]) 

  diff = sumReservedAtTimestamp - sumCreatedTimestamp
  media = (diff)/size
  
  segundos_rest = 0

  horas = media // 3600
  segundos_rest = media % 3600
  minutos = segundos_rest / 60
   
  if (minutos < 10):
    return f'{int(horas)}h0{round(minutos)}min'

  return f'{int(horas)}h{round(minutos)}min'