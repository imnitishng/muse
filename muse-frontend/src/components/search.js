import React, { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'

import spotifyService from '../services/SpotifyService'
import { sendSearchedTrackInfo } from '../services/BackendService'
import { addSearchResults, clearSearchResults } from '../reducers/searchReducers'
import { addSpotifyRecommendations } from '../reducers/infoReducers'
import { changeAppLayout } from '../reducers/styleReducers'


const ResultEntrySong = ({ setDisplay, item, itemImage, itemName, itemArtist }) => {
  const dispatch = useDispatch()

  const handleSearchClick = async (event) => {
    event.preventDefault()
    setDisplay({ display: 'none' })
    const response = await sendSearchedTrackInfo(item)
    dispatch(addSpotifyRecommendations(response.data))
    dispatch(changeAppLayout('withResults'))
  }

  return (
    <>
      <li className="py-0.5 cursor-pointer hover:bg-red-50 hover:text-gray-900">
        <div className="flex flex-nowrap" onClick={handleSearchClick}>
          <img src={itemImage} alt={itemName} className="flex-none h-50" width="50"/>
          <div className="ml-3">
            {itemName} - {itemArtist}
          </div>
        </div>
      </li>
    </>
  )
}

const SearchList = ({ results }) => {
  const [display, setDisplay] = useState({ display: '' })

  return (
    <div className="w-full" style={display}>
      <ul className="text-sm">
        {results.map(item =>
          <ResultEntrySong
            key={item.id}
            setDisplay={setDisplay}
            item={item}
            itemImage={item.album.images[2].url}
            itemName={item.name}
            itemArtist={item.artists[0].name}
          />)}
      </ul>
    </div>
  )
}

const SearchResults = ({ data }) => {
  if(data.search.searchResults.length > 0)
    return (
      <SearchList results={data.search.searchResults}/>
    )
  else
    return (
      <>
        Search a track
      </>
    )
}

const Search = () => {

  const dispatch = useDispatch()
  const [search, setSearch] = useState('')

  const getSongs = async () => {
    const songReturned = await spotifyService.searchSong(search)

    if(songReturned)
      dispatch(addSearchResults(songReturned.data.tracks.items))
  }

  const handleSearchChange = (event) => {
    event.preventDefault()
    setSearch(event.target.value)

    if(event.target.value.length > 3)
      getSongs()
    else
      dispatch(clearSearchResults())
  }

  return (
    <div className="mt-28 mx-14">
      <label className="font-mono text-gray-700 text-lg">
        <input id="search" onChange={handleSearchChange} className="border-4 border-transparent border-purple-600 w-full h-8 mx-auto rounded-md focus:border-teal-400" />
      </label>
      <SearchResults data={useSelector(state => state)}/>
    </div>
  )

}

export default Search