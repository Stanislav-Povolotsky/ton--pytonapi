from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

EVENT_ID = "53388440417dc044d00e99d89b591acc28f100332a004f180e4f14b876620c13"


class TestEventMethod(TestAsyncTonapi):

    async def test_get_event(self):
        response = await self.tonapi.events.get_event(EVENT_ID)
        self.assertIsInstance(response, schema.events.Event)