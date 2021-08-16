class PostCode:
    def __init__(self, postcode_json_dict):
        self.postcode = postcode_json_dict['postcode']
        self.latitude = postcode_json_dict['latitude']
        self.longitude = postcode_json_dict['longitude']
        self.eastings = postcode_json_dict['eastings']
        self.northings = postcode_json_dict['northings']

    def __repr__(self):
        return f"<PostCode({self.postcode})>"

    def get_location(self, en=False): # en = eastings/northings
        if en:
            return self.eastings, self.northings
        else:
            return self.latitude, self.longitude