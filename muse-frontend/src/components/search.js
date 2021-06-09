import React, { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'

import spotifyService from '../services/SpotifyService'
import { sendSearchedTrackInfo } from '../services/BackendService'
import { addSearchResults, clearSearchResults } from '../reducers/searchReducers'
import { addSpotifyRecommendations } from '../reducers/infoReducers'
import { changeAppLayout } from '../reducers/styleReducers'


const ResultEntrySong = ({ setShowSuggestions, item, itemImage, itemName, itemArtist }) => {
  const dispatch = useDispatch()

  const handleSearchClick = async (event) => {
    event.preventDefault()
    setShowSuggestions(false)
    const response = await sendSearchedTrackInfo(item)
    dispatch(addSpotifyRecommendations(response.data))
    dispatch(changeAppLayout('withResults'))
  }

  return (
    <>
      <li
        className="py-0.5 cursor-pointer hover:bg-red-50 hover:text-gray-900"
        onMouseDown={(e) => e.preventDefault()}>
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

const SearchList = ({ results, setShowSuggestions }) => {

  return (
    <div className="w-full z-10 md:absolute bg-white border-gray-100 border-2 shadow-2xl">
      <ul className="text-sm">
        {results.map(item =>
          <ResultEntrySong
            key={item.id}
            setShowSuggestions={setShowSuggestions}
            item={item}
            itemImage={item.album.images[2].url}
            itemName={item.name}
            itemArtist={item.artists[0].name}
          />)}
      </ul>
    </div>
  )
}

const SearchResults = ({ data, showSuggestions, setShowSuggestions }) => {
  if(data.search.searchResults.length > 0 && showSuggestions === true)
    return (
      <SearchList results={data.search.searchResults} setShowSuggestions={setShowSuggestions}/>
    )
  else if((data.search.searchResults.length === 0))
    return (
      <>
        Search a track
      </>
    )
  else
    return (
      <>
      </>
    )
}

const Search = () => {

  const dispatch = useDispatch()
  const [search, setSearch] = useState('')
  const [showSuggestions, setShowSuggestions] = useState(false)

  const getSongs = async () => {
    const songReturned = await spotifyService.searchSong(search)

    if(songReturned)
      dispatch(addSearchResults(songReturned.data.tracks.items))
  }

  const handleSearchChange = (event) => {
    event.preventDefault()
    setShowSuggestions(true)
    setSearch(event.target.value)

    if(event.target.value.length > 3)
      getSongs()
    else
      dispatch(clearSearchResults())
  }

  return (
    <div className="mt-28 w-5/6 self-center">
      <label className="font-mono text-gray-700 text-lg">
        <input id="search"
          className="border-4 border-transparent border-purple-600 w-full h-8 mx-auto rounded-md focus:border-teal-400"
          onChange={handleSearchChange}
          onFocus={() => setShowSuggestions(true)}
          onBlur={() => setShowSuggestions(false)}
        />
      </label>
      <div className="relative">
        <SearchResults data={useSelector(state => state)}
          showSuggestions={showSuggestions}
          setShowSuggestions={setShowSuggestions}/>
      </div>
    </div>
  )

}

export default Search