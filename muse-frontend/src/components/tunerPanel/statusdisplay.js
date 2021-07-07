import React, { useState, useEffect } from 'react'
import { useDispatch } from 'react-redux'
import toast from 'react-hot-toast'

import SpiderReadyBtn from './spiderReadyBtn'
import SpiderRunningBtn from './spiderLoadingBtn'
import RanksLoadingBtn from './ranksLoadingBtn'
import FinishedProcessBtn from './finishedProcessBtn'
import SpiderRunningToast from '../helpers/spiderRunningToast'

import { startLyricsFetch } from '../../services/SpiderService'
import { fetchRanks } from '../../services/ModelService'
import { assignRanksToTracks } from '../../reducers/infoReducers'

const StatusDisplay = ({ recommendationsObj }) => {
  const dispatch = useDispatch()

  // render info based on spider status: (one of) 'waiting', 'running', 'finished', 'dead'
  const [spiderJobStatus, setSpiderJobStatus] = useState('waiting')
  const [crawlerKey, setCrawlerKey] = useState(null)

  useEffect(() => {
    if(spiderJobStatus === 'running') {
      const toastId = toast.custom(
        (t) => {
          t.duration = Infinity
          return (
            <SpiderRunningToast tracks={recommendationsObj.recommendations}/>
          )
        }
      )
      window.localStorage.setItem('toastId', toastId)
    }
    else if(spiderJobStatus === 'finished') {
      const toastId = window.localStorage.getItem('toastId')
      if(toastId !== null)
        toast.success('Lyrics fetched!', {
          id: toastId,
          duration: 3000
        })
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [spiderJobStatus])

  const handleGetLyrics = async (event) => {
    event.preventDefault()
    const response = await startLyricsFetch(recommendationsObj.query_id)
    setCrawlerKey(response.data.job_id)
    setSpiderJobStatus('running')
  }

  const getTrackRanks = async () => {
    const rankToastID = toast.loading('Ranking Tracks')

    const response = await fetchRanks(recommendationsObj.query_id)
    toast.success('Done!', {
      id: rankToastID,
      duration: 3000
    })

    setSpiderJobStatus('dead')
    dispatch(assignRanksToTracks(response, recommendationsObj))
  }

  useEffect(() => {
    if(spiderJobStatus === 'finished')
      getTrackRanks()
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [spiderJobStatus])

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
    return (
      <>
        <RanksLoadingBtn />
      </>
    )
  }
  else {
    return(
      <FinishedProcessBtn />
    )
  }
}

export default StatusDisplay