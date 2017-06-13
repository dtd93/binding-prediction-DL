import datetime
import mysql.connector
import numpy as np



def getAllSmiles():
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select molregno, canonical_smiles from compound_structures")
    selecteds=[]
    cursor.execute(query)
    for c in cursor:
        selecteds.append(c)
    return selecteds



def getLigandsChemblId(tid,passw):
    ligands = []
    cnx = mysql.connector.connect(user='root', database='chembl', password=passw)
    cursor = cnx.cursor()
    query = ("select md.chembl_id from assays a, molecule_dictionary md, activities ac where a.TID = '"+tid+"' and md.MOLREGNO=ac.MOLREGNO and ac.ASSAY_ID = a.ASSAY_ID and a.ASSAY_TYPE = 'B' and a.CONFIDENCE_SCORE >= 7;")
    cursor.execute(query)  
    for chemblid in cursor: #Guarda los resultados de la query en la lista ligands
        ligands.append(chemblid[0])
    return ligands


def getLigandsMolregno(tid,passw):
    ligands = []
    cnx = mysql.connector.connect(user='root', database='chembl', password=passw)
    cursor = cnx.cursor()
    query = ("select ac.MOLREGNO from activities ac, assays a where ac.ASSAY_ID = a.ASSAY_ID and a.TID = '"+tid+"' and ac.STANDARD_TYPE = \"IC50\" and ac.STANDARD_UNITS = \"nM\" and ac.STANDARD_VALUE < 10000 and a.ASSAY_TYPE = \"B\" and a.CONFIDENCE_SCORE >= 7")
    cursor.execute(query)  
    for c in cursor: #Guarda los resultados de la query en la lista ligands
        ligands.append(c[0])
    return ligands


# generic function to search on mysql
def getFromTableFieldValue(table, field, val):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select * from "+ table +" where "+ field +" ="+ val)
    selecteds=[]
    cursor.execute(query)
    for c in cursor:
        selecteds.append(c[field])
    cursor.close()
    cnx.close()
    return selecteds

# function hardcoded, selects assays that are type binding, with a target that is a protein
def forceSelectTop():
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select count(*) as c, a.TID from assays a, target_dictionary t, ACTIVITIES ac where t.TID = a.TID and ac.ASSAY_ID = a.ASSAY_ID and (t.TARGET_TYPE = \"PROTEIN FAMILY\" or t.TARGET_TYPE = \"PROTEIN COMPLEX GROUP\" or t.TARGET_TYPE = \"PROTEIN-PROTEIN INTERACTION\" or t.TARGET_TYPE = \"PROTEIN NUCLEIC-ACID COMPLEX\" or t.TARGET_TYPE = \"PROTEIN COMPLEX\") and a.ASSAY_TYPE = \"B\" and a.CONFIDENCE_SCORE = 7 group by a.TID order by c desc limit 1000;")
    nums = np.empty((0))
    tids = np.empty((0))

    cursor.execute(query)
    count = 0
    for c in cursor:
        nums = np.append(nums,c[0])
        tids = np.append(tids,c[1])
        count += 1 
    cursor.close()
    cnx.close()
    return nums, tids


def forceGetCompunds(tid):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select distinct(ac.MOLREGNO) from assays a, ACTIVITIES ac where ac.ASSAY_ID = a.ASSAY_ID and a.ASSAY_TYPE = \"B\" and a.CONFIDENCE_SCORE >= 7 and a.TID =" +tid)
    nums = np.empty((0))
    cursor.execute(query)
    count = 0
    for c in cursor:
        nums = np.append(nums,c[0])
        count += 1 
    cursor.close()
    cnx.close()
    return nums

# get number of distinct compund for target (just from the assays B conf > 7)
def forceGetNumCompunds(tid):
    cnx = mysql.connector.connect(user='root', database='chembl', password='toor')
    cursor = cnx.cursor()
    query = ("select count(distinct(ac.MOLREGNO)) from assays a, ACTIVITIES ac where ac.ASSAY_ID = a.ASSAY_ID and a.ASSAY_TYPE = \"B\" and a.CONFIDENCE_SCORE >= 7 and a.TID =" +tid)
    nums = np.empty((0))
    cursor.execute(query)
    count = 0
    for c in cursor:
        nums = np.append(nums,c[0])
        count += 1 
    cursor.close()
    cnx.close()
    return nums

def minermain():
    print("minermain")