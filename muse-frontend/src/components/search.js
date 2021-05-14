import React, { useState } from 'react'

import spotifyService from '../services/SpotifyService'

const ResultEntrySong = ({ itemImage, itemName, itemArtist }) => {
  return (
    <>
      <ul className="text-sm">
        <li className="py-0.5 cursor-pointer hover:bg-red-50 hover:text-gray-900">
          <div className="flex flex-nowrap">
            <img src={itemImage} alt={itemName} className="flex-none h-50" width="50"/>
            <div className="ml-3 flex-grow">
              {itemName} - {itemArtist}
            </div>
          </div>
        </li>
      </ul>
    </>
  )
}

const SearchList = ({ results }) => {
  return (
    <div>
      {results.items.map(item =>
        <ResultEntrySong
          key={item.id}
          itemImage={item.album.images[2].url}
          itemName={item.name}
          itemArtist={item.artists[0].name}
        />)}
    </div>
  )
}

const SearchResults = ({ songs }) => {
  if(songs)
    return (
      <SearchList results={songs}/>
    )
  else
    return (
      <>
        Search a track
      </>
    )
}

const Search = () => {

  const [search, setSearch] = useState('')
  const [songs, setSongs] = useState(null)

  const getSongs = async () => {
    const songReturned = await spotifyService.searchSong(search)

    if(songReturned)
      setSongs(songReturned.data.tracks)
  }

  const handleSearchChange = (event) => {
    event.preventDefault()
    setSearch(event.target.value)

    if(event.target.value.length > 3)
      getSongs()
    else
      setSongs(null)
  }

  return (
    <div className="mt-28 mx-14">
      <label className="font-mono text-gray-700 text-lg">
        <input id="search" onChange={handleSearchChange} className="border-4 border-transparent border-purple-600 w-full h-8 mx-auto rounded-md focus:border-teal-400" />
        <SearchResults songs={songs}/>
      </label>
    </div>
  )

}

export default Search