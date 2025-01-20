
import cryptography, pickle
from cryptography.fernet import Fernet
def E():
  k = pickle.load(open("key.env","rb"))
  c = Fernet(k)
  t = c.encrypt(b"9708")
  pickle.dump( k, open( "key.env", "wb" ))
  pickle.dump(t,open("security.env", "wb"))
  c.decrypt(k)
