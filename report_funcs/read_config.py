### These functions read in mappings and other relevant info from our master config file.

import pandas as pd


def get_config_mappings(config_file_path:str): 
    """
    Read in important data mappings from our config file. 
    Return those mappings as dictionaries. 
    """   
    # Dayparts Order
    daypartsorder = pd.read_excel(config_file_path,sheet_name='Dayparts Order')
    daypartsorderDict = daypartsorder.set_index('Daypart')['Order in Report Table'].to_dict()

    # X axis order
    chartOrder = pd.read_excel(config_file_path,sheet_name='Xaxis Order')
    chartOrderDict = chartOrder.set_index('Time')['Order in X axis'].to_dict()

    # Mapping of Nielsen Geographies to DMA:
    geomapping = pd.read_excel(config_file_path,sheet_name='Geo Mapping')
    geomappingDict = geomapping.set_index('Neilsen Name')['Ending Name'].to_dict()

    # Mapping of Station to Affiliate Network:
    stationMapping = pd.read_excel(config_file_path,sheet_name='Station Mapping')
    stationMappingDict = stationMapping.set_index('Station Name')['Network'].to_dict()

    # Penetration mapping by DMA, to be placed at bottom of DMA section in email 
    penetrationMapping = pd.read_excel(config_file_path,sheet_name='Penetration Mapping')
    penetrationMappingDict =  penetrationMapping.set_index('DMA')['Penetration %'].to_dict()

    snNamesMapping = pd.read_excel(config_file_path,sheet_name='Spectrum Station Names')
    snNamesMapppingDict = snNamesMapping.set_index('Station Abbr.')['Station Name Full'].to_dict()

    return daypartsorderDict, chartOrderDict, geomappingDict, stationMappingDict, penetrationMappingDict, snNamesMapppingDict



def get_config_report_info(config_file_path:str): 
    """
    Read important info about details of each report from the config file.
    """

    # Dma list
    dmadf = pd.read_excel(config_file_path,sheet_name='DMA List')
    dmalists = []
    for col in dmadf.columns:
        emaildma =  dmadf[col].dropna().to_list()
        dmalists.append(emaildma)

    # email list 
    emaildf = pd.read_excel(config_file_path,sheet_name='Email List')
    emailto = []
    for col in emaildf.columns:
        emaillist =  emaildf[col].dropna().to_list()
        emailto.append(emaillist)

    # subject list 
    subjectdf = pd.read_excel(config_file_path,sheet_name='Email Subject Lines')
    emailsubjects = []
    for col in subjectdf.columns:
        emailsubject =  subjectdf[col].dropna().to_list()[0]
        emailsubjects.append(emailsubject)

    # Email notes
    notesdf = pd.read_excel(config_file_path,sheet_name='Email Notes')
    emailnotes = []
    for col in notesdf.columns:
        emailnote =  notesdf[col].dropna().to_list()[0]
        emailnotes.append(emailnote)

    attachmentdf = pd.read_excel(config_file_path,sheet_name='Email Attachments')
    
    emailattachments = []
    for col in attachmentdf.columns:
        attachments =  attachmentdf[col].dropna().to_list()
        emailattachments.append(attachments)
        
    return dmalists, emailto, emailsubjects, emailnotes, emailattachments