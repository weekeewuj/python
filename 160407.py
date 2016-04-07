def saveBrief(self,content,name):
    fileName = name + "/" + name + ".txt"
    f = open(fileName,"w+")
    print u"save files",fileName
    f.write(content.encode('utf-8'))
