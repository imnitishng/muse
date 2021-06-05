import React from 'react'



const RanksReadyBtn = ({ handleGetTrackRanks }) => {

  const btnContent = 'Get Ranks'
  const btnClass = 'bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded'
  // if(buttonType === 'jobrunning') {
  //   btnClass = 'bg-transparent hover:bg-blue-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded'
  //   btnContent = 'Loading'
  // }

  return  (
    <button className={btnClass} onClick={handleGetTrackRanks}>
      {btnContent}
    </button>
  )
}

export default RanksReadyBtn