document.getElementById('runButton').addEventListener('click', sendGetRequest)
document
  .getElementById('deleteButton')
  .addEventListener('click', removeContainer)

async function removeContainer () {
  const currentTab = await getCurrentTab()
  const currentUrl = currentTab.url

  var currUrl = new URL(currentUrl)
  cPort = currUrl.port

  fetch('http://localhost:5000/delete', {
    method: 'POST',
    body: JSON.stringify({
      port: currUrl.port
    }),
    headers: {
      'Content-type': 'application/json; charset=UTF-8'
    }
  })
}

async function sendGetRequest () {
  const currentTab = await getCurrentTab() // Get the current tab
  const currentUrl = currentTab.url // Get the URL of the current tab
  console.log('Current URL:', currentUrl)

  let body = {
    url: currentUrl,
    follow_redirects: false
  }

  risk_score = 8
  if (risk_score < 10) {
    const fUrl = `http://localhost:5000/?url=${currentUrl}`

    try {
      const response = await fetch(fUrl, {
        method: 'GET'
      })

      if (!response.ok) {
        throw new Error('Network response was not ok')
      }

      const data = await response.json()
      console.log(data.remoteUrl)
      window.open(data.remoteUrl)
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error)
    }
  }
  console.log('Risk: ' + risk_score)
}

function getCurrentTab () {
  return new Promise((resolve, reject) => {
    chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
      if (tabs && tabs.length > 0) {
        resolve(tabs[0])
      } else {
        reject(new Error('Unable to get current tab.'))
      }
    })
  })
}
