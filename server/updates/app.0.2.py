#Client Side
# import library xmlrpc client karena akan digunakan rpc
import xmlrpc.client

ver = 0.2

# buat stub/skeleton (proxy) pada client
s = xmlrpc.client.ServerProxy('http://127.0.0.1:8008')

print('Mengecek versi terbaru...')

latest_version = s.get_latest_version()

print('Latest version: ', latest_version)
print('Current version: ', ver)

if float(latest_version) > ver:

    print('Versi terbaru ditemukan. Apakah kamu ingin mengupdate ke versi terbaru? (Y/n)')
    inp = input()

    if(inp == 'Y'):

        downloaded_file = s.download_version(latest_version)

        with open('updates/app.' + latest_version + '.py', "wb") as handle:
            handle.write(downloaded_file)
else:

    print('Tidak ada versi baru ditemukan.')
