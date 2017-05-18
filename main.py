import datetime
import mysql.connector

def getLigandsId(tid):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select * from drug_mechanism where TID ="+tid)
    ligands=[]
    cursor.execute(query)
    for (record_id) in cursor:
        ligands.append(record_id[1])
    cursor.close()
    cnx.close()
    #print(ligands)
    return ligands


def getTargets():
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select tid from target_dictionary")
    elements=[]
    cursor.execute(query)
    for c in cursor:
        elements.append(c[0])
    cursor.close()
    cnx.close()
    return elements


#deprecated
def getBindingSites(tid):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select * from binding_sites where TID = 104688")
    elements=[]
    cursor.execute(query)
    for (site_id) in cursor:
        elements.append(c)
    cursor.close()
    cnx.close()
    return elements

#deprecated
def getLigandFromBs(binding_site):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select * from drug_mechanism where TID = 104688")
    element=null
    cursor.execute(query)
    for c in cursor:
        elements = c

    cursor.close()
    cnx.close()
    return element


def getLigandActivities(ligand_id):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select * from compound_records where TID = 104688")
    element=null
    cursor.execute(query)
    for c in cursor:
        elements = c

    cursor.close()
    cnx.close()
    return element


def getAssays(tid):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select * from assays where TID ="+tid)
    assays=[]
    cursor.execute(query)
    for c in cursor:
        assays.append(c[0])
    cursor.close()
    cnx.close()
    return assays

def getActivities(tid):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select * from activities where assay_id ="+tid)
    assays=[]
    cursor.execute(query)
    for c in cursor:
        assays.append(c[3])
    cursor.close()
    cnx.close()
    return assays