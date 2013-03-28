import urllib2
import urlparse
import optparse
import string
from BeautifulSoup import BeautifulSoup


def urls():
    outputfile = open('out_az.csv','w+b')
    i  = 1
    users = []
    
    while i<=400:
        url = "https://vimeo.com/groups/shortfilms/members/page:"+str(i)
        resp = urllib2.urlopen(url)
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent','Mozilla/19.0')]
        resp = opener.open(url)
        response = str(resp.read())
        start = response.find("js-browse_list browse browse_people browse_people_thumbnails")
        end = response.find("</ol>",start)
        parsed_content = response[start:end]
        j = 0
        
        
        while True:
            if 'href="/' in parsed_content[j:]:
                k = parsed_content.find('href="/',j) + 7
                l = parsed_content.find('"',k)
                j = l
                user_id = str(parsed_content[k:l])
                users.append(user_id)
                outputfile.write(user_id + '\n')

            else:
                break
        i = i+1
    print users
    
    outputfile.close()
        
    
