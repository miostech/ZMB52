#from internal import envs

# USER = envs.get_secret("USER_DATABASE")
# PASSWORD = envs.get_secret("PASSWORD_DATABASE")
# HOST = envs.get_secret("HOST_DATABASE")
# PORT = envs.get_secret("PORT_DATABASE")
# DATABASE = envs.get_secret("NAME_DATABASE")

USER = "uptime"
PASSWORD = "Ascendum.Uptim3.."
HOST = "ascendumuptime.database.windows.net"
PORT = 1433
DATABASE = "uptime"
DRIVER = "SQL Server Native Client 11.0"


def connection():
    return f"mssql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?driver={DRIVER}"
