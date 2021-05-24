import React from 'react'

import './assets/main.css'
import Search from './components/search'
import RecommendationsPanel from './components/resultsPanel'
import RecommendationsBlock from './components/recommendations'

const App = () => {

  return (
    <div className="flex flex-col justify-end">
      <Search/>
      <RecommendationsPanel>
        <RecommendationsBlock />
      </RecommendationsPanel>
    </div>
  )
}

export default App
