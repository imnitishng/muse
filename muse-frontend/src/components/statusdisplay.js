import React, { useState } from 'react'

import RanksReadyBtn from './ranksReady'
import RanksLoadingBtn from './ranksLoading'

import { startLyricsFetch } from '../services/BackendService'

const StatusDisplay = ({ recommendationsObj }) => {

  // render info based on spider status: (one of) 'waiting', 'running', 'finished'
  const [spiderJobStatus, setSpiderJobStatus] = useState('waiting')
  const [crawlerKey, setCrawlerKey] = useState(null)

  const handleGetTrackRanks = async (event) => {
    event.preventDefault()
    const response = await startLyricsFetch(recommendationsObj.spotifyRecommendations.query_id)
    setCrawlerKey(response.data.job_id)
    setSpiderJobStatus('running')
  }

  if(spiderJobStatus === 'waiting')
    return (
      <>
        <RanksReadyBtn
          handleGetTrackRanks={handleGetTrackRanks}
        />
      </>
    )
  else if(spiderJobStatus === 'running')
    return (
      <>
        <RanksLoadingBtn
          setSpiderJobStatus={setSpiderJobStatus}
          crawlerKey={crawlerKey}
        />
      </>
    )
  else
    return (
      <>
        Done
      </>
    )
}

export default StatusDisplay