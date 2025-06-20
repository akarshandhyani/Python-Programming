# This Video is Based on MultiProcessing in Python 
# #99 is Solution Video to #94 i.e. Ex-: 11 
# #100 is a conclusion Video of the Course by Harry and the some pathways and Advices to go from here agfter this Course

# Through this we can download or multiprocess various files at a same time

# Eg-: 

import concurrent.futures
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"
# pros = []
# for i in range(50):
#   # downloadFile(url, i)
#   p = multiprocessing.Process(target=downloadFile, args=[url, i])
#   p.start()
#   pros.append(p)

# for p in pros:
#   p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)  