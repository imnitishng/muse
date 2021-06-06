import React from 'react'

import { useInterval } from '../utils/polling'
import { getSpiderStatus, spiderFinished } from '../services/SpiderService'

const SPIDER_POLLING_INTERVAL = 1000

const RanksLoadingBtn = ({ setSpiderJobStatus, crawlerKey }) => {

  useInterval(
    async () => {
      console.log('Getting spider status')
      const response = await getSpiderStatus()
      if(spiderFinished(response, crawlerKey)) {
        setSpiderJobStatus('finished')
      }
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