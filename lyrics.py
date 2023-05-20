import lyricsgenius
import json
import sys
args = sys.argv[1:]
args = str(args).replace("[","").replace("]","").replace(",","").replace("'","")
def kufurvarmi(lyrics):
    g = open("karaliste.json","r").readline()
    f = json.loads(g)
    for s in f:
        if(lyrics == s):
            return True
    
    return False
genius = lyricsgenius.Genius("")
genius.verbose = False #Konsola yazdırmasını kapattım
genius.response_format =  'plain'
lyr = genius.search_song(args)
jsonv = json.loads(lyr.to_json())
s = jsonv['lyrics']
c = s.split()

#print(jsonv['lyrics'])

kufur = False
for d in c:
    d = d.lower()
    kfrvrmı = kufurvarmi(d)
    if(kfrvrmı == True):
        kufur = True
#print(lyrs)
print(kufur)
#print(lyr.lyrics)