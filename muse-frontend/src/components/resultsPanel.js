import React from 'react'
import { useSelector } from 'react-redux'

const ResultsPanel = (props) => {
  const AppLayout = useSelector(state => state.layout)

  if(AppLayout.appLayout === 'withResults')
    return (
      <div>
        { props.children }
      </div>
    )
  else
    return (
      <p className="text-center hidden md:mb-4 md:absolute inset-x-0 bottom-0">
        Music recommendations powered by lyric analysis.
      </p>
    )
}

export default ResultsPanel