import data
from helpers import is_url_reachable


class TestUrbanRoutes:


    @classmethod
    def setUpClass(cls):
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes.")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    def test_select_plan(self):
        def test_select_plan(self):
            routes_page = UrbanRoutesPage(self.driver)

        routes_page.select_supportive_plan()
        assert routes_page.get_current_selected_plan() == 'Comfort'


    def test_fill_phone_number(self):
        def test_fill_phone_number(self):
            routes_page = UrbanRoutesPage(self.driver)

        phone_number = data.PHONE_NUMBER
        routes_page.set_phone(phone_number)
        assert routes_page.get_phone() == phone_number


    def test_fill_card(self):
        def test_fill_card(self):
            routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_current_payment_method() == 'Cartão'


    def test_comment_for_driver(self):
        def test_comment_for_driver(self):
            routes_page = UrbanRoutesPage(self.driver)

        message = data.MESSAGE_FOR_DRIVER
        routes_page.set_message_for_driver(message)
        assert routes_page.get_message_for_driver() == message


    def test_order_blanket_and_handkerchiefs(self):
        def test_order_blanket_and_handkerchiefs(self):
            routes_page = UrbanRoutesPage(self.driver)

        routes_page.click_blanket_and_handkerchiefs_option()
        assert routes_page.get_blanket_and_handkerchiefs_option_checked()


    def test_order_2_ice_creams(self):
        def test_order_2_ice_creams(self):
            routes_page = UrbanRoutesPage(self.driver)

        routes_page.add_ice_cream(2)
        assert routes_page.get_amount_of_ice_cream() == 2


    def test_car_search_model_appears(self):
        def test_order_2_ice_creams(self):
            routes_page = UrbanRoutesPage(self.driver)

        routes_page.add_ice_cream(2)
        assert routes_page.get_amount_of_ice_cream() == 2