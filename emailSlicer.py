def main():
    print("welcome to the email slicer ")
    print(" ")
    #o utilizador escreve o seu endereço de email
    email_input = input("Input your email address: ")
    #o split separa o username do domain do endereço de email
    (username, domain) = email_input.split("@")
    #o split separa o domain da extensao do endereço de email 
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()