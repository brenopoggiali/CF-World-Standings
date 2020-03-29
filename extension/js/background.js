document.addEventListener("DOMContentLoaded", function() {
	chrome.tabs.getSelected(null, function(tab) {
		var tab_url = tab.url;
		var arg = tab_url.split("/");
		var options = ["gym", "contest"]
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
	chrome.tabs.getSelected(null, function(tab) {
		var tabUrl = tab.url;
		var arg = tabUrl.split('/');
		var listUrl = $("#selectedCountry").val();
		if (listUrl === null) {
			alert("Please select a country");
		}
		else {
			var newUrl = "https://codeforces.com/" + arg[3] + "/" + arg[4] + "/standings?list=" + listUrl;
			chrome.tabs.update(tab.id, {url: newUrl});
		}
	});
})
