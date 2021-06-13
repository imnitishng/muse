import React from 'react'
import { useSelector } from 'react-redux'

const Track = ({ trackInfo, trackImage, trackNameToShow }) => {
  console.log(trackInfo)
  return (
    <>
      <li className="hover:bg-red-50 hover:text-gray-900 my-1 h-12 md:h-16">
        <div className="flex flex-row h-full w-full">
          <div className="flex items-center justify-center flex-none bg-green-500 w-9 max-h-full md:w-14">
            <div className="text-white text-base md:text-2xl font-condensed">
              { trackInfo.rank ? `${(trackInfo.rank*100).toFixed(1)}%` : '-' }
            </div>
          </div>
          <div className="flex-none">
            <img src={trackImage} alt={trackNameToShow} className="h-full"/>
          </div>
          <div className="pl-3 flex flex-col justify-center">
            <div className="truncate">
              {trackInfo.info.name}
            </div>
            <div className="text-xs truncate font-bold">
              {trackInfo.info.artists[0]}
            </div>
          </div>
        </div>
      </li>
    </>
  )
}

const RecommendationsBlock = () => {
  const fetchedSongsObj = useSelector(state => state.results)
  const spotifyTracks = fetchedSongsObj.recommendations

  return (
    <div className="flex-grow">
      <ul className="text-xs md:text-sm">
        {spotifyTracks.map(track =>
          <Track
            key={track.id}
            trackInfo={track}
            trackImage={track.info.album.images[2].url}
            trackNameToShow={track.nameToShow}
          />)}
      </ul>
    </div>
  )
}

export default RecommendationsBlock