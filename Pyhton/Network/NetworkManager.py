import mechanize
import cookielib
import urllib2


def getcontent(url):
    try:
        wp = urllib2.urlopen(url)
        content = wp.read()
        return content
    except Exception,e:
        print Exception,":",e


def web_getcontent(url):
    try:
        br = mechanize.Browser()
        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        # Browser options
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        # Follows refresh 0 but not hangs on refresh > 0
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        # Want debugging messages?
        # br.set_debug_http(True)
        # br.set_debug_redirects(True)
        # br.set_debug_responses(True)
        # User-Agent (this is cheating, ok?)
        br.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'), \
                         ('Cookie',"PHPSESSID=igevebvoga7r920i7p6nrcl4m6; pk10defaultNum=1; Hm_lvt_446167950c0005631fc20128d9b6869d=1479972020; Hm_lpvt_446167950c0005631fc20128d9b6869d=1479973599"), \
                         ("Accept-Encoding", "gzip, deflate, sdch"), \
                         ("Host", "www.cp098.com"),  \
                         ("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"), \
                         ("Accept", "*/*"), \
                         ("Referer", "http://www.cp098.com/pk10"), \
                         ("X-Requested-With", "XMLHttpRequest"), \
                         ("Connection", "keep-alive")]

        r = br.open(url)
        html = r.read()
        return html

    except Exception, e:
        print Exception, ":", e