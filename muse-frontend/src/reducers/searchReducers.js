const initialState = {
  searchResults: [],
}

export const searchReducer = (state = initialState, action) => {
  switch(action.type) {
  case 'ADD_SEARCH_RESULTS':
    return { searchResults: action.data }
  case 'CLEAR_SEARCH_RESULTS':
    return { searchResults: [] }
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