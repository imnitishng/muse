import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api'

export const fetchRanks = async (queryID) => {
  const requestBody = {
    recommendation_id: queryID,
    model_code: 'use'
  }
  const response = await axios.post(`${baseURL}/get_embeddings`, requestBody)
  return response
}

