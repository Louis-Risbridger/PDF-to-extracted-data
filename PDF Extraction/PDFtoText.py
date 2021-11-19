import fitz

#Ask user for the document name and makes sure the input is a pdf
flag = False
while flag == False:
    file = input("Please input the PDF you would like to extract data from(Please Include the '.pdf') \n")
    if file[len(file)-4:] == ".pdf":
        flag = True

print("Valid PDF name")
text = ""

#getting pdf and turning into a long string while makeing sure the file is there

try:    
    with fitz.open(file) as doc:
        for page in doc:
            text += page.get_text()
except:
    print("File was not found")
    
outfile = open("Converted.txt", "w+", encoding="utf-8")
for line in text:
    outfile.write(line) 
outfile.close()    
