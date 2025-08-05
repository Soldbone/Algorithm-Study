from datetime import datetime
now = datetime.now()

from datetime import datetime, timezone

date = datetime.now(timezone.utc) 

print(date.year, str(date.month).zfill(2), str(date.day).zfill(2), sep='\n')