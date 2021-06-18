import React from 'react'

import Search from './components/search'
import RecommendationsPanel from './components/resultsPanel'
import RecommendationsBlock from './components/recommendations'
import RecommendationsTuner from './components/tunerPanel/tunerPanel'
import Notification from './components/helpers/notification'

const App = () => {

  return (
    <div className="flex flex-col justify-end font-body">
      <Search/>
      <RecommendationsPanel>
        <RecommendationsBlock />
        <RecommendationsTuner />
      </RecommendationsPanel>
      <Notification content={'testing a long notification'}/>
    </div>
  )
}

export default App
