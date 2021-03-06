from urllib import request


goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=8&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'
baidu_url = 'http://www.google.co.uk/finance/historical?q=NASDAQ%3ABIDU&ei=nWITWcjtJ4bFUZj0gugD&output=csv'

def download_stock_data(csv_url, filename):
    response = request.urlopen(csv_url)# connect/open
    csv = response.read()
    csv_str = str(csv) # convert to string
    lines = csv_str.split("\\n")
    dest_url = filename # r means raw so any characters accepted
    fx = open(dest_url, 'w') #open file
    for line in lines:
        fx.write(line + "\n")# write

    fx.close()

download_stock_data(goog_url, 'google.csv')
download_stock_data(baidu_url, 'baidu.csv')



