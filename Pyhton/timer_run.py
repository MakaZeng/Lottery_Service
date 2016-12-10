import sys

import Apps.BJSCPK10.Crawser as BJPKCrawser
import Apps.CQSSC.Crawser as CQSSCCrawser
import Apps.GDKLSF.Crawser as GDKLSFCrawser
import Apps.GDSYXW.Crawser as GDSYXWCrawser
import Apps.JSKS.Crawser as JSKSCrawser
import Apps.TJSSC.Crawser as TJSSCCrawser
import Apps.XYFT.Crawser as XYFTCrawser
import Apps.XYNC.Crawser as XYNCCrawser

from Apps import XJSSC as XJSSCCrawser

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