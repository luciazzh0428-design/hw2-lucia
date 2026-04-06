def generate_reply(user_input):
    if "refund" in user_input.lower():
        return "We are sorry to hear that. We will process your refund as soon as possible."
    
    elif "not arrived" in user_input.lower():
        return "We apologize for the delay. We are checking your order status and will update you shortly."
    
    elif "worst service" in user_input.lower():
        return "We sincerely apologize for your experience. We will work to resolve this issue immediately."
    
    elif "hack" in user_input.lower():
        return "We cannot fulfill that request, but we are happy to assist you with other inquiries."
    
    else:
        return "Thank you for reaching out. Could you please provide more details?"

if __name__ == "__main__":
    print("Customer Support AI\n")

    user_input = input("Enter customer message: ")

    reply = generate_reply(user_input)

    print("\n=== AI RESPONSE ===\n")
    print(reply)