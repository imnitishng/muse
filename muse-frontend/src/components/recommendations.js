import React from 'react'
import { useSelector } from 'react-redux'

const Track = ({ trackInfo, trackNameToShow, trackRank }) => {
  var trackRankClass
  if(trackRank) {
    // Map decimal ranks 0.21314 to the (nearest number divisble by 5)*10 = colorID
    var trackRankColorVal = (Math.floor((trackRank.toFixed(2)*20)/5)*5)*10
    trackRankColorVal = trackRankColorVal ? trackRankColorVal : trackRankColorVal + 10
    trackRankClass = `flex items-center justify-center flex-none bg-rankColor-${trackRankColorVal} w-9 max-h-full md:w-14`
  }
  else
    trackRankClass = 'flex items-center justify-center flex-none bg-gray-600 w-9 max-h-full md:w-14'

  return (
    <>
      <li className="cursor-default transition duration-300 ease-in-out hover:bg-red-50 hover:text-gray-900 my-1 h-12 md:h-16">
        <div className="flex flex-row h-full w-full">
          <div className={trackRankClass}>
            <div className="text-white text-base md:text-2xl font-condensed">
              { trackRank ? `${(trackRank*100).toFixed(1)}%` : '-' }
            </div>
          </div>
          <div className="flex-none p-1">
            <img src={trackInfo.album_art_md} alt={trackNameToShow} className="h-full shadow-2xl-darker"/>
          </div>
          <div className="pl-3 flex flex-col justify-center min-w-0">
            <div className="truncate font-bold">
              {trackInfo.title}
            </div>
            <div className="text-xs truncate">
              {trackInfo.main_artist}
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
            trackInfo={track.info}
            trackNameToShow={track.nameToShow}
            trackRank={track.rank}
          />)}
      </ul>
    </div>
  )
}

export default RecommendationsBlock