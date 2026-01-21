# import win32com.client

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행': 'A000100'}
    def getcount(self):
        return len(self.stocks)
    def nametocode(self, name):
        return self.stocks[name]

instCpStockCode = CpStockCode()

print(instCpStockCode.getcount())
print(instCpStockCode.nametocode('유한양행'))

# explore = win32com.client.Dispatch("InternetExplorer.Application")
# explore.Visible = False