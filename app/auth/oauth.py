from flask import url_for, current_app, redirect, request
from rauth import OAuth2Service

import json
from urllib.request import urlopen


class OAuthSignIn:
    providers = None

    def __init__(self, provider_name):
        """Init the class data by grabbing it from the app configuration"""
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for(
            'auth.oauth_callback', provider=self.provider_name, _external=True)

    @classmethod
    def get_provider(self, provider_name):
        """Get a provider from an internal list of providers.

        If no internal list of providers exists, create one and populate
        it by searching through the subclasses of this class. Each
        subclass is assumed to be from a provider (eg Google, Facebook, etc).
        """
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]


class GoogleSignIn(OAuthSignIn):
    def __init__(self):
        super(GoogleSignIn, self).__init__('google')
        googleinfo = urlopen(
            'https://accounts.google.com/.well-known/openid-configuration')
        google_params = json.load(googleinfo)
        self.service = OAuth2Service(
            name='google',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url=google_params.get('authorization_endpoint'),
            base_url=google_params.get('userinfo_endpoint'),
            access_token_url=google_params.get('token_endpoint'))

    def authorize(self):
        return redirect(
            self.service.get_authorize_url(
                scope='email',
                response_type='code',
                redirect_uri=self.get_callback_url()))

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={
                'code': request.args['code'],
                'grant_type': 'authorization_code',
                'redirect_uri': self.get_callback_url()
            },
            decoder=json.loads)
        me = oauth_session.get('').json()
        return (me['name'], me['email'])
