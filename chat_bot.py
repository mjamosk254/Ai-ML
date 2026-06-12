def zuri():
    print("hello, I am zuri your safaricom assistant")
    print("ask me about bundles, mpesa, airtime, internet, refunds, or agents")
    message=input("you: ").lower()
    if "bundles" in message:
        print("zuri:you can buy bundles using *544# or my safaricom app")
    elif "mpesa" in message:
        print("zuri:use *334# or sim toolkit or mpesa app for services")
    elif "reverse" in message:
        print("zuri: to initiate a refund forward the message to 456")
    else:
        print("zuri: sorry i did not understand your request")
zuri()                    