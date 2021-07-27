import axios from 'axios'
import { getHost  } from '../utils/helper'


const hostURL = getHost()
const baseURL = `${hostURL}/api/spiders`

export const startLyricsFetch = async (queryID) => {
  const requestBody = {
    recommendation_id: queryID
  }
  const response = await axios.post(`${baseURL}/start`, requestBody)
  return response
}

export const getSpiderStatus = async () => {
  const response = await axios.get(`${baseURL}/status`)
  return response
}

export const getFinishedSpiders = (response) => {
  const finishedSpiders = response.data.finished
  const spiderIDs = []
  finishedSpiders.forEach(
    (finishedSpiderInfo) => {spiderIDs.push(finishedSpiderInfo['id'])}
  )
  return spiderIDs
}
