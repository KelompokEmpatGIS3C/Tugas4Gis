#!/bin/python


import folium

m = folium.Map(
    location=[-6.21462, 106.84513],
    zoom_start=12,
    tiles='Stamen Terrain'
)

tooltip = 'Click me!'

folium.Marker([-6.203189, 106.846839], popup='<i>Tugu Proklamasi</i>').add_to(m)
folium.Marker([-6.190242, 106.838724], popup='<i>Taman Ismail Marzuki</i>').add_to(m)
folium.Marker([-6.191407, 106.838621], popup='<i>Ibis Budget Hotels</i>').add_to(m)
folium.Marker([-6.190051, 106.840759], popup='<i>Makam Habib Abdurrahman Al Habsyi</i>').add_to(m)
folium.Marker([-6.188764, 106.839719], popup='<i>TIM XXI</i>').add_to(m)
folium.Marker([-6.189337, 106.837872], popup='<i>Holland Bakery</i>').add_to(m)
folium.Marker([-6.195175, 106.823081], popup='<i>Bundaran Hotel Indonesia</i>').add_to(m)
folium.Marker([-6.194954, 106.823065], popup='<i>Monumen Selamat Datang</i>').add_to(m)
folium.Marker([-6.196270, 106.823889], popup='<i>Swimming Pool - Mandarin Hotel, Jakarta</i>').add_to(m)
folium.Marker([-6.199610, 106.832275], popup='<i>Lapangan Merdeka</i>').add_to(m)
folium.Marker([-6.231707, 106.909807], popup='<i>Rumah Sakit Duren Sawit</i>').add_to(m)
folium.Marker([-6.231944, 106.908660], popup='<i>Warung Bu Tin</i>').add_to(m)
folium.Marker([-6.225864, 106.898880], popup='<i>PT. INDOPSIKO INDONESIA</i>').add_to(m)
folium.Marker([-6.195030, 106.878456], popup='<i>Gedung Dewi Sartika, Universitas Negeri Jakarta</i>').add_to(m)
folium.Marker([-6.198222, 106.877793], popup='<i>Lapangan Golf Rawamangun</i>').add_to(m)
folium.Marker([-6.194831, 106.912626], popup='<i>PT. Lativi Media Karya (tvOne)</i>').add_to(m)
folium.Marker([-6.302446, 106.895155], popup='<i>Taman Mini Indonesia Indah</i>').add_to(m)
folium.Marker([-6.312821, 106.861838], popup='<i>Mall Graha Cijantung</i>').add_to(m)
folium.Marker([-6.157329, 106.908704], popup='<i>Mall Kelapa Gading</i>').add_to(m)
folium.Marker([-6.328956, 106.890288], popup='<i>Kampung Artis</i>').add_to(m)
folium.Marker([-6.196195, 106.829531], popup='<i>Taman Menteng</i>').add_to(m)
folium.Marker([-6.199388, 106.832670], popup='<i>Taman Suropati</i>').add_to(m)
folium.Marker([-6.175384, 106.827148], popup='<i>Monumen Nasional</i>').add_to(m)
folium.Marker([-6.170189, 106.824174], popup='<i>Istana Merdeka</i>').add_to(m)
folium.Marker([-6.312434, 106.820162], popup='<i>Taman Ragunan</i>').add_to(m)
folium.Marker([-6.219897, 106.814125], popup='<i>Plaza Semanggi</i>').add_to(m)
folium.Marker([-6.176579, 106.837442], popup='<i>RSAD Gatot Soebroto</i>').add_to(m)
folium.Marker([-6.178354, 106.838090], popup='<i>Museum Kebangkitan Nasional</i>').add_to(m)
folium.Marker([-6.170164, 106.831387], popup='<i>Masjid Istiqlal</i>').add_to(m)
folium.Marker([-6.123794, 106.831809], popup='<i>Dunia Fantasi</i>').add_to(m)
folium.Marker([-6.134263, 106.813040], popup='<i>Kota Tua</i>').add_to(m)
folium.Marker([-6.134903, 106.813262], popup='<i>Taman Fattahillah, Kota Tua</i>').add_to(m)
folium.Marker([-6.137195, 106.812972], popup='<i>Museum Bank Indonesia</i>').add_to(m)
folium.Marker([-6.325301, 106.852310], popup='<i>Rumah Mertua</i>').add_to(m)

m
