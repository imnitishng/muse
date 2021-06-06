import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/spiders'

export const startLyricsFetch = async (queryID) => {
  const requestBody = {
    query_id: queryID
  }

  const response = await axios.post(`${baseURL}/start`, requestBody)
  console.log(response)
  return response
}

export const getSpiderStatus = async () => {
  const response = await axios.get(`${baseURL}/status`)
  console.log(response)
  return response
}

export const spiderFinished = async (response, crawlerID) => {
  if(crawlerID in response.data.finished)
    return true
  return false
}
