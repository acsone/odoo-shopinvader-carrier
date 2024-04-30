# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import tagged

from .common import TestShopinvaderDeliveryPickupCommon


@tagged("post_install", "-at_install")
class TestCart(TestShopinvaderDeliveryPickupCommon):
    def test_setting_pickup_site(self):
        shipping = self.cart.partner_shipping_id
        self.assertEqual(shipping.ref, "foo")
        self.assertEqual(shipping.name, "Foo")
        self.assertEqual(self.cart.final_shipping_partner_id, self.final_partner)
        self.assertEqual(self.cart.final_shipping_partner_id.is_pickup_site, True)
        self.assertEqual(self.cart.final_shipping_partner_id.name, "Osiris")
        self.assertEqual(self.cart.carrier_id, self.poste_carrier)

    def test_changing_pickup_site(self):
        previous_shipping = self.cart.partner_shipping_id
        self._cart_set_delivery_pickup(self.cart, self.pickup_site_bar)
        self.assertNotEqual(self.cart.partner_shipping_id, previous_shipping)
        shipping = self.cart.partner_shipping_id
        self.assertEqual(shipping.ref, "bar")
        self.assertEqual(shipping.name, "Bar")
        self.assertEqual(self.cart.final_shipping_partner_id, self.final_partner)
        self.assertEqual(self.cart.final_shipping_partner_id.is_pickup_site, True)
        self.assertEqual(self.cart.final_shipping_partner_id.name, "Osiris")
        self.assertEqual(self.cart.carrier_id, self.free_carrier)

    def test_change_carrier(self):
        self._set_carrier(self.cart, data={"carrier_id": self.free_carrier.id})
        self.assertEqual(self.cart.partner_shipping_id, self.final_partner)
        self.assertEqual(self.cart.final_shipping_partner_id.is_pickup_site, False)
        self.assertEqual(self.cart.final_shipping_partner_id.name, "Osiris")

    def test_unset_carrier(self):
        self._set_carrier(self.cart, data={"carrier_id": False})
        self.assertEqual(self.cart.partner_shipping_id, self.final_partner)
