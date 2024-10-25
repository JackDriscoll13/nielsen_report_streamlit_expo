

def save_html_files(generate_html, html_strings, emails, chart_path_dict, table_path_dict): 
    if generate_html: 
        for i in range(len(html_strings)): 
            # Get email details
            subject = emails[i]['subject']
            html = html_strings[i]


            # Replace the cids with the image paths
            for path in chart_path_dict:
                chart_cid = 'cid:'+ ((chart_path_dict[path])[1:-1])
                #newpath = 'C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/' + path # local path
                awspath = '/home/ubuntu/nielsen_refactored/' + path #aws path
                html = html.replace(chart_cid, awspath)

            for path in table_path_dict:
                table_cid = 'cid:'+ ((table_path_dict[path])[1:-1])
                #newpath = 'C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/' + path # local path
                awspath = '/home/ubuntu/nielsen_refactored/' + path #aws path
                html = html.replace(table_cid, awspath)



            with open(f'resources/html_exports/file{i+1}.html', 'w') as file: 
                file.write(f'<p>{subject}</p>' + '<br><hr color="black" size="2" width="100%"><br>' + html)
        print('Done. Html files created in resources/html_exports/')
    else: 
        print('Skipped. No html files created.')




