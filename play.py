




















def get_crypto(response, id, id1):
    portfolio = Portfolio.objects.get(id=id)
    if portfolio in response.user.portfolio.all():
        if response.method == "GET":
            crypto = portfolio.crypto_set.get(id=id1)
            if cryto in response.user.crypto.all():
                serializer = ItemSerializer(crypto)
            else:
                return HTTPResponse("Unauthorized")

            return Response(serializer.data)

