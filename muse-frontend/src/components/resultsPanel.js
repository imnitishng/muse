import React from 'react'
import { useSelector } from 'react-redux'
import UserSelectionBlock from './UserSelectionBlock'


const ResultsPanel = (props) => {
  const AppLayout = useSelector(state => state.layout)

  if(AppLayout.appLayout === 'withResults')
    return (
      <div className="flex flex-col items-center">
        <UserSelectionBlock />
        <div className="w-11/12 md:flex md:flex-row self-center">
          { props.children }
        </div>
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