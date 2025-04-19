# sp500-goldencross
Bu projede, S&P 500 endeksi için 50 günlük ve 200 günlük hareketli ortalamalar (SMA) kullanarak basit bir alım-satım stratejisi oluşturduk. Amaç, SMA50'nin SMA200'ü geçtiği noktalarda alış, tam tersi durumda satış yaparak, küçük bir yatırım stratejisi simüle etmek.

# Ne Yapıyoruz?
S&P 500 verilerini yfinance ile indiriyoruz.

50 ve 200 günlük hareketli ortalamaları hesaplıyoruz.

Bu hareketli ortalamalarla alım ve satım noktaları belirliyoruz.

Grafik üzerinde hem fiyatı hem de alım-satım noktalarını gösteriyoruz.

Başlangıçta 100.000$ ile başlıyoruz ve strateji sonrasında ne kadar kazandığımızı hesaplıyoruz.

# Gereksinimler
Projenin çalışabilmesi için şu kütüphanelere ihtiyacınız var:

pandas

matplotlib

yfinance

numpy

Yüklemek için:
"""pip install pandas matplotlib yfinance numpy"""
