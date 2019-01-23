import MySQLdb as mdb
from bottle import FormsDict
from hashlib import md5

# connection to database project2
def connect():
    """makes a connection to MySQL database.
    @return a mysqldb connection
    """
    
    #TODO: fill out function parameters. Use the user/password combo for the user you created in 2.1.2.1
    
    return mdb.connect(host="localhost",
                       user="fisiaka2",
                       passwd="1ea14023161737d15b0cfba5ad8c5eba49e51853fc0e11cdb5da46377487ccc7",
                       db="project2");

def createUser(username, password):
    """ creates a row in table named user 
    @param username: username of user
    @param password: password of user
    """

    db_rw = connect()
    cur = db_rw.cursor()

    #TODO: Implement a prepared statement using cur.execute() so that this query creates a row in table user
    password_hash = md5(password).hexdigest()
    query = ("INSERT INTO users (username, password, passwordhash) "
            "VALUES ('{username}', '{password}', '{passwordhash}');").format(username=str(username), password=str(password), passwordhash=str(password_hash))
    
    cur.execute(query)
    db_rw.commit()

def validateUser(username, password):
    """ validates if username,password pair provided by user is correct or not
    @param username: username of user
    @param password: password of user
    @return True if validation was successful, False otherwise.
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query selects a row from table user
    query = "SELECT * FROM users WHERE username='{username}' AND password ='{password}';".format(username=str(username), password=str(password))
    cur.execute(query)
    if cur.rowcount < 1:
        return False
    return True

def fetchUser(username):
    """ checks if there exists given username in table users or not
    if user exists return (id, username) pair
    if user does not exist return None
    @param username: the username of a user
    @return The row which has username is equal to provided input
    """

    db_rw = connect()
    cur = db_rw.cursor(mdb.cursors.DictCursor)
    query= "SELECT id, username FROM users WHERE username='{user}';".format(user=str(username))
    cur.execute(query)
    #TODO: Implement a prepared statement so that this query selects a id and username of the row which has column username = username
    if cur.rowcount < 1:
        return None
    return FormsDict(cur.fetchone())

def addHistory(user_id, query):
    """ adds a query from user with id=user_id into table named history
    @param user_id: integer id of user
    @param query: the query user has given as input
    """

    db_rw = connect()
    cur = db_rw.cursor()

    #TODO: Implement a prepared statment using cur.execute() so that this query inserts a row in table history
    sqlquery =("INSERT INTO history (user_id, query) "
                "VALUES ('{user_id}', '{query}');").format(user_id=str(user_id), query=str(query))
    cur.execute(sqlquery)
    db_rw.commit()

#grabs last 15 queries made by user with id=user_id from table named history
def getHistory(user_id):
    """ grabs last 15 distinct queries made by user with id=user_id from 
    table named history
    @param user_id: integer id of user
    @return a first column of a row which MUST be query
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query selects 15 distinct queries from table history
    query = "SELECT DISTINCT id, query FROM history WHERE user_id='{user_id}';".format(user_id=str(user_id))
    cur.execute(query)
    rows = cur.fetchall();
    rows = [pair[1] for pair in rows]
    searches = []
    for index in range(len(rows) - 1, -1, -1):
        if (rows[index] not in searches):
            searches.append(rows[index])
        if(len(searches) == 15):
            break
    return searches
