import json

file_1 = open("/Users/aarthy/projects/training/simple-math/json_entries.log", encoding="utf-8", mode="r")
data_1 = json.load(file_1)
#print(data_1)
topic_list = []

print (data_1["count"])
print(len(data_1["entries"]))
if len(data_1["entries"]) == data_1["count"]:
    for entry in data_1["entries"]:
        if entry["Category"] not in topic_list:
            topic_list.append(entry["Category"])
    print(topic_list)

file_2 = open("/Users/aarthy/projects/training/simple-math/data_json_us.log")
data_2 = json.load(file_2)
#print(data_2)

for entry in data_2:
    for item in data_2["data"]:
        print ("Year :" + str(item["Year"]) + "  ;  Population :" + str(item["Population"]))
    for sourceitem in data_2["source"]:
        print ("source_name :" + sourceitem["annotations"]["source_name"] + "  ;  source_description :" + sourceitem["annotations"]["source_description"])