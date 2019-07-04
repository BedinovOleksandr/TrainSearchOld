import sys
import argparse
from plagins.traine_search import train_search
import plagins.notification_by_bot as bot


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fr', type=int, default='+')
    parser.add_argument('-t', '--to', type=int, default='+')
    parser.add_argument('-d', '--date', type=str, default='?')
    parser.add_argument('-tf', '--time', type=str, default='?')
    parser.add_argument('-tr', '--train', type=str, default='?')

    return parser


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
print(namespace)

result = train_search(namespace.fr, namespace.to, namespace.date, namespace.time)
l = result["data"]["list"]
for i in l:
   if i["num"] == namespace.train:
      bot.notification('alarm ' + namespace.train)
