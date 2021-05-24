import { createStore, combineReducers } from 'redux'

import { composeWithDevTools } from 'redux-devtools-extension'
import { searchReducer } from './reducers/searchReducers'
import { infoReducer } from './reducers/infoReducers'
import { styleReducer } from './reducers/styleReducers'

const reducer = combineReducers({
  search: searchReducer,
  results: infoReducer,
  layout: styleReducer
})

const store = createStore(
  reducer,
  composeWithDevTools()
)

export default store