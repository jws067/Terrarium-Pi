import os.path
class FileWriter(object):
    def Save(self, name, waterAmt, unit, time):
        if os.path.isfile("config.txt"):
            file = open("config.txt", "r+")
            file.write(name + " \n" + waterAmt + "\n" + unit + "\n" + time + "\n")
            file.close()
            print "Saved..."
    def Create(self, name, waterAmt, unit, time):
        if not os.path.isfile("config.txt"):
            file = open("config.txt","w+")
            file.write(name + " \n" + waterAmt + "\n" + unit + "\n" + time + "\n")
            file.close()
            print "File Created..."
    def Read(self):
        try:
            print "trying"
            if os.path.isfile("config.txt"):
                print "Reading..."
                file = open("config.txt", "r")
                for line in range(4):
                    data = file.readline().split()
                    if (line == 0):
                        name = data[0]
                    elif(line == 1):
                        waterAmt = data[0]
                    elif(line == 2):
                        unit = data [0]
                    else:
                        time = data[0]
                return name, waterAmt, unit, time
            else:
                raise
        except:
            print "Unexpected Error. Check that File Exists."
