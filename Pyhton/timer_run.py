import Network.NetworkManager as NM
import Util.DateUtil as DU
import sys
import time
import re
import json

import BJSCPK10.Crawser as BJPKCrawser
import CQSSC.Crawser as CQSSCCrawser
import GDKLSF.Crawser as GDKLSFCrawser
import GDSYXW.Crawser as GDSYXWCrawser
import JSKS.Crawser as JSKSCrawser
import XJSSC.Crawser as XJSSCCrawser
import TJSSC.Crawser as TJSSCCrawser
import XYFT.Crawser as XYFTCrawser
import XYNC.Crawser as XYNCCrawser

reload(sys)
sys.setdefaultencoding('utf-8')


crawser = BJPKCrawser.Crawser()
crawser.crawser_index()

crawser = CQSSCCrawser.Crawser()
crawser.crawser_index()

crawser = GDKLSFCrawser.Crawser()
crawser.crawser_index()

crawser = GDSYXWCrawser.Crawser()
crawser.crawser_index()

crawser = JSKSCrawser.Crawser()
crawser.crawser_index()

crawser = TJSSCCrawser.Crawser()
crawser.crawser_index()

crawser = XJSSCCrawser.Crawser()
crawser.crawser_index()

crawser = XYFTCrawser.Crawser()
crawser.crawser_index()

crawser = XYNCCrawser.Crawser()
crawser.crawser_index()

crawser = GDKLSFCrawser.Crawser()
crawser.crawser_index()