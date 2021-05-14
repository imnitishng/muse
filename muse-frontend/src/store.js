import { createStore, combineReducers } from 'redux'

import { composeWithDevTools } from 'redux-devtools-extension'
import { searchReducer } from './reducers/searchReducers'
import { infoReducer } from './reducers/infoReducers'

const reducer = combineReducers({
  search: searchReducer,
  results: infoReducer
})

const store = createStore(
  reducer,
  composeWithDevTools()
)

export default store