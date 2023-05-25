# from datetime import datetime
#
# date_time_str = '18/09/2019'
#
# date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')
#
#
# print ("The type of the date is now",  type(date_time_obj))
# print ("The date is", date_time_obj)

import re

pattern = '^[0-3]{2}/[0-12]{2}/[0-99]{2}$'
test_string = '32/12/99'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("error")
