import argparse, safygiphy
from colorama import init, Fore
init()
parser = argparse.ArgumentParser()
parser.add_argument("keyword", help="The keyword you wish to base your password off of")
args = parser.parse_args()
g= safygiphy.Giphy()

r = g.random(tag=args.keyword)
t = r[u'data'][u'url']
print (Fore.BLUE + "URL Link:")
print (Fore.WHITE + t)
full = t.rsplit('/',1)[-1]
if (len(full) < 19):
        print (Fore.GREEN + "ID")
        print (Fore.WHITE + full)
else:
        print (Fore.GREEN + "Most complexity")
        print (Fore.WHITE + full)
        print (Fore.YELLOW + "Phrase Idea")
        print (Fore.WHITE + full.rsplit('-',1)[0])
        print (Fore.CYAN + "ID Tag")
        print (Fore.WHITE + full.rsplit('-',1)[-1])

