# Shahriyar Mammadli
# Object Class for SSLProxy
# Import required libraries
import datetime

class ProxyItem:
    # Create the proxy item
    def __init__(self, ip, port, country, anonymityType, lastChecked):
        self.ip = ip
        self.port = port
        self.country = country
        # Anonymity level of the proxy
        self.anonymityType = anonymityType
        # The last check date of the proxy
        self.lastChecked = ProxyItem.__lastCheckedDate(self, lastChecked)


    # Calculation of the proxy last check date
    def __lastCheckedDate(self, lastChecked):
        # Current time
        curTime = datetime.datetime.now()
        # Time to subtract
        subTime = int(lastChecked.split(" ")[0])
        # Make words singular by removing 's'
        dateType = ""
        if(lastChecked.split(" ")[1][len(lastChecked.split(" ")[1]) - 1] == 's'):
            dateType = lastChecked.split(" ")[1][0:len(lastChecked.split(" ")[1]) - 1]
        else:
            dateType = lastChecked.split(" ")[1]
        # There are four possibilities for last checked date "# seconds ago", "# minutes ago", ...
        # ... "# hours ago", and all other cases which we will not consider
        if(dateType == "second"):
            # Formatted date time
            forTime = datetime.timedelta(seconds=subTime)
        elif(dateType == "minute"):
            # Formatted date time
            forTime = datetime.timedelta(minutes=subTime)
        elif(dateType == "hour"):
            # Formatted date time
            forTime = datetime.timedelta(hours=subTime)
        else:
            return None
        return curTime - forTime

    # Function for getting ip
    def getIp(self):
        return self.ip

    # Function for getting port
    def getPort(self):
        return self.port

    # Function for getting country
    def getCountry(self):
        return self.country

    # Function for getting anonymityType
    def getAnonymityType(self):
        return self.anonymityType

    # Function for getting lastChecked
    def getLastChecked(self):
        return self.lastChecked