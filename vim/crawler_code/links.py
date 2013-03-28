import urllib2
import urllib
import time 

def links():
    j = 0
    output = open("result.csv",'w+b')
    lines = [line.strip() for line in open('out_az.csv')]
    for i in lines:
        feature_videos = []
        http_code = []
        url = "https://vimeo.com/"+str(i)
        if urllib.urlopen(url).getcode() == 404:
            continue
        else:
        
    ##        i= 'eterea'
    ##        url = 'http://vimeo.com/eterea'
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent','Mozilla/19.0')]
            resp = opener.open(url)
            response = str(resp.read())
        ##        print response
            start = response.find("<header>")
            end = response.find("</header>", start)
            name_parse = response[start:end]
            start = name_parse.find('itemprop="name">') + 16
            end = name_parse.find('</span>',start)
            name = str(name_parse[start:end])
            
            if '<span class="badge_plus">' in name_parse:
                paying = 'YES'
            else:
                paying = 'NO'
            
            start = response.find('block floated_list stat_list bubble_list nipple_left')
            end = response.find('</section>',start)
            video_parse = response[start:end]
            if '<a href="/'+i+'/videos" class="empty"' in video_parse:
                videos = 'No'
            else:
                videos = 'Yes'
            
            start = response.find('<div class="featured_videos"')
            end = response.find('</section>',start)
            feature_parse = response[start:end]
            
        ##    print feature_parse
            x = 0
            while True:
                if '<a href="/' in feature_parse[x:]:
                    start = feature_parse.find('<a href="/',x) + 10
                    end = feature_parse.find('"', start)
                    feature = feature_parse[start:end]
                    x = end
                    print feature
                    feature_videos.append(feature)
                else:
                    break
            for i in feature_videos: 
                sp_url = "https://vimeo.com/channels/staffpicks/"+i
                resp = urllib.urlopen(sp_url).getcode()
                http_code.append(resp)
            if 200 in http_code:
                staff_pick = 'yes'
            else:
                staff_pick = 'No'
            
            output.write(name+','+url+','+paying+','+videos+','+staff_pick+'\n')
            print name,url,paying,videos,staff_pick
            j = j+1
            if j == 51:
                time.sleep(600)
                j = 0
                
            
    output.close()
                

        
        
