from sqlobject import *
import os.path

dbfile = 'taxa.db3'

conn_str = os.path.abspath(dbfile)
conn_str = 'sqlite:'+ conn_str

sqlhub.processConnection = connectionForURI(conn_str)

class Taxonomy(SQLObject):
    class sqlmeta:
        idName = "tax_id"
        fromDatabase = True
    names = MultipleJoin('Name', joinColumn="tax_id")

class Name(SQLObject):
    class sqlmeta:
        fromDatabase = True
    taxa = ForeignKey('Taxonomy', dbName="tax_id")

