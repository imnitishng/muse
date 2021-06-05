import axios from 'axios'
import qs from 'qs'

import { getAccessToken } from './BackendService'

const baseUrl = 'https://api.spotify.com/v1'

const searchSong = async songName => {

  const getRequestBody = () => {
    const accessToken = window.localStorage.getItem('access_token')

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

    return requestBody
  }

  let response = null
  try {
    response = await axios(getRequestBody())
  }
  catch(e) {
    await setNewAccessToken()
    response = await axios(getRequestBody())
  }
  return response
}


const setNewAccessToken = async () => {
  const response = await getAccessToken()
  const accessToken = response.data.access_token
  window.localStorage.setItem('access_token', accessToken)
}

export default { searchSong }