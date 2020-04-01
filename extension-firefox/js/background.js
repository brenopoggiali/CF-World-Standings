document.addEventListener("DOMContentLoaded", function() {
	browser.tabs.query({currentWindow: true, active: true}).then((tabs) => {
		var tab = tabs[0];
		var tab_url = tab.url;
		var arg = tab_url.split("/");
		var options = ["gym", "contest"]
		browser.storage.local.get("lastCountryUrl", function(obj) {
			if (obj.lastCountryUrl) $("#selectedCountry").val(obj.lastCountryUrl);
		});
		if (options.includes(arg[3]) && arg[2] === "codeforces.com") {
			$("#found").show();
			$("#notFound").hide();
		}
		else {
			$("#found").hide();
			$("#notFound").show();
		}
	});
})

$("#goToStandings").click(() => {
	browser.tabs.query({currentWindow: true, active: true}).then((tabs) => {
		var tab = tabs[0];
		var tabUrl = tab.url;
		var arg = tabUrl.split('/');
		var listUrl = $("#selectedCountry").val();
		if (listUrl === null) {
			alert("Please select a country");
		}
		else {
			var newUrl = "https://codeforces.com/" + arg[3] + "/" + arg[4] + "/standings?list=" + listUrl;
			browser.storage.local.set({ "lastCountryUrl": listUrl });
			browser.tabs.update(tab.id, {url: newUrl});
		}
	});
})
