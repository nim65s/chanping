from channels.generic.websocket import AsyncJsonWebsocketConsumer


class WSPingConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content):
        d = {'pong': content['ping']}
        await self.send_json(d)
