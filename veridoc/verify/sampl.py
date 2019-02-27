import pyodbc
server = '127.0.0.1'
database = 'master'
username = 'sa'
password = 'Creative2000'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cnxn.autocommit = True
cursor = cnxn.cursor()

backup = "verify/MyData.txt"
sql = "BACKUP DATABASE [sampleDB] TO DISK = N'samplDB.bak'"
GO
cursor.execute(sql)
cursor.cancel()
cnxn.autocommit = False
cnxn.close()




#backup = 'verify/1.txt'
#f= open("1.txt","w+")
