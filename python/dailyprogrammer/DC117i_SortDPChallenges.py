import sys, re, json, urllib2, time, operator

def get_reddits():
    diff_re     = re.compile('\[([a-z]*?|[A-Z]*?)\]')
    num_re      = re.compile('#\d+')
    title_re    = re.compile('\((.*?)\)')
    url         = 'http://www.reddit.com/r/dailyprogrammer.json?limit=100&after='
    cnt         = 0
    sr_info     = {}

    while True:
        try:
            resp = urllib2.urlopen(url).read()
        except urllib2.HTTPError, e:
            print "Recieved back " + str(e.code) + ": " + str(e.reason)
            sys.exit()
        except urllib2.URLError, e:
            print "Recieved back " + str(e.reason)
            sys.exit()
        data = json.loads(resp)
        for x in data['data']['children']:
            d = diff_re.findall(x['data']['title'])
            if(len(d)):
                n = int(num_re.findall(x['data']['title'])[0].lstrip('#'))
                t = title_re.findall(x['data']['title'])
                if(not len(t)): t = "No Title"
                else: t = t[0]
                sr_info[cnt] = [n, d[0], t, x['data']['url']]
                cnt += 1

        if(data['data']['after'] == None):
            break
        url = 'http://www.reddit.com/r/dailyprogrammer.json?limit=100&after='+data['data']['after']
        time.sleep(5) # Added because I'm super awesome and keep getting 429 errors :-)

    c_alph = "eihdabcfgjklmnopqrstuvwxyz" # Custom alphabet used for sorting difficulties
    # Print out the first list, sorted by number then difficulty.
    for x in sorted(sr_info.items(), key=lambda v: (v[1][0],[c_alph.index(c) for c in v[1][1]])):
        print "["+x[1][1].title()+"] #"+str(x[1][0])+" \'"+x[1][2]+"\' "+x[1][3]
    # Print out the second list, sorted by difficulty then number.
    for x in sorted(sr_info.items(), key=lambda v: ([c_alph.index(c) for c in v[1][1]],v[1][0])):
        print "["+x[1][1].title()+"] #"+str(x[1][0])+" \'"+x[1][2]+"\' "+x[1][3]
    # Print out the total number of challenges
    print "%d Total Challenges" % len(sr_info)

if __name__ == '__main__':
    get_reddits()