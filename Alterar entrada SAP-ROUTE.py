from getpass import getuser
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import messagebox

#função da janela POP
def popup_completed(mensagem, e="Aviso"):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(e, mensagem)
#função para alterar arquivo XML
def alterar_arquivo_xml(caminho):
    # Abrir o arquivo XML
    tree = ET.parse(caminho)
    root = tree.getroot()

    # Procurar a tag <Service> com o atributo 'name' igual a 'S4P'
    for service in root.iter('Service'):
        if service.get('server') == 'vhpats4pci.sap.patrimar.com.br:3200':
            # Alterar os atributos da tag <Service>
            service.set('name', 'S4P')
            service.set('server', 'PUBLIC')
            #remove os atributos
            service.attrib.pop('mode', None)
            service.attrib.pop('sncop', None)
            service.attrib.pop('routerid', None)
            #adiciona novos atributos
            service.set('msid', 'bf19a9e2-f820-4ab6-b47d-9efd33fef09c')
            service.set('sncname', 'p:CN=S4P, OU=SAP-HEC, O=SAP SE, C=DE')

            # Adicionar a nova tag <Messageservers>
            messageservers = ET.SubElement(root, 'Messageservers')
            messageserver = ET.SubElement(messageservers, 'Messageserver')
            messageserver.set('uuid', 'bf19a9e2-f820-4ab6-b47d-9efd33fef09c')
            messageserver.set('name', 'S4P')
            messageserver.set('host', 'vhpats4pci.sap.patrimar.com.br')
            messageserver.set('port', '3601')
    # Salvar as alterações no arquivo XML
    tree.write(caminho)

user = getuser()
arquivo = f'C:\\Users\\{user}\\AppData\\Roaming\\SAP\\Common\\SAPUILandscape.xml'
try:
    alterar_arquivo_xml(arquivo)    
    popup_completed("Entrada SAP alterada com Sucesso!", e="Concluido")
except Exception as error_log:
    popup_completed(f"Não foi possivel alterar a entrada SAP \n\n {error_log}", e="Error")
