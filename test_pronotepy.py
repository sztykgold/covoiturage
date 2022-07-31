import pronotepy
from pronotepy.ent import ent_hdf
# importing ent specific function, you do not need to import anything if you dont use an ent

client = pronotepy.Client('http://195.221.154.181/professeur.html?login=true',
                      username='alexandre.sztykgold', #username='SZTYKGOLD',
                      password='#Robert666', #password='#Robert666',
                      ent=ent_hdf)
if client.logged_in:
    print('ca marche !')
else:
    print(":(")