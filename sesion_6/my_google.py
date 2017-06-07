# _*_ coding: utf-8 _*_

import google as goo
import re
import urllib

def download_file(download_url):
    filename = re.match(".*/(.*\.pdf)$", download_url).group(1)

    # print "Filename:", filename

    web_file = urllib.urlopen(download_url)
    local_file = open(filename, 'w')
    local_file.write(web_file.read())
    web_file.close()
    local_file.close()

# WITHOUT REGEX: into search put: filetype:pdf Ex. "alarm 525 filetype:pdf"
result = goo.search("alarm 526 filetype:pdf", num=10, stop=1, pause=60.0)
# result = ["http://lloydselectronica.com/manuales/Manual-LA-525.pdf"]
for url in result:
    # TODO: Check if the url refers to pdf
    if re.match(".*\.pdf$", "%s" % url, re.UNICODE):
        # TODO: Download the url
        print "DOWNLOADING: %s" % url
        download_file(url)
