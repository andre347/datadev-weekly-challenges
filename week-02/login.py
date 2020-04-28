from dotenv import load_dotenv
load_dotenv()
import os
import tableauserverclient as TSC

# create an auth object
tableau_auth = TSC.PersonalAccessTokenAuth(os.getenv('TOKENNAME'), os.getenv('TOKENSECRET'), os.getenv('SITE') )

# create an instance for your server
server = TSC.Server(os.getenv('SERVER'), use_server_version=True)

# call the sign-in method with the auth object and print something to the console
with server.auth.sign_in_with_personal_access_token(tableau_auth):
    print('I am logged in!')