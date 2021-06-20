import React from 'react'
import { Toaster } from 'react-hot-toast'

import Search from './components/search'
import RecommendationsPanel from './components/resultsPanel'
import RecommendationsBlock from './components/recommendations'
import RecommendationsTuner from './components/tunerPanel/tunerPanel'

const App = () => {

  return (
    <div className="flex flex-col justify-end font-body">
      <Search/>
      <RecommendationsPanel>
        <RecommendationsBlock />
        <RecommendationsTuner />
      </RecommendationsPanel>
      <Toaster
        position='bottom-right'
      />
    </div>
  )
}

export default App
