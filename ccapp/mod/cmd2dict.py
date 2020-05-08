import mklist, ESL

def cmd2dict(cmd):
    con = ESL.ESLconnection('127.0.0.1', '8021', 'ClueCon')
    if con.connected():
       e = con.api(cmd)
       input_str = e.getBody()
       mkl = mklist.MakeListofDicts()
       keys = mkl.extractKeys(input_str)
       values = mkl.extractValues(input_str,0)
       list = mkl.assignKeyValues(keys, values)
    else:
       list = []
    return list     
