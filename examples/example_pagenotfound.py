from steamstoreprice import SteamStorePrice

url = "http://store.steampowered.com/app/0000000/"
pricelib = SteamStorePrice()
pricelib.getpage(pricelib.normalizeurl(url))
