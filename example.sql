select count(*) as c, a.TID from assays a, target_dictionary t, ACTIVITIES ac where t.TID = a.TID and ac.ASSAY_ID = a.ASSAY_ID and (t.TARGET_TYPE = "PROTEIN FAMILY" or t.TARGET_TYPE = "PROTEIN COMPLEX GROUP" or t.TARGET_TYPE = "PROTEIN-PROTEIN INTERACTION" or t.TARGET_TYPE = "PROTEIN NUCLEIC-ACID COMPLEX" or t.TARGET_TYPE = "PROTEIN COMPLEX") and a.ASSAY_TYPE = "B" and a.CONFIDENCE_SCORE = 7 group by a.TID order by c desc limit 10;
+------+--------+
| c    | TID    |
+------+--------+
| 2345 | 104717 |
| 2036 | 104290 |
| 1763 | 104294 |
| 1208 | 104283 |
| 1125 | 104292 |
| 1055 | 104710 |
|  982 | 104293 |
|  939 | 104685 |
|  697 | 105083 |
|  689 | 104288 |
+------+--------+



select count(distinct(ac.MOLREGNO)) as c, a.TID from assays a, target_dictionary t, ACTIVITIES ac where t.TID = a.TID and ac.ASSAY_ID = a.ASSAY_ID and (t.TARGET_TYPE = "PROTEIN FAMILY" or t.TARGET_TYPE = "PROTEIN COMPLEX GROUP" or t.TARGET_TYPE = "PROTEIN-PROTEIN INTERACTION" or t.TARGET_TYPE = "PROTEIN NUCLEIC-ACID COMPLEX" or t.TARGET_TYPE = "PROTEIN COMPLEX") and a.ASSAY_TYPE = "B" and a.CONFIDENCE_SCORE >= 7 group by a.TID order by c desc limit 10;
+------+--------+
| c    | TID    |
+------+--------+
| 1368 | 104290 |
| 1367 | 104717 |
| 1211 | 104294 |
|  868 | 104292 |
|  815 | 104710 |
|  807 | 104685 |
|  729 | 104283 |
|  592 | 104293 |
|  526 | 104702 |
|  501 | 104690 |
+------+--------+

select count(distinct(ac.MOLREGNO)) from activities ac, assays a where ac.ASSAY_ID = a.ASSAY_ID and a.TID = 104290 and ac.STANDARD_TYPE = "IC50" and ac.STANDARD_VALUE < 10000 and a.ASSAY_TYPE = "B" and a.CONFIDENCE_SCORE >= 7;
+------------------------------+
| count(distinct(ac.MOLREGNO)) |
+------------------------------+
|                           79 |
+------------------------------+


select count(distinct(ac.MOLREGNO)) as c, a.TID from assays a, target_dictionary t, ACTIVITIES ac where t.TID = a.TID and ac.ASSAY_ID = a.ASSAY_ID and (t.TARGET_TYPE = "PROTEIN FAMILY" or t.TARGET_TYPE = "PROTEIN COMPLEX GROUP" or t.TARGET_TYPE = "PROTEIN-PROTEIN INTERACTION" or t.TARGET_TYPE = "PROTEIN NUCLEIC-ACID COMPLEX" or t.TARGET_TYPE = "PROTEIN COMPLEX") and a.ASSAY_TYPE = "B" and a.CONFIDENCE_SCORE >= 7 group by a.TID order by c desc limit 10;
+------+--------+
| c    | TID    |
+------+--------+
| 1368 | 104290 |
| 1367 | 104717 |
| 1211 | 104294 |
|  868 | 104292 |
|  815 | 104710 |
|  807 | 104685 |
|  729 | 104283 |
|  592 | 104293 |
|  526 | 104702 |
|  501 | 104690 |
+------+--------+

select count(*), ac.STANDARD_TYPE from activities ac, assays a where ac.ASSAY_ID = a.ASSAY_ID and a.TID = 104290 and a.ASSAY_TYPE = "B" and a.CONFIDENCE_SCORE >= 7 group by ac.STANDARD_TYPE;
+----------+---------------+
| count(*) | STANDARD_TYPE |
+----------+---------------+
|       53 | Activity      |
|       12 | Affinity      |
|        7 | EC50          |
|        1 | Efficacy      |
|       13 | Emax          |
|      111 | IC50          |
|       17 | Imax          |
|      104 | Inhibition    |
|        2 | Kd            |
|     1656 | Ki            |
|       47 | pKi           |
|       11 | Ratio Ki      |
|        2 | Rmax          |
+----------+---------------+


select count(ac.MOLREGNO) from activities ac, assays a where ac.ASSAY_ID = a.ASSAY_ID and a.TID = 104717 and ac.STANDARD_TYPE = "IC50" and ac.STANDARD_UNITS = "nM" and ac.STANDARD_VALUE < 10000 and a.ASSAY_TYPE = "B" and a.CONFIDENCE_SCORE >= 7;
+--------------------+
| count(ac.MOLREGNO) |
+--------------------+
|               1524 |
+--------------------+