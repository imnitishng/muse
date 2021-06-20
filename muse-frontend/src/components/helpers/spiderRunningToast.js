import React, { useState } from 'react'

import { useInterval } from '../../utils/polling'
import Spinner from './spinner'

// spider runs for approx 30 secs for 50 tracks
const REFRESH_RATE = 50/30*1000

const SpiderRunningToast = ({ tracks }) => {
  const [trackIndex, setTrackIndex] = useState(0)

  const changeTrackImg = () => {
    if(trackIndex < tracks.length-1)
      setTrackIndex(trackIndex+1)
  }

  useInterval(
    () => {
      changeTrackImg()
    },
    REFRESH_RATE
  )

  const trackImgURL = tracks[trackIndex].info.album.images[0].url
  console.log(trackImgURL)

  return (
    <div className='flex flex-col justify-around w-4/12 bg-white shadow-2xl rounded-md text-center text-sm md:w-3/12 lg:w-1.5/12'>
      <div className='p-1'>
        <img src={trackImgURL} className='w-full'/>
      </div>
      <div className='p-2 flex flex-row justify-evenly items-center max-h-full'>
        <Spinner />
        Fetching Lyrics
      </div>
    </div>
  )
}

export default SpiderRunningToast