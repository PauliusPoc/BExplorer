from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .session import Client

import requests

def index(request):
    client = Client()
    client.create_session()
    latest_blocks = client.execute_command('python latest_blocks.py')
    client.close_session()
    context = {
        'latest_blocks': latest_blocks,
    }
    return render(request, 'BExplorer/index.html', context)

def block_details(request, block_height):
    client = Client()
    client.create_session()
    block = client.execute_command('python block_details.py --bheight ' + str(block_height))
    print(block)
    print(block[12])
    client.close_session()
    context = {
        'hash': block[0],
        'confirmations': block[1],
        'time': block[2],
        'height': block[3],
        'previous_hash': block[4],
        'difficulty': block[5],
        'merkle_root': block[6],
        'total_weight': block[7],
        'nonce': block[8],
        'total_transactions': block[9],
        'total_transacted': block[10],
        'total_fee': block[11],
    }
    ''''''
    return render(request, 'BExplorer/block.html', context)

def block_hash(request, previous_hash):
    client = Client()
    client.create_session()
    block = client.execute_command('python get_block_height.py --bhash ' + str(previous_hash))
    print(block)
    print(block[12])
    client.close_session()
    context = {
        'hash': block[0],
        'confirmations': block[1],
        'time': block[2],
        'height': block[3],
        'previous_hash': block[4],
        'difficulty': block[5],
        'merkle_root': block[6],
        'total_weight': block[7],
        'nonce': block[8],
        'total_transactions': block[9],
        'total_transacted': block[10],
        'total_fee': block[11],
    }
    
    return render(request, 'BExplorer/block.html', context)


def prices(request):
    context = {}
    context["crypto_data"] = get_crypto_data()
    return render(request, "BExplorer/prices.html", context)


# return the data received from api as json object
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()

    return data

# Create your views here.
