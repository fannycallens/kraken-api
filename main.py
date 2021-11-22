import ws_client
import rest_api
import json

def depth_callback(depthEvent):
    print(depthEvent)

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
    '''

    subscribe_depth = {'event' : 'subscribe', 'subscription' : {'name' : 'depth'}}
    subscribe_depth_json = json.dumps(subscribe_depth)

    ws_client.WssClient().subscribe_public(subscribe_depth_json,depth_callback)

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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
