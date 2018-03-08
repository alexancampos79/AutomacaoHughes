from iv import iv
iv = iv("normal","E:\AutomaçãoHughes\files","Router","PNT02309",{'vista': 'snmp', 'property':'snmprd', 'value':'public'},"YESYE")

fileModeFile = u"""mode continue on;
mode force on;
"""
delete = iv.delete()
includeBasic = iv.includeBasic()
delete = fileModeFile + delete
includeBasic = fileModeFile + iv.getVista() + iv.getProperties() + iv.getInstance() + iv.includeBasic()

print(includeBasic)