import axios from 'axios'

import { getHost  } from '../utils/helper'

const hostURL = getHost()
const baseURL = `${hostURL}/api/spotify`

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
