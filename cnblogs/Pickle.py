
#pickle 模块化
import  pickle

#dumps (object)序列化
listA=["one","two","three"]
listB=pickle._dumps(listA)
print("dumps (object)序列化 : {0}".format(listB))

#loads(string)反序列化
listC=pickle.loads(listB)
print("loads(string)反序列化 : {0}".format(listC))

#dump(object,file),将对象序列化存储到文件
writeFile=open('test.txt','wb')
try:
    pickle.dump(listA,writeFile,True)
except Exception as e:
    print(e)
finally:
    writeFile.close()
    
#load(object,file)将dump存储在文件里的数据反序列化
readFile=open('test.txt','rb')
listTemp=pickle.load(readFile)
print("load(object,file)将dump存储在文件里的数据反序列化:{0}".format(listTemp))
readFile.close()