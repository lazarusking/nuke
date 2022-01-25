#!/usr/bin/env python3
import argparse
import logging
import os
import re
import sys
import time

from hentai import Format, Hentai

# from nhentai import NHentai

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%I:%M:%S', level=logging.INFO)


def parseList(read_list):
    # print(read_list,"list now")
    content = re.compile(r'[\d]+')
    read_list = str(content.findall(str(read_list)))
    content = re.compile(r'(?!0)[\d]+')
    read_list = content.findall(read_list)
    return(sorted(set(read_list)))


def formatter(prog): return argparse.HelpFormatter(prog, max_help_position=60)


parser = argparse.ArgumentParser(formatter_class=formatter,
                                 description="Simple command line file parser for hentai nukes ")
group = parser.add_mutually_exclusive_group()
group.add_argument("-f", "--file", help=''' -f [FILE] filename \
                  Default file name is 'nukes.txt' ''',  type=argparse.FileType('r', encoding='utf-8'))
group.add_argument("-s", "--string", help='''-s [string] multiple strings can follow\
                    ''', action="store", default=["177013", "12242"], nargs="+", type=parseList)

parser.add_argument("-o", "--out", help='''-o [FILE].....OUTPUT file
                    Default file name is 'output.txt' ''', default="output.txt", nargs="?", type=argparse.FileType('w+', encoding='utf-8'))
parser.add_argument("-d", "--download", help='''if present downloads the files to a folder
                    ''', action="store_true")

args = parser.parse_args()
# print(parser.print_help())

# doujin.download(progressbar=True,dest=doujin.title(Format.Pretty))


def path_join(path=""):
    return os.path.join(os.getcwd(), path)


fname = sys.argv[0]
dirname = path_join()

# print(dirname, os.path.curdir)
args1 = ["-f", "-a"]
FILEPATH = ""
OUTPUT = args.out.name
# logging.info(args)
# print(args)
if len(sys.argv) > 1:

    if args.file:
        FILEPATH = os.path.join(dirname, args.file.name)
        print(FILEPATH)

    if args.out:
        OUTPUT = args.out.name
    if args.download:
        if not os.path.exists(path_join("Hentai Download")):
            os.mkdir(path_join("Hentai Download"))
            # logging.debug('This message should appear on the console')
            # logging.info(os.getcwd())

else:
    parser.print_help()
    os.system("pause")

    sys.exit()


start_time = time.time()

# nhentai = NHentai()


def raw(path=FILEPATH):
    try:
        if args.file:
            with open(path, "r+", encoding="utf-8") as f:
                read_list = f.read()
                return parseList(read_list)
        elif args.string:
            return parseList((args.string))
        else:
            parser.print_help()
            # sys.exit()
            os.system("pause")

    except FileNotFoundError:
        print("Default File(nukes.txt) doesn't exist in current directory it seems.")


def nuke_title(nuke, output=OUTPUT):
    # nuke_dict = {n: nhentai._get_doujin(id=nuke)['title'] for n in nuke}
    # codecs.encode(nuke)

    with open(output, "w+", encoding="utf-8") as f:
        nuke = [(n) for n in nuke if len(n) <= 6 or len(n) == 0]

        for n in nuke:
            # try:
            # p = f.write(''.join('{}:{}\n'.format(
            #     n, nhentai._get_doujin(id=n)['title'])for n in nuke))
            # for line in f:
            #     print(f.readline())

            # p = [(nhentai._get_doujin(id=n))['title'] for n in nuke]
            # content = ''.join('{}:{}\n'.format(nuke[x], p[x])
            #                   for x in range(0, len(p)))
            # f.write((content))
            # x = 1
            # while x < 2:

            try:
                # x += 1
                # p = ['{} : {}\n'.format(nhentai._BASE_URL+'/g/'+n, nhentai.search(query=n).title.pretty)]
                # p = ''.join(p)
                doujin = Hentai(n)
                p = "{} : {}\n".format(doujin.url, doujin.title(Format.Pretty))
                print(doujin.title(Format.Pretty))
                # logging.debug(f"{p} Success:")

                if args.download:
                    logging.info(f'Downloading 🌚: {doujin.id}')

                    if os.path.basename(os.getcwd()) != "Hentai Download":
                        os.chdir(path_join("Hentai Download"))
                    #     logging.info(os.curdir)
                    # logging.info(os.getcwd())
                    doujin.download(folder="", progressbar=True,
                                    dest=doujin.title(Format.Pretty))
                    logging.info('Downloaded ✌ 🌚  ')

                f.write(p)
                logging.info(f"Success! {p}")

            except Exception:
                print("Connection Error or something!")
                f.write("sike, no nuke or something")
        print(f"\nNukes written to file: {OUTPUT}")


# print('{}:{}\n'.format(n, 'sike'))
# print(e)
# x = 2
                # continue

    # print((time.time()-start_time))


if __name__ == "__main__":
    nuke = raw()
    print()
    nuke_title(nuke)

    # q = open("nuke_final.txt", "r", encoding="utf-8")
    # print(q.read())
    print(f"Elasped Time :{time.time()-start_time}s")
