import axios from 'axios'

const backendURL = 'http://127.0.0.1:6800'

export const getSpiderStatus = async (crawlerID) => {
  const response = await axios.get(`${backendURL}/listjobs`)
  console.log(response)
  console.log(crawlerID)
  return response
}

export const spiderFinished = async (response) => {
  if(response)
    return true
  else
    return false
}