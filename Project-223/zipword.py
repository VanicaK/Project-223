import zipfile,time

folderpath=input("Path to zipped file:")
zipf=zipfile.ZipFile(folderpath)
global result
result=0
global tried
tried=0
c=0

if not zipf:
    print("This isn't password protected, it is free to open")
else:
    worldlistfile=open("C:/Users/vijay/OneDrive/Desktop/VS Projects Python/Project-223/wordlist.txt","r")
    body=worldlistfile.read().lower()
    passes=[]
    passes=body.split("\n")
    starttime=time.time()
    for i in range(len(passes)):
        word=passes[i]
        password=word.encode("utf-8").strip()
        c+=1
        print("attempting to deocde with {}".format(word))
        try:
            with zipfile.ZipFile(folderpath,"r") as zf:
                zf.extractall(pwd=password)
                print("success! password is "+word)
                endtime=time.time()
                totaltime=endtime-starttime
                result=1
                print("time taken: "+totaltime)
                break
        except:
            pass
