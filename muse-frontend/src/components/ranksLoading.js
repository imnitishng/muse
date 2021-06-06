import React from 'react'

import { useInterval } from '../utils/polling'
import { getSpiderStatus, getFinishedSpiders } from '../services/SpiderService'

const SPIDER_POLLING_INTERVAL = 1000

const RanksLoadingBtn = ({ setSpiderJobStatus, crawlerKey }) => {

  const handleSpiderFinished = async () => {
    const response = await getSpiderStatus()
    const finishedSpiderIDs = getFinishedSpiders(response)
    if(finishedSpiderIDs.includes(crawlerKey)) {
      setSpiderJobStatus('finished')
    }
  }

  useInterval(
    async () => {
      await handleSpiderFinished()
    },
    SPIDER_POLLING_INTERVAL
  )

  const btnClass = 'bg-transparent hover:bg-blue-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded'
  const btnContent = 'Loading'

  return  (
    <button className={btnClass}>
      {btnContent}
    </button>
  )
}

export default RanksLoadingBtn