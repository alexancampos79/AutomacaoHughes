import os
import sys

class iv:
    
    def __init__(self,ptype,ppath,pvista,pinstName,pproperties,preports):
        self.type = ptype
        self.path = ppath
        self.vista = pvista
        self.instName = pinstName
        self.propertiesName = pproperties['property']
        self.propertiesValue = pproperties['value']
        self.vistaProperty = pproperties['vista']
        self.reports = preports

    def __del__(self):
        print('Deletando objeto IV')   

    def delete(self):         
        deleteFile = u"""query vista name = "{vista}";
        if ($vista = $null) begin
            echo "error line 4: + \\"{vista}\\" , no such vista";
            exit;
        end;
        assign $V_{vista} = $vista;
        query instance name = "{instName}" , vistas = [$V_{vista}];
        if ($instance = $null) begin
            echo "error line 5: \\"{instName}\\", no such instance";
            exit;
        else
            remove instance $instance;
            if ($? <> $success) begin
                echo "error line 5: Cannot remove instance \\"{instName}\\"";
                exit;
            end;
        end;

        """.format(vista=self.vista,instName=self.instName)
        return deleteFile

    def getVista(self):  
        getVistaFile = u"""query vista name = "{vista}";
        if ($vista = $null) begin
            echo "error line 2: \\"{vista}\\", no such vista";
            exit;
        end;
        assign $V_{vista} = $vista;

        """.format(vista=self.vista)
        return getVistaFile

    def getProperties(self):  
        getPropertiesFile = u"""query vista name = "{vista}";
        if ($vista = $null) begin
            echo "error line 2: \\"{vista}\\", no such vista";
            exit;
        end;
        assign $V_{vista} = {vista}   

        query property vista = $V_{vista}, name = "{propertyName}";
        if ($property = $null) begin
            echo "error line : \\"{propertyName}\\" for vista: \\"{vista}\\", no such property";
            exit;
        else
	        assign $_{vista}_{propertyName}PId = $property;
        end;
        assign $setProperties = 1;

        """.format(vista=self.vistaProperty, propertyName=self.propertiesName)
        return getPropertiesFile
    
    def getInstance(self):
        getInstanceFile = u"""query instance name = "{instName}", vistas = [{vista}];

        """.format(instName=self.instName, vista=self.vista)
        return getInstanceFile
    
    def getReport(self):
        self.vista 

    def includeBasic(self):  
        includeBasicFile = u"""if ($instance <> $null) begin
	        assign $action = "set";
	        assign $I_{instName}_{vista} = $instance;
        else
	        assign $action = "create";
        end;

        if ($action = "create") begin
	        create instance name = "{instName}",
		        vistas = [$V_{vista}];
	        assign $I_{instName}_{vista} = $instance;
        end;

        if ($setProperties = 1) begin
	        query propertyvalue instance=$I_{instName}_{vista}, property=$_{vistaProperty}_{propertyName}PId;
	        set propertyvalue $propertyvalue value= "{propertyValue}";

        end;

        """.format(instName=self.instName, vista=self.vista,propertyName=self.propertiesName,vistaProperty=self.vistaProperty,propertyValue=self.propertiesValue)
        return includeBasicFile

    def includeProxy(self):
        self.vista        

    def startReport(self):
        self.vista
    