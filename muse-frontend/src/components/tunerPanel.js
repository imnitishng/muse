import React from 'react'
import { useSelector } from 'react-redux'

import StatusDisplay from './statusdisplay'

const RecommendationsTuner = () => {

  const recommendationsObj = useSelector(state => state.results)

  return (
    <div>
      <StatusDisplay recommendationsObj={recommendationsObj}/>
    </div>
  )
}

export default RecommendationsTuner