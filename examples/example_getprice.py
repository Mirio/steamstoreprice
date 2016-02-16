from steamstoreprice import SteamStorePrice

url = "http://store.steampowered.com/app/349040/"
pricelib = SteamStorePrice()
print(pricelib.getprice(url))
