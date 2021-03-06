import json
import urllib
import re

geocode = {"af":[33,65], "al":[41,20], "dz":[28,3], "as":[-14.3333,-170], "ad":[42.5,1.6], "ao":[-12.5,18.5], "ai":[18.25,-63.1667], "aq":[-90,0], "ag":[17.05,-61.8], "ar":[-34,-64], "am":[40,45], "aw":[12.5,-69.9667], "au":[-27,133], "at":[47.3333,13.3333], "az":[40.5,47.5], "bs":[24.25,-76], "bh":[26,50.55], "bd":[24,90], "bb":[13.1667,-59.5333], "by":[53,28], "be":[50.8333,4], "bz":[17.25,-88.75], "bj":[9.5,2.25], "bm":[32.3333,-64.75], "bt":[27.5,90.5], "bo":[-17,-65], "ba":[44,18], "bw":[-22,24], "bv":[-54.4333,3.4], "br":[-10,-55], "io":[-6,71.5], "bn":[4.5,114.6667], "bg":[43,25], "bf":[13,-2], "bi":[-3.5,30], "kh":[13,105], "cm":[6,12], "ca":[60,-95], "cv":[16,-24], "ky":[19.5,-80.5], "cf":[7,21], "td":[15,19], "cl":[-30,-71], "cn":[35,105], "cx":[-10.5,105.6667], "cc":[-12.5,96.8333], "co":[4,-72], "km":[-12.1667,44.25], "cg":[-1,15], "cd":[0,25], "ck":[-21.2333,-159.7667], "cr":[10,-84], "ci":[8,-5], "hr":[45.1667,15.5], "cu":[21.5,-80], "cy":[35,33], "cz":[49.75,15.5], "dk":[56,10], "dj":[11.5,43], "dm":[15.4167,-61.3333], "do":[19,-70.6667], "ec":[-2,-77.5], "eg":[27,30], "sv":[13.8333,-88.9167], "gq":[2,10], "er":[15,39], "ee":[59,26], "et":[8,38], "fk":[-51.75,-59], "fo":[62,-7], "fj":[-18,175], "fi":[64,26], "fr":[46,2], "gf":[4,-53], "pf":[-15,-140], "tf":[-43,67], "ga":[-1,11.75], "gm":[13.4667,-16.5667], "ge":[42,43.5], "de":[51,9], "gh":[8,-2], "gi":[36.1833,-5.3667], "gr":[39,22], "gl":[72,-40], "gd":[12.1167,-61.6667], "gp":[16.25,-61.5833], "gu":[13.4667,144.7833], "gt":[15.5,-90.25], "gg":[49.5,-2.56], "gn":[11,-10], "gw":[12,-15], "gy":[5,-59], "ht":[19,-72.4167], "hm":[-53.1,72.5167], "va":[41.9,12.45], "hn":[15,-86.5], "hk":[22.25,114.1667], "hu":[47,20], "is":[65,-18], "in":[20,77], "id":[-5,120], "ir":[32,53], "iq":[33,44], "ie":[53,-8], "im":[54.23,-4.55], "il":[31.5,34.75], "it":[42.8333,12.8333], "jm":[18.25,-77.5], "jp":[36,138], "je":[49.21,-2.13], "jo":[31,36], "kz":[48,68], "ke":[1,38], "ki":[1.4167,173], "kp":[40,127], "kr":[37,127.5], "kw":[29.3375,47.6581], "kg":[41,75], "la":[18,105], "lv":[57,25], "lb":[33.8333,35.8333], "ls":[-29.5,28.5], "lr":[6.5,-9.5], "ly":[25,17], "li":[47.1667,9.5333], "lt":[56,24], "lu":[49.75,6.1667], "mo":[22.1667,113.55], "mk":[41.8333,22], "mg":[-20,47], "mw":[-13.5,34], "my":[2.5,112.5], "mv":[3.25,73], "ml":[17,-4], "mt":[35.8333,14.5833], "mh":[9,168], "mq":[14.6667,-61], "mr":[20,-12], "mu":[-20.2833,57.55], "yt":[-12.8333,45.1667], "mx":[23,-102], "fm":[6.9167,158.25], "md":[47,29], "mc":[43.7333,7.4], "mn":[46,105], "me":[42,19], "ms":[16.75,-62.2], "ma":[32,-5], "mz":[-18.25,35], "mm":[22,98], "na":[-22,17], "nr":[-0.5333,166.9167], "np":[28,84], "nl":[52.5,5.75], "an":[12.25,-68.75], "nc":[-21.5,165.5], "nz":[-41,174], "ni":[13,-85], "ne":[16,8], "ng":[10,8], "nu":[-19.0333,-169.8667], "nf":[-29.0333,167.95], "mp":[15.2,145.75], "no":[62,10], "om":[21,57], "pk":[30,70], "pw":[7.5,134.5], "ps":[32,35.25], "pa":[9,-80], "pg":[-6,147], "py":[-23,-58], "pe":[-10,-76], "ph":[13,122], "pn":[-24.7,-127.4], "pl":[52,20], "pt":[39.5,-8], "pr":[18.25,-66.5], "qa":[25.5,51.25], "re":[-21.1,55.6], "ro":[46,25], "ru":[60,100], "rw":[-2,30], "sh":[-15.9333,-5.7], "kn":[17.3333,-62.75], "lc":[13.8833,-61.1333], "pm":[46.8333,-56.3333], "vc":[13.25,-61.2], "ws":[-13.5833,-172.3333], "sm":[43.7667,12.4167], "st":[1,7], "sa":[25,45], "sn":[14,-14], "rs":[44,21], "sc":[-4.5833,55.6667], "sl":[8.5,-11.5], "sg":[1.3667,103.8], "sk":[48.6667,19.5], "si":[46,15], "sb":[-8,159], "so":[10,49], "za":[-29,24], "gs":[-54.5,-37], "es":[40,-4], "lk":[7,81], "sd":[15,30], "sr":[4,-56], "sj":[78,20], "sz":[-26.5,31.5], "se":[62,15], "ch":[47,8], "sy":[35,38], "tw":[23.5,121], "tj":[39,71], "tz":[-6,35], "th":[15,100], "tl":[-8.55,125.5167], "tg":[8,1.1667], "tk":[-9,-172], "to":[-20,-175], "tt":[11,-61], "tn":[34,9], "tr":[39,35], "tm":[40,60], "tc":[21.75,-71.5833], "tv":[-8,178], "ug":[1,32], "ua":[49,32], "ae":[24,54], "gb":[54,-2], "us":[38,-97], "um":[19.2833,166.6], "uy":[-33,-56], "uz":[41,64], "vu":[-16,167], "ve":[8,-66], "vn":[16,106], "vg":[18.5,-64.5], "vi":[18.3333,-64.8333], "wf":[-13.3,-176.2], "eh":[24.5,-13], "ye":[15,48], "zm":[-15,30], "zw":[-20,30]}

