import axios from 'axios'
import { getHost  } from '../utils/helper'


const hostURL = getHost()
const baseURL = `${hostURL}/api`

export const fetchRanks = async (queryID) => {
  const requestBody = {
    recommendation_id: queryID,
    model_code: 'use'
  }
  const response = await axios.post(`${baseURL}/get_embeddings`, requestBody)
  return response
}

