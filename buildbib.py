import json
import urllib
import re

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

def exhibitNode(item,tags):
    if item['data']['itemType'] == "attachment":
        itemType = "Attachment"
    elif item['data']['itemType'] == "note":
        itemType = "Note"
    elif item['data']['itemType'] == "webpage":
        itemType = "Web Page"
        
    else:
        itemType = "Publication"

    eItem = {
        "id":item['key'],
        "key":item['key'],
        "type":itemType,
        "itemType":item['data']['itemType'],
        "label":item['data']['title'],
        "date":item['data'].get('date',''),
        "abstract":item['data'].get('abstractNote',''),
        "url":item['data'].get('url',''),
        "doi":item['data'].get('doi',''),
        "place":item['data'].get('place',''),
        "publisher":item['data'].get('publisher',''),
        "volume":item['data'].get('volume',''),        
        "issue":item['data'].get('issue',''),        
        "pages":item['data'].get('pages',''),        
        "publication":item['data'].get('publicationTitle',item['data'].get('proceedingsTitle',''))
    }
    
    for k, v in tags['tags'].iteritems():
        if len(v) == 1:
            eItem.update({k:v[0]})
        else:
            eItem.update({k:v})
    
    try:
        authors = []
        for creator in item['data']['creators']:
            authors.append(creator.get('lastName','') + ", " + creator.get('firstName'))
        eItem.update({"author":authors})
    except KeyError:
        #No Authors
        pass
    
    return eItem





def crawlZotero(group,query):
    url = "https://api.zotero.org/groups/"+str(group)+"/items/?v=3&"+query

    while True:
        zoteroData = fetchFile(url)
        jsonData = json.loads(zoteroData['data'])

        for item in jsonData:
            if item['data'].get('extra','') == 'coded' or 'candidate' in item['data'].get('extra',''):
                tags = validateTags(item)
                exhibitJson['items'].append(exhibitNode(item,tags))

        if zoteroData['links'].get('next',''):
            print "Fetching next" + zoteroData['links']['next']
            url = zoteroData['links']['next']
        else:
            break;


exhibitJson = json.loads(open('exhibit/template.json').read())

## For now we're not fetching notes
crawlZotero(164662,"itemType=-note")


open('exhibit/data.json','w').write(json.dumps(exhibitJson, indent=4, separators=(',', ': ')))