def fetchFile(url): 
    f = urllib.urlopen(url)
    # Get the headers and extract last/next headers
    headers = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", str(f.info()) ))
    links_list = dict(re.findall(r"\<(?P<value>.*?)\>; rel=\"(?P<name>.*?)\"", headers["Link"] ))
    links = {v: k for k, v in links_list.items()}
    return {"data": f.read(), "links":links }

# For now we just validate to remove spaces etc. 
# In future we should validate against a set codelist
def validateTags(item):
    returnTags = {"tags":{"freeTags":[]}}
    for tag in item['data']['tags']:
        smartTag = tag['tag'].split(":")
        try:
            if " " in smartTag[1]:
                print "ERROR. Space found in " + smartTag[0] +" tag for item " + item['key'] #ToDo - improve error handling
                tagValue = smartTag[1].replace(" ","-")
            else:
                tagValue = smartTag[1]
                
            try:
                returnTags['tags'][smartTag[0]].append(tagValue)
            except KeyError:
                returnTags['tags'].update({smartTag[0]: [tagValue]})
        except IndexError:
            returnTags['tags']['freeTags'].append(smartTag[0])

    return returnTags

def exhibitNode(note,tags):
    if note['data']['itemType'] == "attachment":
        itemType = "Attachment"
    elif note['data']['itemType'] == "note":
        itemType = "Note"
    elif note['data']['itemType'] == "webpage":
        itemType = "Web Page"
    else:
        itemType = "Publication"

    
    try:
        article = {}
        article = lookup[str(note['data']['parentItem'])]
        print "Found article"
        eItem = {
                     "id":note['key'],
                     "key":note['key'],
                     "note":note['data'].get("note",''),
                     "itemID":article.get('id'),
                     "type":itemType,
                     "itemType":itemType,
                     "label":"Note on '" + article.get('label','unknown item') + "'",
                     "article":article.get('label','Unknown Item') + "'",
                     "date":article.get('date',''),
                     "url":article.get('url',''),
                     "publication":article.get('publication',''),
                     "latlng":article.get('latlng',''),
                     "period":article.get('period',''),
                     "focus": article.get('users',''),
                     "stage": article.get('stage',''),
                     "method": article.get('method',''),
                     "sector": article.get('sector',''),
                     "impact-sector": article.get('impact-sector',''),
                     "impact": article.get('impact',''),
                     "author": article.get('author',''),
                     "geo": article.get('geo',''),
           }
        for k, v in tags['tags'].iteritems():
           if len(v) == 1:
               eItem.update({k:v[0]})
           else:
               eItem.update({k:v})

           if(k == "geo"):
               for c in v:
                   try:
                       geo.append(str(geocode[c][0]) + "," + str(geocode[c][1]))
                   except:
                       pass
           
    except:
        eItem = {"data":{}}
    
    return eItem





def crawlZotero(group,query):
    url = "https://api.zotero.org/groups/"+str(group)+"/items/?v=3&"+query

    while True:
        zoteroData = fetchFile(url)
        jsonData = json.loads(zoteroData['data'])

        for item in jsonData:
            tags = validateTags(item)
            exhibitJson['items'].append(exhibitNode(item,tags))

        if zoteroData['links'].get('next',''):
            print "Fetching next" + zoteroData['links']['next']
            url = zoteroData['links']['next']
        else:
            break;

exhibitJson = json.loads(open('exhibit/template.json').read())
lookup = json.loads(open('lookup.json').read())

## For now we're not fetching notes
crawlZotero(164662,"itemType=note")


open('exhibit/notes.json','w').write(json.dumps(exhibitJson, indent=4, separators=(',', ': ')))