# _*_ coding: utf-8 _*_

import duckduckgo as dk
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
result = dk.query("python")
# result = ["http://lloydselectronica.com/manuales/Manual-LA-525.pdf"]
print result.results
for q in result.results:
    url = q.url

    print url

    # TODO: Check if the url refers to pdf
    if re.match(".*\.pdf$", "%s" % url, re.UNICODE):
        # TODO: Download the url
        print "DOWNLOADING: %s" % url
        download_file(url)
