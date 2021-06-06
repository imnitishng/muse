import React from 'react'



const RanksReadyBtn = ({ handleGetTrackRanks }) => {

  const btnContent = 'Get Ranks'
  const btnClass = 'bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded'

  return  (
    <button className={btnClass} onClick={handleGetTrackRanks}>
      {btnContent}
    </button>
  )
}

export default RanksReadyBtn