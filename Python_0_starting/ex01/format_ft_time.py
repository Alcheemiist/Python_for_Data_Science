import time
from datetime import datetime

epoch = time.time()

print("Seconds since January 1, 1970: {0:.4f} or {0:.2e} in scientific notation".format(epoch))

date_str = datetime.fromtimestamp(epoch).strftime('%b %d %Y')

print(date_str)