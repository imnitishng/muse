import axios from 'axios'
import qs from 'qs'

const baseUrl = 'https://api.spotify.com/v1'
let accessToken = null

const searchSong = async songName => {
  await getNewAccessToken()

  const headers = {
    'Authorization':  `Bearer ${accessToken}`,
  }
  const data = {
    q: songName,
    type: 'track',
    limit: 10
  }
  const requestBody = {
    method: 'get',
    url: `${baseUrl}/search?${qs.stringify(data)}`,
    headers: headers,
  }

  const response = await axios(requestBody)
  return response
}


const getNewAccessToken = async () => {
  const clientToken = process.env.REACT_APP_CLIENT_SECRET_BASE64

  const tokenURL = 'https://accounts.spotify.com/api/token'

  const requestBody = {
    method: 'post',
    url: tokenURL,
    headers: {
      'Authorization': `Basic ${clientToken}`,
      'content-type': 'application/x-www-form-urlencoded'
    },
    data: qs.stringify({
      grant_type: 'client_credentials'
    })
  }

  const response = await axios(requestBody)
  accessToken = response.data.access_token
}

export default { searchSong }