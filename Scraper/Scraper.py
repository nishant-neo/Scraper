#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NISHANT
#
# Created:     25-03-2015
# Copyright:   (c) NISHANT 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint
from lxml import html
import requests
import os
class Scraper:
    """
    It is the class that scrapes the data from  a page from wikipedia.org and
    then scrapes 10 other random wiki pages using lxml and requests.
    """
    link='http://en.wikipedia.org/wiki/Big_data'
    links=[]

    def scrap(self,link,h):
        """
        A function that scrapes the page whose link is passed into it using lxml and requests
        and also creates the list of links present in that wiki page
        """
        links=[]
        page=requests.get(link)
        tree=html.fromstring(page.text)
        heading =tree.xpath('//*[@id="mw-content-text"]/p/a/text()|//*[@id="mw-content-text"]/p/text()|//*[@id]/text()|//*[@id="mw-content-text"]/p/b/text()|//*[@id="mw-content-text"]/table/text()')
        links= tree.xpath('//*[@id="mw-content-text"]/p/a/@href')
        self.links=self.links+links
        comment=tree.xpath('//*/comment()')
        temp_filename = "output%d.txt" % (h)
        text_file = open(temp_filename, "w")
        text_file.write(link+'\n')
        text_file.write('*************************METADATA*************************\n')

        for n in comment:
            try:
                text_file.write(str(n))
            except:
                continue

        text_file.write('\n*************************DATA*************************\n')
        print 'Scraping '+link

        for i in heading:
            i=i.replace('\t', '')
            try:
                text_file.write(i)
            except:
                continue

        text_file.close()
        f=open(temp_filename)
        filename = os.path.basename(link)+'.txt'
        f2=open(filename,"w")
        for line in f:
            if (line!='\n'):
                f2.write(line)
        f.close()
        f2.close()
        os.remove(temp_filename)

    def linker(self):
        """
        Function that starts with a starting page and then creates 10 random indexes and
        then follows those links and scrapes data out of it
        """
        self.scrap(self.link,0)
        for i in range(1, 11):
            randlink=randint(1,len(self.links))
            if('http://' in self.links[randlink]):
                #self.scrap(self.links[randlink],i)
                pass
            else:
                self.scrap('http://en.wikipedia.org'+self.links[randlink],i)
def main():
    ch=Scraper()
    ch.linker()

main()