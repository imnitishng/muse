import React, { useState } from 'react'
import { useDispatch } from 'react-redux'

import SpiderReadyBtn from './spiderReadyBtn'
import SpiderRunningBtn from './spiderLoadingBtn'
import RanksLoadingBtn from './ranksLoadingBtn'

import { startLyricsFetch } from '../../services/SpiderService'
import { fetchRanks } from '../../services/ModelService'
import { assignRanksToTracks } from '../../reducers/infoReducers'

const StatusDisplay = ({ recommendationsObj }) => {
  const dispatch = useDispatch()

  // render info based on spider status: (one of) 'waiting', 'running', 'finished', 'dead'
  const [spiderJobStatus, setSpiderJobStatus] = useState('waiting')
  const [crawlerKey, setCrawlerKey] = useState(null)

  const handleGetLyrics = async (event) => {
    event.preventDefault()
    const response = await startLyricsFetch(recommendationsObj.query_id)
    setCrawlerKey(response.data.job_id)
    setSpiderJobStatus('running')
  }

  const getTrackRanks = async () => {
    const recommendation_ids = recommendationsObj.recommendations.map((e) => (e.id))
    const response = await fetchRanks(recommendation_ids)
    setSpiderJobStatus('dead')
    dispatch(assignRanksToTracks(response, recommendationsObj))
  }

  if(spiderJobStatus === 'waiting') {
    return (
      <>
        <SpiderReadyBtn
          handleGetLyrics={handleGetLyrics}
        />
      </>
    )
  }
  else if(spiderJobStatus === 'running') {
    return (
      <>
        <SpiderRunningBtn
          setSpiderJobStatus={setSpiderJobStatus}
          crawlerKey={crawlerKey}
        />
      </>
    )
  }
  else if(spiderJobStatus === 'finished') {
    getTrackRanks()
    return (
      <>
        <RanksLoadingBtn />
      </>
    )
  }
  else {
    return(
      <>
        Done
      </>
    )
  }
}

export default StatusDisplay