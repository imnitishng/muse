import axios from 'axios'

const backendURL = 'http://127.0.0.1:8000/api/v1'

export const getAccessToken = async () => {
  const response = await axios.get(`${backendURL}/access_token`)
  return response
}

export const sendSearchedTrackInfo = async (trackObj) => {

  const requestBody = {
    spotifyObj: JSON.stringify(trackObj)
  }

  const response = await axios.post(`${backendURL}/sp_recommedations`, requestBody)
  console.log(response)

  return response
}

export const startLyricsFetch = async (queryID) => {

  const requestBody = {
    query_id: queryID
  }

  const response = await axios.post(`${backendURL}/start_fetch`, requestBody)
  console.log(response)
  return response
}
