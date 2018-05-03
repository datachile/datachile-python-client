from datachile import ChileCube

client = ChileCube()
query = client.get_comunas()

print(query)