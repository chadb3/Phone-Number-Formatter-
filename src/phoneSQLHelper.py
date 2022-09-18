import sqlite3

def SELECT_PHONE_NUMBER(areaCodeIn):
    con=sqlite3.connect("testDB.sqlite3")

def SELECT_AREA_CODES_FROM_STATE(stateIN):
    fileNamePath="data/PNDB.sqlite3"
    sqlite3Connection=sqlite3.connect(fileNamePath)
    cur=sqlite3Connection.cursor()
    res=cur.execute("SELECT ")

def SELECT_STATE_FROM_ABBR(stateABBR):
    fileNamePath="data/PNDB.sqlite3"




class PhoneNumberDB:
    def __init__(this):
        this.DATABASEFILE="data/PNDB.sqlite3"
        this.MODE="?mode=rw"
        this._URI=True
        #this.sql_connection=sqlite3.connect(this.DATABASEFILE+this.MODE,this._URI)
    def SELECT_STATE(this, ITEM_IN):
        None
    def SELECT_PHONE_NUMBER(this,ID_IN):
        None
    def SELECT_AREA_CODE(this,ITEM_IN):
        None
    def SELECT_ALL_AREA_CODES_AND_STATE_ABBR(this):
        con=sqlite3.connect(this.DATABASEFILE)#+this.MODE,this._URI) look into why this doesn't work, or if it is even needed at all...
        sqlCursor=con.execute("SELECT * FROM USA_AREA_CODES")
        try:
            retList=sqlCursor.fetchall()
            return retList
        except Exception as ex:
            print(ex)
            print("\n\nIssue: SELECT * FROM USA_AREA_CODES - Did Not Work!\n\n")
            return []
        print("(^: <-> if you see this something is wrong in \"SELECT_ALL_AREA_CODES_AND_STATE_ABBR\"")
        
    def TEST_SELECT_STATE(this):
        print("if you are not working directly inside src this might not work...")
        con=sqlite3.connect("testDB.sqlite3")
        #state=con.execute("SELECT STATE FROM US_STATES WHERE ID=1") #111=None
        state=con.execute("SELECT * FROM US_STATES")
        print(state)
        print("SELECT * FROM US_STATES")
        try:
            a=state.fetchall()
            print("STATEs: {}".format(a)) #.fetchone()[0]
            print(type(a))
            print(a[0][0])
            print(a[0][1])
            print(a[0][2])
        except Exception as k:
            print(k)
        con.close()