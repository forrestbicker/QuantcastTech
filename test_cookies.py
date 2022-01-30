# test_cookies.py

from most_active_cookie import get_cookies, most_active_cookies_from_file

# test case where one cookie is most active on the given date
def test_one_cookie():
    with open('test/test_cookies.csv', 'w+') as f:
        f.write('''cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00''')
    assert most_active_cookies_from_file('test/test_cookies.csv', "2018-12-09") == ['AtY0laUfhglK3lC7']

# test case where multiple cookies are tied on the given date
def test_tie():
    with open('test/test_cookies.csv', 'w+') as f:
        f.write('''cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00''')
    assert most_active_cookies_from_file('test/test_cookies.csv', "2018-12-09") == ['AtY0laUfhglK3lC7', '5UAVanZf6UtGyKVS']

# test case where all cookies are unique (all tied) on a larger dataset
def test_unique():
    with open('test/test_cookies.csv', 'w+') as f:
        f.write('''cookie,timestamp
giWIc2K2tWznOrTF,2022-01-30T01:22:00+00:00
uR7hvXQMDk2a7l7n,2022-01-30T01:53:00+00:00
YMgZvKRI8Z9wNxNX,2022-01-30T02:22:00+00:00
2Fu31i9kf1Qpi2pL,2022-01-30T02:41:00+00:00
4GE4bII5re85DHQ9,2022-01-30T03:16:00+00:00
fNFfdYeZ42UIGZ8B,2022-01-30T03:45:00+00:00
15o7rP4H24eczbjx,2022-01-30T04:18:00+00:00
w4JVz97uC55UEw35,2022-01-30T04:59:00+00:00
M6wK9WJ3kFvWOReI,2022-01-30T05:20:00+00:00''')
    assert most_active_cookies_from_file('test/test_cookies.csv', "2022-01-30") == [
        'giWIc2K2tWznOrTF',
        'uR7hvXQMDk2a7l7n',
        'YMgZvKRI8Z9wNxNX',
        '2Fu31i9kf1Qpi2pL',
        '4GE4bII5re85DHQ9',
        'fNFfdYeZ42UIGZ8B',
        '15o7rP4H24eczbjx',
        'w4JVz97uC55UEw35',
        'M6wK9WJ3kFvWOReI'
    ]

# test case where no cookies occur on the given date
def test_no_cookie():
    with open('test/test_cookies.csv', 'w+') as f:
        f.write('''cookie,timestamp
nsW7NU3eXb16986r,2022-01-30T01:18:00+00:00
5hR66sAMoaL5sokF,2022-01-30T01:43:00+00:00
uS4Pp3i1cHcaPmDX,2022-01-30T02:08:00+00:00
F9sdkV3SO21GYVOP,2022-01-30T02:55:00+00:00
a72a4MWbQK63Co51,2022-01-30T03:16:00+00:00
Vft3z5K8gR84qVsd,2022-01-30T03:37:00+00:00
SharzP4s8G35Uhsq,2022-01-30T04:08:00+00:00
4w8fdjJO2f682i6Q,2022-01-30T04:53:00+00:00
B6M9VxiP9z8ysMUS,2022-01-30T05:28:00+00:00
s9JVzV6CWW5DvcUZ,2022-01-30T05:36:00+00:00''')
    assert most_active_cookies_from_file('test/test_cookies.csv', "2022-01-31") == []

# test case where input file is empty
def test_no_input():
    with open('test/test_cookies.csv', 'w+') as f:
        f.write('''cookie,timestamp''')
    assert most_active_cookies_from_file('test/test_cookies.csv', "2022-01-31") == []

# test case where only one cookie occurs
def test_unanimous():
    with open('test/test_cookies.csv', 'w+') as f:
        f.write('''cookie,timestamp
QSwHx2ssREMUT6OX,2022-01-30T01:21:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T01:45:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T02:11:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T02:38:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T03:05:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T03:31:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T04:14:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T04:44:00+00:00
QSwHx2ssREMUT6OX,2022-01-30T05:17:00+00:00''')
    assert most_active_cookies_from_file('test/test_cookies.csv', "2022-01-30") == ['QSwHx2ssREMUT6OX']

