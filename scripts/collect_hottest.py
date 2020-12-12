import json
import argparse
import os.path as osp
import requests

def get_posts(topic):
    posts=[]
    where=""
    num=100 
    for i in range(5):
        if i==0:
            data=requests.get(f'http://api.reddit.com{topic}/new?limit={num}',
                        headers={'User-Agent' : 'windows: requests (by /u/druths)'})
        else:
            data=requests.get(f'http://api.reddit.com{topic}/new?limit={num}&after={where}',
                        headers={'User-Agent' : 'windows: requests (by /u/druths)'})
        content=data.json()['data']['children']
        posts.extend(content)
        where=posts[-1]['data']['name']
    posts=posts[:500]
    return posts
        



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o',help="the output file")
    parser.add_argument('subred',help="the subreddit that you are interested in.")

    args=parser.parse_args()

    out=args.o
    topic=args.subred

    posts=get_posts(topic)

    with open(out,'w') as fp:
        fp.write(
                    '\n'.join(json.dumps(i) for i in posts) 
                    )



if __name__=='__main__':
    main()
