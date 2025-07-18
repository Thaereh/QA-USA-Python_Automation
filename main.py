import data
import helpers

class TestUrbanRoutes:
    @classmethod

    def setup_class (cls):
        if helpers.is_url_reachable (data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route (self):
        print("function created for set route")
        pass
    def  test_select_plan (self):
        print("function created for set route")
        pass
    def test_fill_phone_number (self):
        print("function created for set route")
        pass
    def test_fill_card (self):
        print("function created for set route")
        pass
    def test_comment_for_drive (self):
        print("function created for set route")
        pass
    def test_order_blanket_and_handkerchiefs(self):
        print("function created for set route")
        pass
    def test_order_2_ice_creams (self):
        number_of_ice_creams = 2
        for i in range(number_of_ice_creams):
            print("function created for order 2 ice creams")
            # Add in S8
        pass
    def test_car_search_model_appears (self):
        print("function created for set route")
        pass
