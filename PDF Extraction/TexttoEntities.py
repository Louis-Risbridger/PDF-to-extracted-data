import spacy
nlp = spacy.load("en_core_web_sm")


#Getting txt tokenised
f = open("Converted.txt", "r", encoding="utf-8")
text = f.read()
doc = nlp(text)


columns =2
rows=500
entities = [[0 for x in range(columns)] for x in range(rows)]

for ent in doc.ents:
    for i in range(rows):
        if entities[i][0] == 0:
            entities[i][0] = ent.text
            entities[i][1] += 1 
            break
        elif entities[i][0] == ent.text:
            entities[i][1] += 1
            break
            
entToken = []            
for i in range(rows-1):
    entToken.append( (str(entities[i][0]) + " : " + str(entities[i][1])) )
                
print("Succcess")
    
outfile = open("Entities.txt", "w+", encoding="utf-8")
for line in entToken:
    outfile.write(line + "\n") 
outfile.close()  

            
