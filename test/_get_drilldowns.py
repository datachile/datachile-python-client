from datachile import ChileCube

client = ChileCube()
cube_id = "election_participation"

dd = client.get_drilldowns(cube_id)

print(dd)