# nuke
Simple command line file parser for hentai nukes utilizing [hentai-chan's wrapper](https://github.com/hentai-chan/hentai/).

It sorts and filters nuke codes from either a file or string making an output file containing `url : title` of nukes
with the option to download the images of all the nukes. 
PS: Incorrect nukes are filtered out

```
usage: nuke.py [-h] [-f FILE | -s STRING [STRING ...]] [-o [OUT]] [-d]
py nuke.py -f nukes.txt
py nuke_name.py -s 177013 21031 3450000 -d


optional arguments:
  -h, --help                                            show this help message and exit
  -f FILE, --file FILE                                  -f [FILE] filename Default file name is 'nukes.txt'
  -s STRING [STRING ...], --string STRING [STRING ...]  -s [string] multiple strings can follow
  -o [OUT], --out [OUT]                                 -o [FILE].....OUTPUT file Default file name is 'output.txt'
  -d, --download                                        if present downloads the files to a folder
````
