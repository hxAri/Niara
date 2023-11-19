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
	Cookies, 
	Object, 
	Readonly, 
	RequestRequired, 
	tree, 
	typeof, 
	Yutiriti 
)

from niara.client import Client
from niara.config import *
from niara.typing import *


#[niara.Niara]
class Niara( RequestRequired, Readonly, Yutiriti ):
	
	#[Niara( Bool secure, Client client, Cookies|Dict|Object cookies )]: None
	def __init__( self, secure:bool=False, client:Client=None, cookies:Cookies|dict|Object=None ) -> None:
		
		"""
		"""

		if client is None:
			client = Client( secure=secure, cookies=cookies )
		elif not isinstance( client, Client ):
			raise TypeError( "Invalid \"\" parameter, value must be type Client, {} passed".format( typeof( client ) ) )
		
		self.__client__ = client
		self.__request__ = client.request
		...
	
	def access( self ) -> None:
		if self.authenticated:
			options = [
				"/access", [
					"Gets the status the client's access"
				],
				"/access/config", [
					"Retrieves the access configuration for this NiFi"
				],
				"/access/kerberos", [
					"Creates a token for accessing the REST API via",
					"Kerberos ticket exchange / SPNEGO negotiation"
				],
				"/access/knox/callback", [
					"Redirect/callback URI for processing the result",
					"of the Apache Knox login sequence.",
				],
				"/access/knox/logout", [
					"Performs a logout in the Apache Knox."
				],
				"/access/knox/request", [
					"Initiates a request to authenticate through Apache Knox."
				],
				"/access/logout", [
					"Performs a logout for other providers that have been issued a JWT."
				],
				"/access/logout/complete", [
					"Completes the logout sequence by removing the cached Logout Request",
					"and Cookie if they existed and redirects to /nifi/login."
				],
				"/access/token/expiration", [
					"Get expiration for current Access Token"
				],
				"Cancel", [
					"Back to main"
				]
			]
			self.output( self.access, [ "User authentication and token endpoints\n", options ])
			select = self.input( "Action", number=True, default=[ idx for idx in range( len( options ) ) ] )
			match int( select ):
				case 1: ...
				case 2: ...
				case 3: ...
				case 4: ...
				case 5: ...
				case 6: ...
				case 7: ...
				case 8: ...
				case 9: ...
				case _:
					self.main()
		else:
			self.signin()
	
	@final
	@property
	def authenticated( self ) -> bool: return self.client.authenticated
	
	@final
	@property
	def authorization( self ) -> Authorization: return self.client.authorization
	
	@final
	@property
	def banner( self ) -> str:
		return f"""
             \x1b[1;38;5;240m::
            \x1b[1;38;5;245m^\x1b[1;38;5;255mJJ\x1b[1;38;5;245m^\x1b[1;38;5;240m... :~\x1b[1;38;5;245m^
      \x1b[1;38;5;245m.^\x1b[1;38;5;240m::\x1b[1;38;5;255m~7JJJJJJ??JJJ\x1b[1;38;5;245m^
      \x1b[1;38;5;255m7JJJYYJ?77??JJJJJJ?!!??\x1b[1;38;5;240m:
      \x1b[1;38;5;240m:\x1b[1;38;5;255mJJJ?\x1b[1;38;5;245m^.     .^\x1b[1;38;5;255m!?JJLJJJ?\x1b[1;38;5;240m.
    \x1b[1;38;5;240m:\x1b[1;38;5;245m^\x1b[1;38;5;255m?JJJ\x1b[1;38;5;245m. \x1b[1;38;5;69m*  \x1b[1;38;5;245m~\x1b[1;38;5;255m7\x1b[1;38;5;245m^   .^\x1b[1;38;5;255m?JIJJJJ?\x1b[1;38;5;240m: ..
   \x1b[1;38;5;240m.\x1b[1;38;5;255m?JJJJJ\x1b[1;38;5;245m^  \x1b[1;38;5;240m.\x1b[1;38;5;245m!\x1b[1;38;5;255mJY7     \x1b[1;38;5;245m.\x1b[1;38;5;255m?JAJJ\x1b[1;38;5;245m~::^\x1b[1;38;5;240m::.
    \x1b[1;38;5;240m..\x1b[1;38;5;245m^\x1b[1;38;5;255m?JJJ??JJJJ\x1b[1;38;5;245m:      :\x1b[1;38;5;255mJNJ7\x1b[1;38;5;245m^\x1b[1;38;5;240m:\x1b[1;38;5;245m~!~\x1b[1;38;5;240m::.
       \x1b[1;38;5;240m:\x1b[1;38;5;255mJJJ?J?7JJ\x1b[1;38;5;245m~       \x1b[1;38;5;255m7AJ?\x1b[1;38;5;245m^\x1b[1;38;5;240m:::::.
       \x1b[1;38;5;240m.\x1b[1;38;5;255m!7\x1b[1;38;5;245m^..  :^.       \x1b[1;38;5;255m?JJ?\x1b[1;38;5;245m!!\x1b[1;38;5;240m~~^
                        \x1b[1;38;5;245m:\x1b[1;38;5;255mJJJ7\x1b[1;38;5;245m!!!!!
                       \x1b[1;38;5;245m:\x1b[1;38;5;255m?JJ?\x1b[1;38;5;245m!!!\x1b[1;38;5;240m~~~.
                      \x1b[1;38;5;245m^\x1b[1;38;5;255m?JJ?\x1b[1;38;5;245m!!^\x1b[1;38;5;240m:::::.
                    \x1b[1;38;5;245m:\x1b[1;38;5;255m7JJJ7\x1b[1;38;5;245m!!\x1b[1;38;5;240m~.:\x1b[1;38;5;245m~!~\x1b[1;38;5;240m::.
                  \x1b[1;38;5;245m:\x1b[1;38;5;255m!JJJJ7\x1b[1;38;5;245m!!!!^::^\x1b[1;38;5;240m::.
                \x1b[1;38;5;245m:\x1b[1;38;5;255m~JJCJJ7\x1b[1;38;5;245m!!!!!!!^\x1b[1;38;5;240m.
               \x1b[1;38;5;245m^\x1b[1;38;5;255m?JHJJ?\x1b[1;38;5;245m!!!!!!!!^
             \x1b[1;38;5;245m:\x1b[1;38;5;255m7JJIJJ?\x1b[1;38;5;245m!!!\x1b[1;38;5;240m^^\x1b[1;38;5;245m::\x1b[1;38;5;240m^^
           \x1b[1;38;5;245m^\x1b[1;38;5;255m!JJJNJJ7\x1b[1;38;5;245m!!!^\x1b[1;38;5;240m::\x1b[1;38;5;245m~~\x1b[1;38;5;240m::.
          \x1b[1;38;5;245m^\x1b[1;38;5;255m?JJTJJJ7\x1b[1;38;5;245m!!!!^.^!!^\x1b[1;38;5;240m:.
        \x1b[1;38;5;245m^\x1b[1;38;5;255m?JJYJJJJ7\x1b[1;38;5;245m!!!!!!^\x1b[1;38;5;240m:::..
      \x1b[1;38;5;245m:\x1b[1;38;5;255m7JJAJJJJ?\x1b[1;38;5;245m!!!!!!!!^
      \x1b[1;38;5;255m7JJJJJJJ?\x1b[1;38;5;245m!!!!!!!\x1b[1;38;5;240m~:
"""

	@final
	@property
	def client( self ) -> Client: return self.__client__

	def controller( self ) -> None:

		def bulletin( self:Niara ) -> None: ...
		
		def cluster( self:Niara ) -> None:
			cluster = self.thread( "Getting contents of cluster", lambda: self.client.controllerCluster() )
			self.output( cluster, tree( cluster ) )
			self.previous( self.controller, ">>>" )
		
		def config( self:Niara ) -> None:
			configs = self.thread( "Getting current NiFi configuration", lambda: self.client.controllerConfig() )
			self.output( cluster, [ tree( configs ) ] )
			self.previous( self.controller, ">>>" )

		options = [
			"/controller/bulletin", [
				"Creates a new bulletin"
			],
			"/controller/cluster", [
				"Gets the contents of the cluster"
			],
			# "/controller/cluster/nodes/{id}", [
			# 	"Gets a node in the cluster"
			# ],
			# "/controller/cluster/nodes/{id}", [
			# 	"Updates a node in the cluster"
			# ],
			# "/controller/cluster/nodes/{id}", [
			# 	"Removes a node from the cluster"
			# ],
			"/controller/config", [
				"Retrieves the configuration for this NiFi Controller"
			],
			# "/controller/config", [
			# 	"Retrieves the configuration for this NiFi"
			# ],
			"/controller/controller-services", [
				"Creates a new controller service"
			],
			"/controller/history", [
				"Purges history"
			],
			"/controller/parameter-providers", [
				"Creates a new parameter provider"
			],
			"/controller/registry-clients", [
				"Creates a new flow registry client"
			],
			"/controller/registry-clients", [
				"Gets the listing of available flow registry clients"
			],
			"/controller/registry-clients/{id}", [
				"Gets a flow registry client"
			],
			"/controller/registry-clients/{id}", [
				"Updates a flow registry client"
			],
			"/controller/registry-clients/{id}", [
				"Deletes a flow registry client"
			],
			"/controller/registry-clients/{id}/descriptors", [
				"Gets a flow registry client property descriptor"
			],
			"/controller/registry-types", [
				"Retrieves the types of flow that this NiFi supports"
			],
			"/controller/reporting-tasks", [
				"Creates a new reporting task"
			],
			"/controller/status/history", [
				"Gets status history for the node"
			],
			"Cancel", [
				"Back to main"
			]
		]
		self.output( self.controller, [ "Get controller configuration, Manage the cluster, Create reporting tasks\n", options ] )
		select = select = self.input( "Action", number=True, default=[ idx for idx in range( len( options ) ) ] )
		match select:
			case 1: bulletin( self )
			case 2: cluster( self )
			case 3: config( self )
			case 4: ...
			case 5: ...
			case 6: ...
			case 7: ...
			case 8: ...
			case 9: ...
			case 10: ...
			case 11: ...
			case 12: ...
			case 13: ...
			case 14: ...
			case 15: ...
			case 16: ...
			case 17: ...
			case 18: ...
			case 19: ...
			case _:
				self.main()

	def main( self ) -> None:
		if self.authenticated:
			options = [
				"Access", [
					"User authentication and token endpoints"
				],
				"Connections", [
					"Create a connection, Set queue priority, Update connection destination"
				],
				"Controller", [
					"Get controller configuration, Manage the cluster, Create reportingtasks"
				],
				"Controller Services", [
					"Manage controller services, Update controller service references"
				],
				"Counters", [
					"Get counters, Reset counters"
				],
				"Data Transfer", [
					"Send data, Receive data"
				],
				"Flow", [
					"Get the data flow, Obtain component status, Query history"
				],
				"FlowFile Queues", [
					"View queue contents, Download flowfile content, Empty queue"
				],
				"Funnels", [
					"Manage funnels"
				],
				"Input Ports", [
					"Create an input port, Set remote port access control"
				],
				"Labels", [
					"Create a label, Set label style"
				],
				"Output Ports", [
					"Create an output port, Set remote port access control"
				],
				"Parameter Contexts", [
					"Manage Parameter Contexts and associated validation"
				],
				"Parameter Providers", [
					"Manage Parameter Providers and associated validation"
				],
				"Policies", [
					"Get policies, Create policies"
				],
				"Process Groups", [
					"Create components, Instantiate a template, Upload a template"
				],
				"Processors", [
					"Create a processor, Set properties, Schedule"
				],
				"Provenance", [
					"Query provenance, Search event lineage"
				],
				"Provenance Events", [
					"Download content, Replay"
				],
				"Remote Process Groups", [
					"Create a remote group, Enable transmission"
				],
				"Reporting Tasks", [
					"Manage reporting tasks"
				],
				"Resources", [
					"Get resources"
				],
				"Site to Site", [
					"Get available ports, Get peers"
				],
				"Snippets", [
					"Create a snippet, Move a snippet, Delete a snippet"
				],
				"System Diagnostics", [
					"Get system diagnostics"
				],
				"Templates", [
					"Download a template, Delete a template"
				],
				"Tenants", [
					"Add users and group, Group users"
				],
				"Versions", [
					"Manage versions of process groups"
				],
				"Close", [
					"Close the program"
				]
			]
			self.output( self.main, [ "Available NiFi Endpoints\n", options ])
			select = self.input( "Action", number=True, default=[ idx for idx in range( len( options ) ) ] )
			match select:
				case 1: self.access()
				case 2: self.connection()
				case 3: self.controller()
				case 4: ...
				case 5: ...
				case 6: ...
				case 7: ...
				case 8: ...
				case 9: ...
				case 10: ...
				case 11: ...
				case 12: ...
				case 13: ...
				case 14: ...
				case 15: ...
				case 16: ...
				case 17: ...
				case 18: ...
				case 19: ...
				case 20: ...
				case 21: ...
				case 22: ...
				case 23: ...
				case 24: ...
				case 25: ...
				case 26: ...
				case 27: ...
				case 28: ...
				case _:
					self.close()
		else:
			self.output( self.main, "Oops! Looks like you haven't been authenticated" )
			self.tryAgain( "Next SignIn [Y/n]", next=self.signin, other=self.close )
	
	def signin( self, username:str=None, password:str=None ) -> None:
		if username is None:
			self.output( self.signin, "Please input your username" )
			username = self.input( "Username" )
		if password is None:
			self.output( self.signin, "Please input your password" )
			password = self.getpass( "Password" )
		signin = self.thread( f"Trying lo logging into {username}", lambda: self.client.signin( username=username, password=password ) )
		if signin is True:
			self.output( self.signin, "SignIn Successfully" )
			self.previous( self.main, ">>>" )
		else:
			self.output( self.signin )
			self.tryAgain( next=self.signin, other=self.close )

