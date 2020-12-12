import pandas as pd
import argparse
import json
import random

def load_json(fname):
    content=[]
    with open(fname, 'r') as content_file:
        for jsonObj in content_file:
            Dict = json.loads(jsonObj)
            content.append(Dict)
    return content

def get_posts(content,num,maxlen):
    names=[]
    titles=[]
    coding=['']*num

    index=random.sample(range(maxlen),num)
    
    for i in index:
        names.append(content[i]['data']['name'])
        titles.append(content[i]['data']['title'])
    
    dic={"Name":names,"title":titles,"coding":coding}

    posts=pd.DataFrame(dic)

    return posts
        

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-o',help="Gimme the output file you desire.")
    parser.add_argument('jsonfile',help='the json file you want to read.')
    parser.add_argument('num_posts', help='the number of posts you want.')

    args=parser.parse_args()
    content=load_json(args.jsonfile)
    
    #deciding the number of posts
    
    if int(args.num_posts)<0:
        raise Exception("number of posts has to be positive int.")
    num=min(len(content),int(args.num_posts))

    posts=get_posts(content,num,len(content))
    posts.to_csv(args.o,sep='\t',index=False)

if __name__=='__main__':
    main()
