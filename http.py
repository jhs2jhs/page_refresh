import httplib
import urlparse

host = 'v.youku.com'
#host = 'static.youku.com'
url = '/v_show/id_XNDI4MzM0MDA4.html'
#url = '/v1.0.0250/v/swf/loader.swf?VideoIDS=XNDI4MzM0MDA4'
#url= '/v1.0.0250/v/swf/loader.swf?VideoIDS=XNDI4MzM0MDA4&embedid=ODIuMjEuMTY0LjgCMTA3MDgzNTAyAgI%3D&wd='
port = 80
strict = 1
timeout = 10
source_address = None
headers = {
    #"Host":"www.amazon.com", 
    "Connection":"keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #"Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    }

def refresh():
    conn = httplib.HTTPConnection(host=host, port=port, strict=strict, timeout=timeout, source_address=source_address)
    #try:
    conn.request(method='GET', url=url, headers=headers)
    use_httplib_resp(conn)
    #except Exception as e:
    #    print '**exception:', e
    conn.close()

def use_httplib_resp(conn):
    resp = conn.getresponse()
    status_resp = resp.status
    reason_resp = resp.reason
    headers_resp = resp.getheaders()
    body_resp = resp.read()
    print status_resp, reason_resp
    print headers_resp
    #print body_resp

def multi_refresh():
    pass

for i in range(1, 20):
    print refresh()

