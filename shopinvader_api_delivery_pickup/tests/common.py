# Copyright 2019 Akretion (http://www.akretion.com).
# Copyright 2019 ACSONE SA/NV
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.shopinvader_api_delivery_carrier.tests.common import (
    TestShopinvaderDeliveryCarrierCommon,
)


class TestShopinvaderDeliveryPickupCommon(TestShopinvaderDeliveryCarrierCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.final_partner = cls.cart.partner_shipping_id
        cls.poste_carrier.with_dropoff_site = True
        cls._set_carrier(cls.cart, cls.poste_carrier)
        cls.pickup_site_foo = cls.env["dropoff.site"].create(
            {"ref": "foo", "name": "Foo", "carrier_id": cls.poste_carrier.id}
        )
        cls.pickup_site_bar = cls.env["dropoff.site"].create(
            {"ref": "bar", "name": "Bar", "carrier_id": cls.free_carrier.id}
        )
        cls._cart_set_delivery_pickup(cls.cart, cls.pickup_site_foo)

    def _cart_set_delivery_pickup(self, cart, pickup_site_id):
        self._set_delivery_pickup(cart=cart, data={"pickup_site_id": pickup_site_id.id})

    def _delivery_pickup_search(self, params, cart):
        return self._search(params=params, cart=cart)
