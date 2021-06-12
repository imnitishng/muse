import React from 'react'

import Search from './components/search'
import RecommendationsPanel from './components/resultsPanel'
import RecommendationsBlock from './components/recommendations'
import RecommendationsTuner from './components/TunerPanel/tunerPanel'

const App = () => {

  return (
    <div className="flex flex-col justify-end">
      <Search/>
      <RecommendationsPanel>
        <RecommendationsBlock />
        <RecommendationsTuner />
      </RecommendationsPanel>
    </div>
  )
}

export default App
