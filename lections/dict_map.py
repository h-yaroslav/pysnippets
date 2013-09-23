#!/usr/bin/python

import os, sys
from pprint import pprint as pp

volumes = ({'inspector_id': 40873L, 'region_total_count': 1L},
        {'inspector_id': 86931L, 'region_total_count': 3L}, {'inspector_id':
        87738L, 'region_total_count': 1L}, {'inspector_id': 90662L,
        'region_total_count': 5L}, {'inspector_id': 117628L,
        'region_total_count': 1L}, {'inspector_id': 134725L,
        'region_total_count': 65L}, {'inspector_id': 138766L,
        'region_total_count': 22L}, {'inspector_id': 161883L,
        'region_total_count': 1L}, {'inspector_id': 169844L,
        'region_total_count': 13L}, {'inspector_id': 187731L,
        'region_total_count': 1L}, {'inspector_id': 192961L,
        'region_total_count': 80L}, {'inspector_id': 196959L,
        'region_total_count': 29L}, {'inspector_id': 203859L,
        'region_total_count': 1L}, {'inspector_id': 206786L,
        'region_total_count': 1L}, {'inspector_id': 212710L,
        'region_total_count': 3L}, {'inspector_id': 227020L,
        'region_total_count': 1L}, {'inspector_id': 227022L,
        'region_total_count': 1L}, {'inspector_id': 232954L,
        'region_total_count': 1L}, {'inspector_id': 255120L,
        'region_total_count': 2L}, {'inspector_id': 283808L,
        'region_total_count': 1L}, {'inspector_id': 288666L,
        'region_total_count': 3L}, {'inspector_id': 313995L,
            'region_total_count': 1L}, {'inspector_id': 321223L,
                'region_total_count': 1L}, {'inspector_id': 326090L,
                    'region_total_count': 1L}, {'inspector_id': 329155L,
                        'region_total_count': 1L}, {'inspector_id': 460190L,
                            'region_total_count': 6L}, {'inspector_id':
                                466769L, 'region_total_count': 1L},
{'inspector_id': 469438L, 'region_total_count': 3L}, {'inspector_id': 522774L,
    'region_total_count': 1L}, {'inspector_id': 547749L, 'region_total_count':
        5L}, {'inspector_id': 566866L, 'region_total_count': 1L},
{'inspector_id': 567475L, 'region_total_count': 1L}, {'inspector_id': 573820L,
    'region_total_count': 2L}, {'inspector_id': 635398L, 'region_total_count':
        1L}, {'inspector_id': 733145L, 'region_total_count': 1L},
{'inspector_id': 740264L, 'region_total_count': 1L}, {'inspector_id': 788467L,
    'region_total_count': 1L}, {'inspector_id': 923499L, 'region_total_count':
        1L}, {'inspector_id': 1062196L, 'region_total_count': 3L},
{'inspector_id': 1493629L, 'region_total_count': 1L}, {'inspector_id':
    1518085L, 'region_total_count': 2L}, {'inspector_id': 1591180L,
        'region_total_count': 1L}, {'inspector_id': 1591182L,
            'region_total_count': 1L}, {'inspector_id': 1621949L,
                'region_total_count': 1L}, {'inspector_id': 1658959L,
                    'region_total_count': 1L}, {'inspector_id': 1665942L,
                        'region_total_count': 2L}, {'inspector_id': 1667688L,
                            'region_total_count': 1L}, {'inspector_id':
                                1670103L, 'region_total_count': 1L})
