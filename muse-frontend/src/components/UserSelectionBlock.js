import React from 'react'
import { useSelector, useDispatch } from 'react-redux'

import '../assets/selection.css'
import { clearSearchResults } from '../reducers/searchReducers'
import { changeAppLayout } from '../reducers/styleReducers'


const UserSelectionBlock = () => {
  const dispatch = useDispatch()
  const selectedTrack = useSelector(state => state.search.userSelection)

  const handleTrackDeselect = (event) => {
    event.preventDefault()
    const ele = document.getElementById('search')
    ele.value = ''
    dispatch(changeAppLayout('regular'))
    dispatch(clearSearchResults())
  }

  return (
    <div className="overflow-hidden relative rounded-lg shadow-xl my-3">
      <img src={selectedTrack.album.images[0].url} id='blurred'/>
      <div className="md:w-max flex items-center justify-between px-3 py-1 relative
      font-sans text-xs md:text-base">
        <img src={selectedTrack.album.images[0].url} id='cover' className="w-12 md:w-20"/>
        <div className="px-2 w-40 md:w-full">
          <p className="mix-blend-overlay truncate md:overflow-clip ">
            {selectedTrack.name}
          </p>
        </div>
        <button className="w-3 md:w-7 mix-blend-overlay" onClick={handleTrackDeselect}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 329.26933 329">
            <path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0"/>
          </svg>
        </button>
      </div>
    </div>
  )
}

export default UserSelectionBlock