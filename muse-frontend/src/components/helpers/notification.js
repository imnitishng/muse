import React from 'react'

const Notification = ({ content }) => {
  return (
    <div className="flex absolute w-full bottom-12">
      <div className="flex-grow">
        {content}
      </div>
    </div>
  )
}

export default Notification