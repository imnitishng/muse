import React from 'react'
import { useSelector } from 'react-redux'

const Track = ({  trackImage, trackNameToShow }) => {
  return (
    <>
      <li className="py-0.5 cursor-pointer hover:bg-red-50 hover:text-gray-900">
        <div className="flex flex-row">
          <div className="flex-none">
            <img src={trackImage} alt={trackNameToShow} className="h-50" width="50"/>
          </div>
          <div className="ml-3 truncate">
            {trackNameToShow}
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
      <ul className="text-sm">
        {spotifyTracks.map(track =>
          <Track
            key={track.id}
            trackInfo={track.info}
            trackImage={track.info.album.images[2].url}
            trackNameToShow={track.nameToShow}
          />)}
      </ul>
    </div>
  )
}

export default RecommendationsBlock