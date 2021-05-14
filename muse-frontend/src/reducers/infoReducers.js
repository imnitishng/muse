const initialState = {
  spotifyRecommendations: [],
}

export const infoReducer = (state = initialState, action) => {
  switch(action.type) {
  case 'ADD_SPOTIFY_RCMDS':
    return { spotifyRecommendations: action.data }
  default:
    return state
  }
}

export const addSpotifyRecommendations = (data) => (
  {
    type: 'ADD_SPOTIFY_RCMDS',
    data: data
  }
)
