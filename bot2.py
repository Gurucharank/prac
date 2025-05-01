def banking_chatbot():
    print("Welcome to SmartBank! How can I assist you today?")   
    while True:
        print("\nYou can ask me the following:")
        print("1. What's my account balance?")
        print("2. What loan options do you offer?")
        print("3. How can I contact customer support?")
        print("4. What are your bank's opening hours?")
        print("5. How do I reset my password?")
        print("6. Exit")
        # Get user's query
        question = input("Please enter your question: ").lower()
        if "account balance" in question:
            print("\nYour account balance is $2,500.00.")
        elif "loan options" in question:
            print("\nWe offer the following loan options:")
            print("1. Personal Loan")
            print("2. Home Loan")
            print("3. Car Loan")
            print("For more details, please visit our website or contact customer support.")
        elif "contact customer support" in question:
            print("\nYou can reach our customer support team at:")
            print("Email: support@smartbank.com")
            print("Phone: 1-800-555-1234")
        elif "opening hours" in question:
            print("\nOur bank's opening hours are:")
            print("Monday to Friday: 9:00 AM - 5:00 PM")
            print("Saturday: 9:00 AM - 1:00 PM")
            print("Closed on Sundays and public holidays.")
        elif "reset my password" in question:
            print("\nTo reset your password, please follow these steps:")
            print("1. Visit our password reset page on the website.")
            print("2. Enter your registered email address.")
            print("3. Check your inbox for a password reset link.")
            print("4. Follow the instructions to set a new password.")
        elif "exit" in question:
            print("Thank you for using SmartBank. Have a great day!")
            break
        else:
            print("Sorry, I didn't understand that. Please ask again.")
banking_chatbot()
