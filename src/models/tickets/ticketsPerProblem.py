def execute(cursorTickets):
  
  numberOfNetworkAccess = 0
  numberOfSoftwareMalfunction = 0
  numberOfEmailAccess = 0
  numberOfBenefitsUse = 0
  numberOfPayment = 0
  numberOfInsuficientDoc = 0
  numberOfDamagedEquipment = 0
  numberOfNetworkAccess = 0
  numberOfOthers = 0

  for ticket in cursorTickets:
    if ticket["problem"]["title"] == "Acesso a rede":
      numberOfNetworkAccess+=1
    if ticket["problem"]["title"]  == "Mau funcionamento de software":
      numberOfSoftwareMalfunction+=1
    if ticket["problem"]["title"]  == "Acesso ao email":
      numberOfEmailAccess+=1

    if ticket["problem"]["title"] == "Uso de beneficios":
      numberOfBenefitsUse+=1
    if ticket["problem"]["title"]  == "Pagamento":
      numberOfPayment+=1
    if ticket["problem"]["title"]  == "Documentação insuficiente":
      numberOfInsuficientDoc+=1
    if ticket["problem"]["title"] == "Equipamento danificado":
      numberOfDamagedEquipment+=1
    if ticket["problem"]["title"]  == "Outros":
      numberOfOthers+=1

  return {
    "network_access":numberOfNetworkAccess,
    "email_access":numberOfEmailAccess,
    "benefits_use":numberOfBenefitsUse,
    "payment":numberOfPayment,
    "software_malfunction":numberOfSoftwareMalfunction,
    "insuficient_doc":numberOfInsuficientDoc,
    "damaged_equipament":numberOfDamagedEquipment,
    "others":numberOfOthers
  }
