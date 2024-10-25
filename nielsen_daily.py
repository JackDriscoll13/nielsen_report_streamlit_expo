import report_funcs

def create_nielsen_reports(daily_data_15min_path:str, daily_data_dayparts_path:str, 
                           email_to:str, generate_html:bool, del_image_dir:bool = True): 
    
    ######################
    # Initialize benchmark data 
    benchmark_15min_path = 'resources/data/April Benchmark/Spectrum News - 15 Mins.xlsx'
    benchmark_dayparts_path = 'resources/data/April Benchmark/Spectrum News Dayparts.xlsx'

    # Iniliaze config, read in mappings and info from config
    config_path = 'resources/NielsenConfigv4.xlsx'
    #print('Running Nielsen Report...\nReading config file ->', end =' ')
    daypartsorderDict, chartOrderDict, geomappingDict, stationMappingDict, penetration_dict, sn_names_dict = report_funcs.get_config_mappings(config_path)
    dmalists, emailrecipaints, emailsubjects, emailnotes, emailattachments = report_funcs.get_config_report_info(config_path)

    # print(stationMappingDict)
    print(emailsubjects)
    print('--------------------------------')
    print(emailnotes)
    print('--------------------------------')
    print(emailrecipaints)
    print('--------------------------------')
    print(dmalists)
    #print('Done.')

    # Clean data

    print('Reading in and cleaning data ->',end = ' ')
    benchmark_15min = report_funcs.clean_15min_data(benchmark_15min_path, stationMappingDict, chartOrderDict, geomappingDict)
    benchmark_dayparts = report_funcs.clean_daypart_data(benchmark_dayparts_path, stationMappingDict,geomappingDict,daypartsorderDict)

    daily_data_15min = report_funcs.clean_15min_data(daily_data_15min_path, stationMappingDict, chartOrderDict, geomappingDict)
    daily_data_dayparts = report_funcs.clean_daypart_data(daily_data_dayparts_path, stationMappingDict,geomappingDict,daypartsorderDict)
    print('Done.')
    # ##############################################################################################
    # Initialize directory to dump images
    report_funcs.delete_img_dir(del_image_dir=del_image_dir)
    img_dump_dir = report_funcs.create_img_dir()

    # Configure DMA objects based on specific data generates chart images and table images saved in image dir
    print('Configuring DMA image objects:')
    uniquedmas = {x for i in dmalists for x in i}
    dma_html_dict, chart_path_dict, table_path_dict = report_funcs.create_dma_html(uniquedmas, img_dump_dir, benchmark_15min, benchmark_dayparts, daily_data_15min, daily_data_dayparts, sn_names_dict, penetration_dict)
    print('Done. Succesfully created images and dma html objects.')

    # # Write email 
    print('Creating emails:')
    emails, html_strings = report_funcs.get_email_html(dmalists, email_to, daily_data_15min,
                                emailrecipaints, emailsubjects, emailnotes,
                                 dma_html_dict, chart_path_dict, table_path_dict)

    # Save html files
    print('Saving html files ->', end = ' ')
    report_funcs.save_html_files(generate_html, html_strings, emails, 
                                 chart_path_dict, table_path_dict)

    # Send emails
    print('Sending emails:')
    # # report_funcs.send_email(emails, email_to)
    report_funcs.send_email_gmail(emails, email_to)

    print('All done! Succesfully generated report.')
    


#################################    
# For testing purposes locally: 
if __name__ == '__main__':
    create_nielsen_reports(daily_data_15min_path = 'resources/data/Test Daily Data/Spectrum News - 15 Mins_03-04-2024.xlsx' , daily_data_dayparts_path = 'resources/data/Test Daily Data/Spectrum News Dayparts_03-04-2024.xlsx', 
                           email_to='jack.driscoll@charter.com', generate_html=False)