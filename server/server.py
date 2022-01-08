#Server Side
# gunakan xmlrpc bagian server
# import SimpleXMLRPCServer dan SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.client import Binary
import shutil
import os
import pathlib
import json

# buat kelas requesthandler
# batasi pada path /RPC2 saja
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

versions = []

try:
    with open('versions.txt', 'r') as vers:
        versions = json.load(vers)
except:
    print('empty data')

def menu():
    inp = 0

    print('Aksi:')
    print('1. Jalankan server')
    print('2. Tambah versi')

    print('Input:')
    inp = input()

    if(inp == '1'):
        # buat server serta register fungsi register_introspection_functions()
        with SimpleXMLRPCServer(("localhost", 8008), requestHandler=RequestHandler) as server:
            server.register_introspection_functions()

            def get_latest_version():
                return str(versions[-1])

            def download_version(version):
                with open('updates/app.' + version + '.py', 'rb') as handle:
                    binary_data = handle.read()
                    return binary_data

            # b. register fungsinya
            server.register_function(get_latest_version)
            server.register_function(download_version)

            print('Menjalankan server...')
            server.serve_forever()

    elif(inp == '2'):
        print('Input versi:')
        ver = input()

        print('Input lokasi file:')
        path = input()

        versions.append(ver)

        shutil.move(os.path.join(pathlib.Path(__file__).parent.resolve().joinpath(path)), os.path.join(pathlib.Path(__file__).parent.resolve().joinpath('updates'), 'app.' + ver + '.py'))

        # save
        with open('versions.txt', 'w') as vers:
            json.dump(versions, vers)

        menu()

menu()