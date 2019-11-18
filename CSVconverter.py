import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

changes = {
    '\n': '',
    }

with open(os.path.join(__location__, 'CAP 01 2019_Tube 6_001.csv')) as csvfile:
   data = csvfile.read()
   rep = {"\n" : ","}
   for i, j in rep.items():
      data = data.replace(i, j)

with open("output.csv", "w") as outputfile:
      outputfile.write(data)
      outputfile.close()


