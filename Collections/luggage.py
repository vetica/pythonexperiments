def packer(**kwargs):
  print(kwargs)

def unpacker(first_name=None, last_name=None):
  if first_name and last_name:
    print("Hi {} {}!".format(first_name, last_name))
  else:
    print("Hi no name!")

packer(name="Spencer", num=42, spanish_inquisition=None)
unpacker(**{"last_name": "Holladay", "first_name": "Spencer"})