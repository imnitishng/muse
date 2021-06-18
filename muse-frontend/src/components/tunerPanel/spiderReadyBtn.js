import React from 'react'

const SpiderReadyBtn = ({ handleGetLyrics }) => {

  const btnContent = 'Enrich'
  const btnClass = `flex items-center
    transition duration-500 ease-in-out 
    bg-transparent hover:bg-blue-500 text-blue-700 
    font-semibold text-sm hover:text-white 
    py-2 px-4 h-8 md:h-12
    border border-blue-500 hover:border-transparent`

  return  (
    <button className={btnClass} onClick={handleGetLyrics}>
      {btnContent}
    </button>
  )
}

export default SpiderReadyBtn