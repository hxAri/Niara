#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 7.11-2023 16:28
# @github https://github.com/hxAri/Niara
#
# Niara Copyright (c) 2022 - Ari Setiawan <hxari@proton.me>
# Niara Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#


from typing import final
from yutiriti import (
	AuthError, 
	Cookie, 
	Cookies, 
	Object, 
	Readonly, 
	Request, 
	RequestError, 
	RequestRequired,
	typeof
)

from niara.config import BROWSER
from niara.typing import Authorization


class Client( RequestRequired, Readonly ):

	def __init__( self, secure:bool=False, cookies:Cookies=None, request:Request=None ):
		
		"""
		"""

		if request is None:
			request = Request()
		elif not isinstance( request, Request ):
			raise TypeError( "Invalid \"request\" parameter, value just be Request, {} passed".format( typeof( request ) ) )

		if cookies is not None:
			if isinstance( cookies, Cookies ):
				cookies = dict( cookies )
			elif isinstance( cookies, Object ):
				cookies = cookies.dict()
			if not isinstance( cookies, dict ):
				raise TypeError( "Invalid \"cookies\" parameter, value must be type Cookies|Dict|Object, {} passed".format( typeof( cookies ) ) )
			for cookie in list( cookies.keys() ):
				Cookie.set( self.cookies, cookie, cookies[cookie] )
			self.authorization.cookies = cookies
		
		self.__secure__ = secure
		self.__request__ = request
		self.__request__.headers.update({
			"User-Agent": BROWSER
		})

		self.__endpoint__ = "127.0.0.1:8443/nifi-api"
		self.__authorization__ = Authorization({
			"cookies": None,
			"username": None,
			"password": None
		})
	
	@final
	@property
	def authenticated( self ) -> bool:
		if self.secure is True:
			authorization = self.authorization
			if isinstance( authorization, Authorization ):
				return authorization.cookies and \
					authorization.username or \
					authorization.cookies
			return False
		return True
	
	@final
	@property
	def authorization( self ) -> Authorization: return self.__authorization__

	def controllerCluster( self ) -> bool|dict:

		"""
		"""

		request = self.request.get( f"{self.endpoint}/controller/cluster" )
		if request.status == 200:
			return request.json()
		return False
	
	def controllerConfig( self ) -> bool|dict:

		"""
		"""

		request = self.request.get( f"{self.endpoint}/controller/config" )
		if request.status == 200:
			return request.json()
		return False

	@final
	@property
	def endpoint( self ) -> str: return "{}://{}".format( "https" if self.secure is True else "http", self.__endpoint__ )

	@final
	@property
	def secure( self ) -> bool: return self.__secure__
	
	def signin( self, username, password ) -> bool:
		
		"""
		"""

		if username is None:
			raise ValueError( "Username can't be empty" )
		elif not isinstance( username, str ):
			raise TypeError( "Invalid \"username\" parameter, value must be type str, {} passed".format( typeof( username ) ) )
		if password is None:
			raise ValueError( "password can't be empty" )
		elif not isinstance( password, str ):
			raise TypeError( "Invalid \"password\" parameter, value must be type str, {} passed".format( typeof( password ) ) )

		request = self.request.post( f"{self.endpoint}/access/token" )
		if request.status == 200:
			self.authorization.username = username
			self.authorization.password = password
			self.cookies = {
				"__Secure-Request-Token": request.cookies['__Secure-Request-Token'],
				"__Secure-Authorization-Bearer": request.cookies['__Secure-Authorization-Bearer']
			}
			return True
		return False