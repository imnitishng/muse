import axios from 'axios'

const backendURL = 'http://127.0.0.1:8000/api/v1'

export const sendSearchedTrackInfo = async (trackObj) => {

  const requestBody = {
    spotifyObj: JSON.stringify(trackObj)
  }

  const response = await axios.post(`${backendURL}/sp_recommedations`, requestBody)
  console.log(response)

  return response
}
