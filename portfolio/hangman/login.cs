﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace hangman
{
    public class Login
    {
        public string Username { get; set; }
        public string Password { get; set; }

		public Login() {}

		public Login(string username, string password)
		{
			Username = username;
			Password = password;
		}

    }
}
