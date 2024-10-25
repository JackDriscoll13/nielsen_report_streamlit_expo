import dataframe_image as dfi
from .create_table import create_table
from .create_chart import create_chart, create_chart_dallas

from email.utils import make_msgid

def create_dma_html(unique_dmas, image_folder, benchmark_15min, benchmark_dayparts, daily_data_15min, daily_data_dayparts, sn_names_dict, penetration_dict): 
    # Initiliaze html dictionary and 2 cid dictionaries
    dmas_html_dict = {}
    table_path_dict = {}
    chart_path_dict = {}
    
    # Create a html string for each unique dma
    for dma in unique_dmas: 
        
        print(f'\tDMA: "{dma}" ->', end =' ')

        # Isloate the data 
        avg15min = benchmark_15min[benchmark_15min['DMA']==dma]
        daily15min = daily_data_15min[daily_data_15min['DMA']==dma]
        avgdayparts = benchmark_dayparts[benchmark_dayparts['DMA']==dma]
        dailydayparts = daily_data_dayparts[daily_data_dayparts['DMA']==dma]
        
        # Initialize the dma html 
        dmahtml = '<h3 style="font-size:18px;"> ' + str(dma)  + ' </h3> <b>Ratings by Quarter Hour:</b>'

        # Create the chart
        if dma == 'Dallas/Ft. Worth':
            chart = create_chart_dallas(daily15min, avg15min, sn_names_dict)
        else: 
            chart = create_chart(daily15min, avg15min, sn_names_dict)
        chartpath = image_folder + dma[0:3] + '_chart.png'
        chart_cid = make_msgid(domain = 'NWNYMKNAL334CZ2.CORP.CHARTERCOM.com')
        chart.savefig(chartpath,bbox_inches="tight")
        dmahtml += '<br><img src="cid:{chart_cid}" width="900">'.format(chart_cid=chart_cid[1:-1])  

        # Create the table
        if dma == 'Dallas/Ft. Worth':
            table = create_table(dma,avgdayparts,dailydayparts,KAZD=True)
        else: 
            table = create_table(dma,avgdayparts,dailydayparts)
        tablepath = image_folder + dma[0:3] + '_table.png'
        #dfi.export(table, tablepath, dpi = 500,  chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe') This is the chrome path on my local computer 
        dfi.export(table, tablepath, dpi = 500)
        table_cid = make_msgid(domain = 'NWNYMKNAL334CZ2.CORP.CHARTERCOM.com')
        dmahtml += """
                        <br> <b>Dayparts Table ({dma}):</b> <br>
                        <img src="cid:{table_cid}" width="900">
                        <br>{penetration_sentence}<br><br><hr color="black" size="2" width="100%">
                """.format(table_cid = table_cid[1:-1], dma = dma, penetration_sentence = penetration_dict[dma])
        
        # Save relevant information in the dictionaries
        dmas_html_dict[dma] = dmahtml
        table_path_dict[tablepath] = table_cid
        chart_path_dict[chartpath] = chart_cid

        print('Done.')
    return dmas_html_dict, chart_path_dict, table_path_dict


# if __name__ == '__main__':
#        unique_dmas = {'Cleveland/Akron', 'Orlando/Daytona Beach/Melbourne', 'Los Angeles', 'New York', 'Charlotte', 'Tampa/Saint Petersburg', 'Dallas/Ft. Worth'}
#        create_dma_html2(unique_dmas)