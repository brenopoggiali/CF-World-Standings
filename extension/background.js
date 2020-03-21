chrome.browserAction.onClicked.addListener(function(tab) {
	var tab_url = tab.url;
	var arg = tab_url.split("/");
	var options = ["gym", "contest"]
	if (options.includes(arg[3]) && arg[2] === "codeforces.com") {
		var new_url = "https://codeforces.com/" + arg[3] + "/" + arg[4] + "/standings?list=572a105d225caf9f30256d5b10921a4c";
		chrome.tabs.update(tab.id, {url: new_url});
	}
	else {
		alert("Ops!\nParece que você não está dentro de um contest.");
	}
});
