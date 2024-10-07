import textwrap

story = '''You are a time traveller, who has been lost in time. You need to navigate through airports in Asia to
find and stop a bomb blast that happened in the past and took many lives.

Your journey will start from a random airport. So, when
you decide to start your journey, you’ll be informed that how much money in rupees, fuel you have”.
As you begin your mission, you’ll be notified at each airport with the
message, “Welcome to X Airport! You are left with X Rupees , X fuel, and X time.

In order to complete your mission, you have to utilize money and fuel. You can always buy
fuel by using your money left in the wallet. If you’re lucky enough, you might get some
coupons on few random airports which you can redeem at the different airport within the same
country.

You can redeem the coupon to increase money in your wallet. As soon as coupon is
redeemed, you’ll be notified. Use your resources wisely as you have less time and limited resources.
Make sure you find the targeted location within the given time else bomb will blast and your efforts
will go in vain.

Once you arrive at the targeted location, airport display board will show a message “BOMB HAS
BEEN DEACTIVATED THANKS FOR SAVING LIVES”!

You’re in tears of joy that finally your efforts could save many lives!! You’re back in present now.

'''

# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list