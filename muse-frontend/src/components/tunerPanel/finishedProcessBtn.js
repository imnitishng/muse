import React from 'react'

const FinishedProcessBtn = () => {
  const btnClass = `flex items-center
    bg-transparent text-green-500
    font-semibold text-sm cursor-default
    py-2 px-4 h-8 md:h-12 justify-center
    border border-green-500`
  const btnContent = 'Done'

  return (
    <button className={btnClass}>
      {btnContent}
    </button>
  )
}

export default FinishedProcessBtn