

# Overview

This is a little python reporting app I built with [streamlit](https://streamlit.io/).

It is generates custom reports based on input data (nielsen third party data) and emails these reports to users of the app.

The core of this process is the `create_nielsen_reports` function found in the [nielsen_daily.py](nielsen_daily.py) file. The function takes 4 inputs and generates the daily nielsen report in an email it sends to one recipiant.

The program works by reading in 4 raw data files; daily nielsen 15minute data, daily nielsen daypart data, (both provided by the user) benchmark nielsen 15 minute data, and benchmark nielsen daypart data (pre - stored in the back end). The program cleans the data and maps relevant information. Then creates custom charts and tables for each dma based on daily and benchmark data. The program then  embeds these charts and tables into html using a CID for each image, and generates the relevant emails using this html. Finally, it connects to a gmail server and email address and sends the emails to the user. Who can then forward them to people at spectrum.


# Note on Privacy

I've obtained permission to share this code publicly on github, but have been careful to exclude any sensitive business logic or mappings. 

Notably, the primary config file that holds much of the core report information is exlcuded from this exposition. I've also excluded sample data and all other data resources in ~resources/~

I've also exluded the logic that connects to and sends emails from our SMTP server. 

Gitignore:
~~~
# Email Sensitive Files
report_funcs/connect_send_email.py
report_funcs/create_email.py
# Resources
resources/
~~~


## Directory Structure
- [report_funcs/](report_funcs/)  
  All code relating to the main function of this process lives here.  
- [resouces/](resouces/)  
  stores non code but critical files. Most important is [config file](resources\NielsenConfigv4.xlsx), which is an excel file that stores relevant mappings, as well as report details such as email subject lines, dmas to include in each email, and email notes.  
  You will [data/](data/) here, which stores benchmark data files, and [image_dir/](image_dir/) which is where images for the report are temporarily stored.

  
