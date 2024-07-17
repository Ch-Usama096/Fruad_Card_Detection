import logging
import os 
from datetime import datetime

Log_File = f"{datetime.now().strftime("%m__%d__%y , %h__%m__%s")}.log"
Log_Path = os.path.join(os.getcwd() , "Logs" , Log_File)

print(Log_Path)