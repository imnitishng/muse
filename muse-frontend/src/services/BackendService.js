import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/spotify'

export const getAccessToken = async () => {
  const response = await axios.get(`${baseURL}/accesstoken`)
  return response
}

export const sendSearchedTrackInfo = async (trackObj) => {
  const requestBody = {
    spotifyObj: JSON.stringify(trackObj)
  }

  const response = await axios.post(`${baseURL}/recommendations`, requestBody)
  return response
}

