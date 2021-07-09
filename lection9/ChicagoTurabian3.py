from re import *

prefix = r"\d+\.\s"
authorN = r"(?:" + r"(?P<author41>.+)\s(?P<author42>[^\s,]+)\set\sal\." + r"|" +r"(?P<author211>[^,]+)\s(?P<author212>\S+)\sand\s(?P<author22>[^,]+)" + r"|" +  r"(?P<author11>[^,]+)\s(?P<author12>[^\s,]+)" + r"(?:(?:(?:,\s(?P<author3>.+),)?\sand\s(?P<author2>[^,]+)))?" + r")" + r",\s"
titleN = r"(?P<title>.+)\s\("
cityN = r"(?P<city>.+):\s"
publisherN = r"(?P<publisher>.+),\s"
dateN = r"(?P<date>\d+)\),\s"
pageN = r"(?:(?:\d+|\d+-\d+))\."
Nt = prefix + authorN + titleN + cityN + publisherN + dateN + pageN

authorB = r"(?P<author12>\S+),\s(?P<author11>[^,]+)(?:,(?:\s(?P<author3>[^,]+),)?(?:\s(?P<author4>[^,]+),)*\sand\s(?P<author2>[^\d]+))?" + r"\.\s"
titleB = r"(?P<title>.+)\.\s"
cityB = r"(?P<city>.+):\s"
publisherB = r"(?P<publisher>.+),\s"
dateB = r"(?P<date>\d+)\." 
Bt = authorB + titleB + cityB + publisherB + dateB

N, B = search(Nt, input()) , search(Bt, input())
print(N.groups())
print(B.groups())

