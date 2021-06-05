import React from 'react'

import './assets/main.css'
import Search from './components/search'
import RecommendationsPanel from './components/resultsPanel'
import RecommendationsBlock from './components/recommendations'
import RecommendationsTuner from './components/tunerPanel'

const App = () => {

  return (
    <div className="flex flex-col justify-end">
      <Search/>
      <RecommendationsPanel>
        <div className="md:flex md:flex-row justify-around">
          <RecommendationsBlock />
          <RecommendationsTuner />
        </div>
      </RecommendationsPanel>
    </div>
  )
}

export default App
