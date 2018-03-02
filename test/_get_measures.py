from datachile import ChileCube

client = ChileCube()
cube_id = "election_participation"

ms = client.get_measures(cube_id)

print(ms)