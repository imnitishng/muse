import React from 'react'
import Loader from '../helpers/loader'

import { useInterval } from '../../utils/polling'
import { getSpiderStatus, getFinishedSpiders } from '../../services/SpiderService'

const SPIDER_POLLING_INTERVAL = 1000

const SpiderRunningBtn = ({ setSpiderJobStatus, crawlerKey }) => {

  const handleSpiderFinished = async () => {
    const response = await getSpiderStatus()
    const finishedSpiderIDs = getFinishedSpiders(response)
    if(finishedSpiderIDs.includes(crawlerKey)) {
      setSpiderJobStatus('finished')
    }
  }

  useInterval(
    () => {
      handleSpiderFinished()
    },
    SPIDER_POLLING_INTERVAL
  )

  const btnClass = `flex items-center 
    bg-transparent hover:bg-blue-500 
    text-sm text-green-700 font-semibold 
    hover:text-white cursor-wait
    py-2 px-4 h-8 md:h-12
    border border-blue-500 hover:border-transparent`
  const btnContent = 'Fetching Lyrics'

  return  (
    <button className={btnClass}>
      {btnContent}
      <div className="ml-3">
        <Loader />
      </div>
    </button>
  )
}

export default SpiderRunningBtn