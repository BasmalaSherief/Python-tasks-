import pandas as pd
import re 

data = {
    "Index" : [],
    "Prototype" : []
}

with open("LCD_Driver.h", "r") as fl:
    lines = fl.readlines()
    
pattern = r'^\s*[a-zA-Z_][a-zA-Z0-9_ \t\*]*\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(.*\)\s*;'

index_counter = 0
for line in lines:
    if re.match(pattern,line):
        prototype = line.strip()
        data["Prototype"].append(prototype)
        data["Index"].append(f"IDX{index_counter}")
        index_counter += 1

df = pd.DataFrame(data)        
df.to_excel('Documentation.xlsx', index = False)

def read_excel(file_name):
    return pd.read_excel(file_name)

print(read_excel('Documentation.xlsx'))