# test case where all cookies are unique (all tied) on a larger dataset
def test_big():
    with open('test/test_cookies.csv', 'w+') as f:
        f.write('''cookie,timestamp
qsYV8e93We5ezhpc,2022-01-30T01:08:00+00:00
z9o3q2xOuMQ1y9hO,2022-01-30T02:00:00+00:00
54XoI9g2IgZp2Z62,2022-01-30T02:04:00+00:00
xNZugIOut5qpLf1d,2022-01-30T02:59:00+00:00
2y6624KF5e3GWGe6,2022-01-30T03:21:00+00:00
Hh25y82324Ky76hK,2022-01-30T03:45:00+00:00
Ivg5Xe6mpfc45Ve8,2022-01-30T04:14:00+00:00
B38o2P28O8NkyLFC,2022-01-30T04:55:00+00:00
ar591cU6iWjeS5v1,2022-01-30T05:29:00+00:00
G28opW3VmA7ceM71,2022-01-30T05:54:00+00:00
asl26hNW2W9Qv1if,2022-01-30T06:12:00+00:00
qvu4V2dhl4qTUq65,2022-01-30T06:51:00+00:00
5SiecEtgYMkesXEq,2022-01-30T07:03:00+00:00
fw6T8W9lit14j4Ym,2022-01-30T07:53:00+00:00
7G8R33MsyLJ78p9i,2022-01-30T08:09:00+00:00
7qQJ91113ocGZ52E,2022-01-30T08:37:00+00:00
yC7T8bsaIpF93nVV,2022-01-30T09:23:00+00:00
cDna2ayUIPAKx9Pe,2022-01-30T09:55:00+00:00
3eF5GJirs24mHsZ8,2022-01-30T10:21:00+00:00
J4e958ewph1s9qA7,2022-01-30T10:57:00+00:00
UBs2DH54wv335GbW,2022-01-30T11:26:00+00:00
255Dg7kwtkr5fwsf,2022-01-30T11:57:00+00:00
M6fSXtApM9pNgKHy,2022-01-30T12:00:00+00:00
OjU2l7oSRUSv76Mt,2022-01-30T12:35:00+00:00
8B837jiBe9K2YF9K,2022-01-30T13:14:00+00:00
11kt4M5mqCD2OhyN,2022-01-30T13:47:00+00:00
vTH99GA8VoSlE9w4,2022-01-30T14:08:00+00:00
ct43DT44olFTJy4o,2022-01-30T14:51:00+00:00
BM13iPr95x7hqTp6,2022-01-30T15:00:00+00:00
vmUq1697Rfyo2VCt,2022-01-30T15:32:00+00:00''')
    assert most_active_cookies_from_file('test/test_cookies.csv', "2022-01-30") == [
        'qsYV8e93We5ezhpc',
        'z9o3q2xOuMQ1y9hO',
        '54XoI9g2IgZp2Z62',
        'xNZugIOut5qpLf1d',
        '2y6624KF5e3GWGe6',
        'Hh25y82324Ky76hK',
        'Ivg5Xe6mpfc45Ve8',
        'B38o2P28O8NkyLFC',
        'ar591cU6iWjeS5v1',
        'G28opW3VmA7ceM71',
        'asl26hNW2W9Qv1if',
        'qvu4V2dhl4qTUq65',
        '5SiecEtgYMkesXEq',
        'fw6T8W9lit14j4Ym',
        '7G8R33MsyLJ78p9i',
        '7qQJ91113ocGZ52E',
        'yC7T8bsaIpF93nVV',
        'cDna2ayUIPAKx9Pe',
        '3eF5GJirs24mHsZ8',
        'J4e958ewph1s9qA7',
        'UBs2DH54wv335GbW',
        '255Dg7kwtkr5fwsf',
        'M6fSXtApM9pNgKHy',
        'OjU2l7oSRUSv76Mt',
        '8B837jiBe9K2YF9K',
        '11kt4M5mqCD2OhyN',
        'vTH99GA8VoSlE9w4',
        'ct43DT44olFTJy4o',
        'BM13iPr95x7hqTp6',
        'vmUq1697Rfyo2VCt',
    ]
