import win_mtp.access
dev = win_mtp.access.get_portable_devices()
cont = dev[0].get_content()
path = u"Espace de stockage interne partagé\\Android\\data\\net.osmand.plus\\files\\itinerary.gpx"

# cont = cont.get_path(path)
# name = ".\\itinerary.gpx"
# cont.download_file(name)

n = u"Smini\\Espace de stockage interne partagé\\Android\\data\\net.osmand.plus\\files"
print(n)
for r, d, f in win_mtp.access.walk(dev[0], n):
    for f1 in f:
        print(f1.name)

#
# cont = cont.get_path("Interner Speicher\\Ringtones\\hangouts_incoming_call.ogg")
# name = '..\\..\\Tests\\hangouts_incoming_call.ogg'
# cont.download_file(name)