import axios from 'axios'
import qs from 'qs';

const baseUrl = 'https://api.spotify.com/v1'
let accessToken = null

const searchSong = async songName => {
  console.log('serach song called')
  await getNewAccessToken()

  console.log('get token searching songs')

  const headers = {
    'Authorization':  `Bearer ${accessToken}`,
  }
  const data = {
    q: songName, 
    type: 'track',
    limit: 5
  }
  const requestBody = {
    method: 'get',
    url: `${baseUrl}/search?${qs.stringify(data)}`,
    headers: headers,
  }

  axios(requestBody)
    .then(response => {
      return response.data  
    })
    .catch(exception =>
      console.log(exception)
    )
  
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
  
  // axios(requestBody)
  //   .then(response => {
  //     accessToken = response.data.access_token
  //     console.log(response)
  //   })
  //   .catch(exception =>
  //     console.log(exception)
  //   )

  const response = await axios(requestBody)
  console.log('token recieved')
  accessToken = response.data.access_token
}

export default { searchSong }