import React from 'react'
import Loader from '../helpers/loader'

const RanksLoadingBtn = () => {
  const btnClass = `flex items-center 
    bg-transparent
    text-sm text-green-700 font-semibold 
    hover:text-white cursor-wait
    py-2 px-4 h-8 md:h-12
    border border-blue-500`
  const btnContent = 'Ranking Tracks'

  return (
    <button className={btnClass}>
      {btnContent}
      <div className="ml-3">
        <Loader />
      </div>
    </button>
  )
}

export default RanksLoadingBtn