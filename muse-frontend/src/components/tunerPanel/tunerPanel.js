import React from 'react'
import { useSelector } from 'react-redux'

import StatusDisplay from './statusdisplay'
import GranularitySlider from './granularityPanel'

const RecommendationsTuner = () => {

  const recommendationsObj = useSelector(state => state.results)

  return (
    <div>
      <GranularitySlider />
      <div className="mt-5">
        <StatusDisplay recommendationsObj={recommendationsObj}/>
      </div>
    </div>
  )
}

export default RecommendationsTuner