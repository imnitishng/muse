import React from 'react'
import { useSelector } from 'react-redux'

import StatusDisplay from './statusdisplay'

const RecommendationsTuner = () => {

  const recommendationsObj = useSelector(state => state.results)

  return (
    <div className="w:1/3">
      <StatusDisplay recommendationsObj={recommendationsObj}/>
    </div>
  )
}

export default RecommendationsTuner