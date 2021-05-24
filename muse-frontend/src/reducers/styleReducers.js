// regular: default layout with only a search bar on the page
// withResults: layout of the page after getting results from backend

const initialState = {
  appLayout: 'regular'
}

export const styleReducer = (state = initialState, action) => {
  switch(action.type) {
  case 'CHANGE_LAYOUT':
    return { appLayout: action.data }
  default:
    return state
  }
}

export const changeAppLayout = (data) => (
  {
    type: 'CHANGE_LAYOUT',
    data: data
  }
)
