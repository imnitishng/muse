import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api'

export const fetchRanks = async (songIDs) => {
  const requestBody = {
    type: 'semi',
    songs: songIDs,
    model: 'use'
  }
  const response = await axios.post(`${baseURL}/get_embeddings`, requestBody)
  return response
}

