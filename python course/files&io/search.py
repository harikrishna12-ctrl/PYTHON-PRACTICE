with open("python course/files&io/sample.txt","r") as f:
   data=True

   while data:
      data=f.readline()
      if("python" in data):
         print("the word is found")
