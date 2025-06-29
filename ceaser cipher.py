while True:
 choice=input("\n1 for Encrypt / 0 for Decrypt:  ")     
 alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
 if choice=="1":
   user=input("Enter the plain text to convert into ceaser cipher: ")
   result=""
   key=int(input("Enter your key: "))
   for char in user:
     if char in alphabets:
        a=alphabets.index(char)
        add=(a+key)%26
        alpha=(alphabets[add])
        result+=alpha
        print(alpha,end="")
        
 elif choice=="0":
     user=input("Enter your decrypted text: ")
     result=""
     key=int(input("Enter your key: "))
     for char in user:
      if char in alphabets:
        a=alphabets.index(char)
        add=(a-key)%26
        alpha=(alphabets[add])
        result+=alpha
        print(alpha,end="")

 else:
     print("Kindly enter only one word (alphabets) in small letters ")
     break
