import pandas as pd

excel_file_content = pd.read_excel("/Users/aarthy/projects/training/simple-math/file_example_XLS_5000.xls")
excel_file_content = excel_file_content.drop_duplicates(subset=["Id"], keep="first")
#print(excel_file_content)
subset =  pd.DataFrame(excel_file_content, columns=["First Name", "Last Name", "Id"])
#print(subset.sort_values(by=["First Name", "Last Name", "Id"]))
print(excel_file_content.nsmallest(20, ["Id"], "first"))
print(excel_file_content.nlargest(20, ["Id"], "first"))