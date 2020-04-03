/* eslint-disable no-undef */
document.addEventListener('DOMContentLoaded', function () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var tab = tabs[0]
    var tabUrl = tab.url
    var arg = tabUrl.split('/')
    var options = ['gym', 'contest']
    chrome.storage.sync.get('lastCountryUrl', function (obj) {
      if (obj.lastCountryUrl) $('#selectedCountry').val(obj.lastCountryUrl)
    })
    if (options.includes(arg[3]) && arg[2] === 'codeforces.com') {
      $('#found').show()
      $('#notFound').hide()
    } else {
      $('#found').hide()
      $('#notFound').show()
    }
  })
})

$('#goToStandings').click(() => {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var tab = tabs[0]
    var tabUrl = tab.url
    var arg = tabUrl.split('/')
    var listUrl = $('#selectedCountry').val()
    if (listUrl === null) {
      alert('Please select a country')
    } else {
      var newUrl = 'https://codeforces.com/' + arg[3] + '/' + arg[4] + '/standings?list=' + listUrl
      chrome.storage.sync.set({ lastCountryUrl: listUrl })
      chrome.tabs.update(tab.id, { url: newUrl })
    }
  })
})
