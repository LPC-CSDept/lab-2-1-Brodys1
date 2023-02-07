def main():
   ##################################################
   # Comlete your code here
    original_price = int(input("What's the regular price? "))
    rate = int(input("What's the discount percentage? "))/100

    discount_amount = int(original_price * rate)
    final_price = int(original_price - (original_price * rate))
    print ('Regular Price : $', original_price,
    '\nDiscount Amount : $', discount_amount,
    '\nThe Final Price : $', final_price)
   ##################################################

    pass


if __name__ == '__main__':
    main()
