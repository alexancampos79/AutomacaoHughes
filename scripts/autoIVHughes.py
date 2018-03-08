import os
import sys
import datetime
import configparser

class iv:
    
    def __init__(self,ppath,pvista,pinstName,pproperties):
        self.path = ppath
        self.vista = pvista
        self.instName = pinstName
        self.properties = pproperties

    def __del__(self):
        print('Deletando objeto IV')
    
    def deleteBasic(self):
        deleteFile = 'mode continue on;'\
                    '\rmode force on;'\
                    '\n'\
                    '\rquery vista name = \"' + iv.vista + '\";\n'\
                    '\rif ($vista = $null) begin\n'\
                    '\techo "error line 4: \\"' + iv.vista + '\\", no such vista";\n'\
                    "\texit;\n"\
                    '\rend;\n'\
                    '\rassign $V_' + iv.vista + '= $vista;'\
                    '\n\n'\
                    '\rquery instance name = "' + iv.instName + '", vistas = [$V_' + iv.vista + '];\n'\
                    '\rif ($vista = $null) begin\n'\
                    '\techo "error line 5: \\"' +  iv.instName + '\\", no such instance";\n'\
                    '\texit;\n'\
                    '\relse\n'\
                    '\tremove instance $instance;\n'\
                    '\tif ($? <> $success) begin\n'\
                    '\t\techo "error line 5: Cannot remove instance \\"' +iv.instName + '\\"";\n'\
                    '\t\texit;\n'\
                    '\tend;\n'\
                    '\rend;'

        iv.writeFile("deleteBasic",deleteFile)

    def deleteProxy(self):
        deleteFile = 'mode continue on;'\
                    '\rmode force on;'\
                    '\n'\
                    '\rquery vista name = \"' + iv.vista + '\";\n'\
                    '\rif ($vista = $null) begin\n'\
                    '\techo "error line 4: \\"' + iv.vista + '\\", no such vista";\n'\
                    "\texit;\n"\
                    '\rend;\n'\
                    '\rassign $V_' + iv.vista + '= $vista;'\
                    '\n\n'\
                    '\rquery instance name = "' + iv.instName + '", vistas = [$V_' + iv.vista + '];\n'\
                    '\rif ($vista = $null) begin\n'\
                    '\techo "error line 5: \\"' +  iv.instName + '\\", no such instance";\n'\
                    '\texit;\n'\
                    '\relse\n'\
                    '\tremove instance $instance;\n'\
                    '\tif ($? <> $success) begin\n'\
                    '\t\techo "error line 5: Cannot remove instance \\"' +iv.instName + '\\"";\n'\
                    '\t\texit;\n'\
                    '\tend;\n'\
                    '\rend;'

        iv.writeFile("deleteProxy",deleteFile)

    def writeFile(self,pnameFile,pcontentFile):
        self.nameFile = pnameFile
        self.contentFile = pcontentFile
        os.chdir(os.path.dirname(sys.argv[0]))
        path = os.path.dirname(os.getcwd())
        iv.dateF()
        pathFile = path + '/files/' + iv.nameFile + '_' + iv.date +'.ivc'       
        file = open(pathFile, 'w')
        file.write(iv.contentFile)
        file.close()        

    def dateF(self):
        today = datetime.datetime.now()
        self.date = today.strftime('%d%m%Y%H%M%S%f')


os.chdir(os.path.dirname(sys.argv[0]))
pathIni = os.path.dirname(os.getcwd())
pathFileIni = pathIni + '/config/'
FileIniDeleteRouter = pathFileIni + 'deleteRouter.ini'
FileIniDeleteIPGW = pathFileIni + 'deleteIPGW.ini'
FileIniDeleteProxy = pathFileIni + 'deleteProxy.ini'
try:
    iniDeleteRouter = configparser.ConfigParser()
    iniDeleteIPGW = configparser.ConfigParser()
    iniDeleteProxy = configparser.ConfigParser()
    iniDeleteRouter.read(FileIniDeleteRouter)
    iniDeleteIPGW.read(FileIniDeleteIPGW)
    iniDeleteProxy.read(FileIniDeleteProxy)
    vistaDeleteRouter = iniDeleteRouter.get('VISTA','Name')
    libraryDeleteRouter = iniDeleteRouter.get('LIBRARY','Name')
    vistaDeleteIPGW = iniDeleteIPGW.get('VISTA','Name')
    libraryDeleteIPGW = iniDeleteIPGW.get('LIBRARY','Name')
    vistaDeleteProxy = iniDeleteProxy.get('VISTA','Name')
    libraryDeleteProxy = iniDeleteProxy.get('LIBRARY','Name')
except configparser.NoOptionError as err:
    print(err)

iv = ivBasic("normal",libraryDeleteProxy,vistaDeleteProxy,"PNT02309")      
iv.deleteProxy()
del iv
iv = ivBasic("normal",libraryDeleteRouter,vistaDeleteRouter,"CX-PNT02309")      
iv.deleteBasic()
del iv
iv = ivBasic("normal",libraryDeleteIPGW,vistaDeleteIPGW,"IPGW-TESTE")      
iv.deleteBasic()
del iv