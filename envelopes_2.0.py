# -*- coding: utf-8 -*-

# initializing percent rate
NECESSITY_RATE = 0.55
FREEDOM_RATE = 0.1
EDUCATION_RATE = 0.1
LONG_TERM_RATE = 0.1
ENTERTAINMENT_RATE = 0.1
GIFT_RATE = 0.05

# initializing empty envelopes
necessity_envelope = 0
freedom_envelope = 0
education_envelope = 0
long_term_envelope = 0
entertainment_envelope = 0
gift_envelope = 0

# initializing expected income
expected_income = 1000

# initializing handler for standard input
total = 0

# invitation, greetings
print("""Hello!
We will distribute the funds you entered into the envelopes.
Please enter the amount of money to see the result.
Press Ctrl+C to exit the script.\n""")

while total <= expected_income:
    money_amount = float(input('Enter the amount of money: '))
    total += money_amount

    necessity_envelope += total * NECESSITY_RATE
    freedom_envelope += total * FREEDOM_RATE
    education_envelope += total * EDUCATION_RATE
    long_term_envelope += total * LONG_TERM_RATE
    entertainment_envelope += total * ENTERTAINMENT_RATE
    gift_envelope += total * GIFT_RATE

# final output
print(f"We've got the following results:\n"
      f"{'Necessity envelope:' : <30} ${necessity_envelope:.2f}\n"
      f"{'Financial freedom envelope:' : <30} ${freedom_envelope:.2f}\n"
      f"{'Education envelope:' : <30} ${education_envelope:.2f}\n"
      f"{'Long term savings envelope:' : <30} ${long_term_envelope:.2f}\n"
      f"{'Entertainment envelope:' : <30} ${entertainment_envelope:.2f}\n"
      f"{'Gift envelope:' : <30} ${gift_envelope:.2f}\n\n"
      "Thank your for using our program!")
