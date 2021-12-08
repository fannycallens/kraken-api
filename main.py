import ws_client
import rest_api
import asyncio


def depth_callback(depthEvent):
    #fs.recv()
    print(depthEvent)

async def listen_for_message(websocket):
    while True:
        await asyncio.sleep(0)
        try:
            print('Listening for a message...')
            message = await websocket.recv()
            print("< {}".format(message))
        except Exception as e:
            print('Something happened')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kraken = rest_api.API()
    # kraken.load_key('kraken.key')
    ''' 
    kraken.query_private('AddOrder', {'pair': 'XXBTZEUR',
                                 'type': 'buy',
                                 'ordertype': 'limit',
                                 'price': '1',
                                 'volume': '1',
                                 'close[pair]': 'XXBTZEUR',
                                 'close[type]': 'sell',
                                 'close[ordertype]': 'limit',
                                 'close[price]': '9001',
                                 'close[volume]': '1'})
                                 "pair": [
    "XBT/USD",
    "XBT/EUR"
  ],
    '''

    subscribe_depth = {'name' : 'depth'}

    depthWs = ws_client.WssClient().subscribe_public(subscribe_depth, depth_callback)


    # to retrieve token for authentication
    # https://api.kraken.com/0/private/GetWebSocketsToken

    ''' to subscribe to private ws, send subscribe event with token
    {
        "event": "subscribe",
        "subscription":
            {
                "name": "ownTrades",
                "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu"
            }
    }
    '''