complaints = ({'domain': 'nickjr.com', 'protocol': 'http', 'region': 'APAC',
 'complaint_id': 1L, 'state': 'added', 'inspector_id': 40873L, 'path':
 ('c', '/parenting/flicks_for_kids/index.jhtml'), 'subdomain': 'www',
 'resolution': None, 'port': 80L, 'when_timestamp': 1234546706L}, {'domain':
 'hi5.com', 'protocol': 'http', 'region': 'APAC', 'complaint_id': 3L, 'state':
 'added', 'inspector_id': 86931L, 'path': ('c',
     '/friend/photos/displayuploadphotosajax.do'), 'subdomain': '',
 'resolution': None, 'port': 80L, 'when_timestamp': 1234546707L}, {'domain':
 'iesuper.com', 'protocol': 'http', 'region': 'APAC', 'complaint_id': 4L,
 'state': 'added', 'inspector_id': 87738L, 'path': ('c',
     '/client/webinfo.htm'), 'subdomain': 'try', 'resolution': None, 'port':
 80L, 'when_timestamp': 1234546707L}, {'domain': '124.153.106.73', 'protocol':
 'http', 'region': 'APAC', 'complaint_id': 5L, 'state': 'added',
 'inspector_id': 90662L, 'path': ('c',
     '/exambooking/candidateinterface/custombooking.aspx'), 'subdomain': '',
 'resolution': None, 'port': 80L, 'when_timestamp': 1234546707L}, {'domain':
 'tvants.com', 'protocol': 'http', 'region': 'APAC', 'complaint_id': 8L,
 'state': 'added', 'inspector_id': 117628L, 'path': ('c'), 'subdomain':
 'www', 'resolution': None, 'port': 80L, 'when_timestamp': 1234546707L},
 {'domain': 'real.com', 'protocol': 'http', 'region': 'APAC', 'complaint_id':
 9L, 'state': 'added', 'inspector_id': 134725L, 'path': ('c', '/player'),
 'subdomain': 'switchboard', 'resolution': None, 'port': 80L,
 'when_timestamp': 1234546707L}, {'domain': 'rediffmail.com', 'protocol':
     'http', 'region': 'APAC', 'complaint_id': 10L, 'state': 'added',
     'inspector_id': 138766L, 'path': ('c', '/cgi-bin/red.cgi'),
     'subdomain': 'www', 'resolution': None, 'port': 80L, 'when_timestamp':
         1234546707L}, {'domain': 'sanook.com', 'protocol': 'http', 'region':
             'APAC', 'complaint_id': 15L, 'state': 'added', 'inspector_id':
                 161883L, 'path': ('c', '/gameupdate/snews_07626.php'),
             'subdomain': 'game', 'resolution': None, 'port': 80L,
             'when_timestamp': 1234546707L}, {'domain': 'goggle.com',
                 'protocol': 'http', 'region': 'APAC', 'complaint_id': 16L,
                 'state': 'added', 'inspector_id': 169844L, 'path':
                     ('c'), 'subdomain': 'www', 'resolution': None,
                 'port': 80L, 'when_timestamp': 1234546707L}, {'domain':
                     'panoramio.com', 'protocol': 'http', 'region': 'APAC',
                     'complaint_id': 18L, 'state': 'added', 'inspector_id':
                         187731L, 'path': ('c', '/photo/2986004'),
                     'subdomain': 'www', 'resolution': None, 'port': 80L,
                     'when_timestamp': 1234546707L}, {'domain':
                         'windowsmedia.com', 'protocol': 'http', 'region':
                             'APAC', 'complaint_id': 19L, 'state': 'added',
                         'inspector_id': 192961L, 'path': ('c',
                                 '/redir/mediaguide.asp'), 'subdomain': '',
                         'resolution': None, 'port': 80L, 'when_timestamp':
                             1234546707L}, {'domain': 'bharatmatrimony.com',
                                 'protocol': 'http', 'region': 'APAC',
                                 'complaint_id': 21L, 'state': 'added',
                                 'inspector_id': 196959L, 'path': ('c',
                                         '/campaign/tracking.php'),
                                 'subdomain': 'server', 'resolution': None,
                                 'port': 80L, 'when_timestamp': 1234546707L},
{'domain': 'gushare.com', 'protocol': 'http', 'region': 'APAC',
    'complaint_id': 23L, 'state': 'added', 'inspector_id': 203859L, 'path':
        ('c', '/file.php'), 'subdomain': 'sv2', 'resolution': None,
    'port': 80L, 'when_timestamp': 1234546707L}, {'domain':
        'depositfiles.com', 'protocol': 'http', 'region': 'APAC',
        'complaint_id': 25L, 'state': 'added', 'inspector_id': 206786L,
        'path': ('c', '/files/peal9iiac'), 'subdomain': '', 'resolution':
            None, 'port': 80L, 'when_timestamp': 1234546707L}, {'domain':
                'raaga.com', 'protocol': 'http', 'region': 'APAC',
                'complaint_id': 27L, 'state': 'added', 'inspector_id':
                    212710L, 'path': ('c'), 'subdomain': 'www',
                'resolution': None, 'port': 80L, 'when_timestamp':
                    1234546707L}, {'domain': 'jobbnorge.no', 'protocol':
                        'http', 'region': 'APAC', 'complaint_id': 29L,
                        'state': 'added', 'inspector_id': 227020L, 'path':
                            ('c'), 'subdomain': 'www', 'resolution':
                            None, 'port': 80L, 'when_timestamp': 1234546707L},
{'domain': 'megavideo.com', 'protocol': 'http', 'region': 'APAC',
    'complaint_id': 30L, 'state': 'added', 'inspector_id': 227022L, 'path':
        ('c', '/v/hulsuap763ddc509401ca6787b466b8659be6118'),
    'subdomain': 'www', 'resolution': None, 'port': 80L, 'when_timestamp':
        1234546707L}, {'domain': 'saradaga1.com', 'protocol': 'http',
            'region': 'APAC', 'complaint_id': 32L, 'state': 'added',
            'inspector_id': 232954L, 'path': ('c'), 'subdomain': 'www',
            'resolution': None, 'port': 80L, 'when_timestamp': 1234546707L},
{'domain': 'myplaywin.com', 'protocol': 'http', 'region': 'APAC',
    'complaint_id': 34L, 'state': 'added', 'inspector_id': 255120L, 'path':
        ('c'), 'subdomain': 'www', 'resolution': None, 'port': 80L,
    'when_timestamp': 1234546707L}, {'domain': 'brothersoft.com', 'protocol':
        'http', 'region': 'APAC', 'complaint_id': 40L, 'state': 'added',
        'inspector_id': 283808L, 'path': ('c',
                '/dvd_video/dvd_burner/nero-8.3.6.0_eng_update.exe'),
        'subdomain': 'lfiles3', 'resolution': None, 'port': 80L,
        'when_timestamp': 1234546707L})
pp(volumes)
#print
#pp(complaints)

def populate_volumes(x,y):
    try:
        print x, y
        if x['inspector_id'] == y['inspector_id']:
            print x, y
    #        x['volume'] = y['region_total_count']
    except TypeError, e:
        print str(e)
ress = []
for key, val in volumes.items():
    ress.append(key,val)
print ress
#res = dict(int(volumes['inspector_id']) = int(volumes['region_total_count']))
#print res
#print map(lambda x: ":".join(x['inspector_id'],x['region_total_count']), volumes)

