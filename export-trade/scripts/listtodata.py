from bs4 import BeautifulSoup

def process(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    response = {}
#    print(html_doc)
    response['data'] = []
#    try:
#        response['total'] = int(soup.find('span', attrs={'class' : "col_oz"}).string[1:-1]) 
#    except AttributeError:
#        response['total'] = 0
#        return response
    tables = soup.findAll('table', attrs={'class' : 'articles'})
    objects = tables[1].findAll('tr')   
    for o in objects[1:]:
        cells = o.findAll('td')
        record = {}
        record['country'] = cells[0].string
        record['year'] = cells[1].string
        record['timeperiod'] = cells[2].string
        record['export'] = cells[3].string  
        record['import_origin'] = cells[4].string  
        record['import_consigment'] = cells[5].string  
        response['data'].append(record)
    print(len(response['data']))
    return response