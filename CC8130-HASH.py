import hashlib

myText = input("Inisira o texto descriptografado: ")

SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

validaSHA256 = input("Insira o trecho criptografado em SHA256: ")

validaMD5 = input("Insira o trecho criptografado em MD5: ")

print("\nFrase original e suas criptografias corretas: ")
print("\"" + myText + "\" - " + SHA256 + " - " + MD5)

if SHA256 == validaSHA256 and MD5 == validaMD5:
    print("\nNesse caso as 2 criptografias inseridas estão corretas\n")
    print("Crtiptografia inserida SHA256: " + validaSHA256 + " \ Criptografia correta SHA256: " + SHA256)
    print("Crtiptografia inserida MD5: " + validaMD5 + " \ Criptografia correta MD5: " + MD5)

if SHA256 == validaSHA256 and MD5 != validaMD5:
    print("\nNesse caso apenas a criptografia SHA256 está correta\n")
    print("Crtiptografia inserida SHA256: " + validaSHA256 + " \ Criptografia correta SHA256: " + SHA256)
    print("Crtiptografia inserida MD5: " + validaMD5 + " \ Criptografia correta MD5: " + MD5)

if SHA256 != validaSHA256 and MD5 == validaMD5:
    print("\nNesse caso apenas a criptografia MD5 está correta\n")
    print("Crtiptografia inserida SHA256: " + validaSHA256 + " \ Criptografia correta SHA256: " + SHA256)
    print("Crtiptografia inserida MD5: " + validaMD5 + " \ Criptografia correta MD5: " + MD5)

if SHA256 != validaSHA256 and MD5 != validaMD5:
    print("\nNesse caso as 2 criptografias estão incorretas\n")
    print("Crtiptografia inserida SHA256: " + validaSHA256 + " \ Criptografia correta SHA256: " + SHA256 + "\n")
    print("Crtiptografia inserida MD5: " + validaMD5 + " \ Criptografia correta MD5: " + MD5)

