from datetime import datetime

date_format = '%d/%m/%Y'
date_obj = datetime.strptime("31/12/2023", date_format)


tasks = [
    {"id":1,"title":"Clean my house", "completed":True, "date_created":date_obj},
    {"id":2,"title":"Make a cake","completed":False, "date_created":date_obj},
    {"id":3,"title":"Go to sleep", "completed":False, "date_created":date_obj}
]