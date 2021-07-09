const initialState = {
  searchResults: [],
  userSelection: []
}

export const searchReducer = (state = initialState, action) => {
  switch(action.type) {
  case 'ADD_SEARCH_RESULTS':
    return {
      ...state,
      searchResults: action.data
    }

  case 'CLEAR_SEARCH_RESULTS':
    return {
      ...state,
      searchResults: []
    }

  case 'ADD_USER_TRACK_SELECTION': {
    return {
      ...state,
      userSelection: action.tracks
    }
  }

  default:
    return state
  }
}

export const addSearchResults = (data) => (
  {
    type: 'ADD_SEARCH_RESULTS',
    data: data
  }
)

export const clearSearchResults = () => (
  {
    type: 'CLEAR_SEARCH_RESULTS',
  }
)

export const addUserTrackSelection = (tracks) => (
  {
    type: 'ADD_USER_TRACK_SELECTION',
    tracks: tracks
  }
)

export const clearUserTrackSelection = () => (
  {
    type: 'CLEAR_USER_TRACK_SELECTION'
  }
)