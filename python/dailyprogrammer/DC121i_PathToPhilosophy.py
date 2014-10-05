# Clicking on the first link in the main text of a Wikipedia article 
# not in parentheses or italics, and then repeating the process for 
# subsequent articles, usually eventually gets you to the Philosophy 
# article. As of May 26, 2011, 94.52% of all articles in Wikipedia 
# lead eventually to the article Philosophy. The rest lead to an 
# article with no wikilinks or with links to pages that do not exist, 
# or get stuck in loops. Here's a Youtube video demonstrating this phenomenon.
# Your goal is to write a program that will find the path from a given 
# to the Philosophy article by following the first link (not in parentheses, 
# italics or tables) in the main text of the given article. Make sure you 
# have caching implemented from the start so you only need to fetch each page once.
# You will then extend the program to do a depth-first search in search of 
# the Philosophy article, backtracking if you get stuck and quitting only 
# when you know there is no such path. The last thing you will do is generalise 
# it to do a DFS towards any goal article.
# Hint: Yes, there is a Wikipedia API. Feel free to use it.

# Sample Input:
# From: Molecule
# To: Philosophy

# Sample Output:
# Molecule
# Atom
# Matter
# Invariant mass
# Energy
# Kinetic energy
# Physics
# Natural philosophy
# Philosophy # Challenge Input

import sys, urllib.error, urllib.parse, urllib.request, json, re

def crawl_wiki(s,d):
    # Compile the regex and construct the initial URL
    data        = urllib.parse.urlencode({'name':'poppyseedplehzr','location':'interwebs','language':'Python'})
    headers     = { 'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17" }
    cnt         = 0
    s_regex     = re.compile('[\w ]{1}\[\[[^\]]+\]\]{1}[\w ,.\']{1}')
    p_regex     = re.compile('[^\)]*\(')
    #s_regex     = re.compile('[ ,.\w]{1}\[\[[^\]]+\]\]{1}[ ,.\w]{1}')
    history  = set()
    
    #traversals[cnt] = s
    # Begin the main traversal
    while (s.lower() != "philosophy"):
        wiki_url    = "http://en.wikipedia.org/w/index.php?printable=yes&title=" + s
        try:
            req     = urllib.request.Request(wiki_url,data,headers)
            resp    = urllib.request.urlopen(req)
            page    = resp.read()    
            #enc  = resp.headers.get_content_charset()
            print(page)
        except(urllib.error.HTTPError as e):
            print("ERROR:  ", + e.reason)
            sys.exit()
        except(urllib.error.URLError as e):
            print("ERROR:  ", e.reason)
            sys.exit()
        # data   = json.loads(resp.readall().decode(enc))
        # page   = list(data["query"]["pages"].keys())[0]
        # title  = data["query"]["pages"][page]["title"]
        # body   = list(data["query"]["pages"][page]["revisions"])[0]["*"]
        
        # if(body.startswith("#REDIRECT")):
            # #s = body.split(' [[')[1].rstrip(']]').replace(' ','%20')
            # s = body.split(' [[')[1].rstrip(']]').replace(' ','_')
        # else:
            # print("Crawled to " + title)
            # #init_string = r"'''" + re.escape(s.replace('%20',' ')) + r"'''"
            # s = s.replace('_',' ').split()
            # if(len(s) > 1):
            # init_string = r"'''" + re.escape() + r"'''"
            # init_string_index = [x.start() for x in re.finditer(init_string,body,re.IGNORECASE)]
            # print(init_string_index)
            # start_index = body[:init_string_index[0]].rfind('\n')
            # #s = s_regex.findall(body[start_index:-1],re.IGNORECASE)[0][3:-3].split('|')[0].replace(' ','%20')
            # instances = [x[1:-1] for x in s_regex.findall(body[start_index:-1],re.IGNORECASE)]
            # #print(instances)
            # #print(len(instances))
            # instance_locs = [x.start() for x in s_regex.finditer(body[start_index:-1],re.IGNORECASE)]
            # #print(instance_locs)
            # #print(len(instance_locs))
            # for i in range(len(instance_locs)):
                # if(p_regex.search(body,i)!=None):
                    # s = instances[i][2:-2].split('|')[0].replace(' ','_')
                    # print(s + " instance found! at index " + str(i))
                    # cnt += 1
                    # history.add(s)
                    # break
            # else:
                # print("No instances outside of parenthesis were found.  Exiting")
                # sys.exit()
            # #print(instances)
            
    # print(history)
    # print("Philosophy found after " + str(cnt) + " traversals.")

    
if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Usage: " + sys.argv[0] + " start_site finish_site")
    else:
        crawl_wiki(sys.argv[1], sys.argv[2])


    