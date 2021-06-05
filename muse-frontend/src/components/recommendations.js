import React from 'react'
import { useSelector } from 'react-redux'

const Track = ({  trackInfo, trackImage, trackName }) => {
  return (
    <>
      <li className="py-0.5 cursor-pointer hover:bg-red-50 hover:text-gray-900">
        <div className="flex flex-wrap">
          <img src={trackImage} alt={trackName} className="flex-none h-50" width="50"/>
          <div className="ml-3">
            {trackName} - {trackInfo.artists[0]}
          </div>
        </div>
      </li>
    </>
  )
}

const RecommendationsBlock = () => {
  const fetchedSongsObj = useSelector(state => state.results)
  const spotifyTracks = fetchedSongsObj.spotifyRecommendations.recommendations_obj.tracks

  return (
    <div>
      <ul className="text-sm">
        {spotifyTracks.map(track =>
          <Track
            key={track.id}
            trackInfo={track}
            trackImage={track.album.images[2].url}
            trackName={track.name}
          />)}
      </ul>
    </div>
  )
}

export default RecommendationsBlock