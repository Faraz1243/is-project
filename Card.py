# pip install pyscard
from smartcard.CardConnection import CardConnection
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
import time

def check_for_card():
    cardtype = AnyCardType()
    cardrequest = CardRequest(timeout=1, cardType=cardtype)

    while True:
        cardservice = cardrequest.waitforcard()
        if cardservice:
            return cardservice
        else:
            print("No card detected. Checking again in 1 second...")
            time.sleep(1)

def read_smartcard():
    while True:
        try:
            cardservice = check_for_card()
            cardservice.connection.connect()
            atr = cardservice.connection.getATR()
            # print("\033[0;0H")
            print("ATR:", toHexString(atr))
            # move cursor to x,y coordinate without clearing anything
           

            

            cardservice.connection.disconnect()
            return atr

        except KeyboardInterrupt:
            print("Program terminated.")
            break
        except Exception:
            # print("\033[0;0H")
            print("No Card Found!                                      ")
            return "atr not found"

if __name__ == "__main__":
    read_smartcard()
