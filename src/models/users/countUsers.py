def execute(cursorUser):
  
  numberOfTotalUsers = 0 
  numberOfUsersAdmin = 0
  numberOfUsersSupport = 0
  numberOfUsersClient = 0

  for user in cursorUser:
    numberOfTotalUsers+=1
    if user["role"] == "client":
      numberOfUsersClient+=1
    if user["role"] == "support":
      numberOfUsersSupport+=1
    if user["role"] == "admin":
      numberOfUsersAdmin+=1

  return {
    "total_users": numberOfTotalUsers,
    "total_admins": numberOfUsersAdmin,
    "total_supports": numberOfUsersSupport,
    "total_clients": numberOfUsersClient,
  }
