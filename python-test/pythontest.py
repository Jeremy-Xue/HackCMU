import cmu_course_api
import json

data = cmu_course_api.get_course_data("S")

with open('test.json','w') as f:
    json.dump(data,f)