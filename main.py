#first commit 


#commmom commands for interacting with ADLS from DataBricks 

#for access key 
spark.conf.set(
    "fs.azure.account.key.<storage-account>.dfs.core.windows.net",
    dbutils.secrets.get(scope="<scope>", key="<storage-account-access-key>"))

#TO Display secret scope
dbutils.secrets.listScopes()
#To display list of secrets
dbutils.secrets.list(scope = '<Scope Name>')
#For list of all command
dbutils.secrets.help()