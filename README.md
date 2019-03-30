# Password-Cracking
Password security is crucial, which is why it is important for user passwords to be hashed and then stored.
This way, direct passwords are not stored on a server, waiitng for a potential hacker but instead hashed to form a new password which is realted to the users actual password via the hashing algorithm.
However if the hashing alogorithm is easily identifiable and simple enough salt is added then it is only a matter of time before passwords are cracked.
This is eaxavtly what happeend in the Formspring dump which used the SHA258 algorithm and a simple salt of concatening digits  ranging from 01-99.
What I have created is a dictionary lookup password cracking tool. With this in only the first few thousand accounts, I was able to crack almost 200 passwords.
The python file can be easilty minipulated to fit other password dumps and minipulations on the salt.
