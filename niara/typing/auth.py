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
from yutiriti import Typing

#[niara.typing.auth.Authorization]
@final
class Authorization( Typing ):

	#[Authorization.__items__]: Dict<Str, Str>|List<Str>
	@property
	def __items__( self ) -> dict[str:str]|list[str]:
		return [
			"cookies",
			"username",
			"password"
		]