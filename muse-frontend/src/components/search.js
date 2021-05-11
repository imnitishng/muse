import React, { useState } from 'react'
import SongList from './songlist'

const SearchResults = ({ songName }) => {
  if(songName.length > 3) {
    return (
      <>
        <SongList songName={songName}/>
      </>
    )
  }
  else {
    return (
      <div>
        <p>nothing searched</p>
      </div>
    )
  }
}

const Search = () => {

  const [search, setSearch] = useState('')

  const handleSearchChange = (event) => {
    console.log(event.target.value)
    setSearch(event.target.value)
  }

  return (
    <>
      <label className="block font-medium font-mono text-gray-700 text-lg">
      Search a song
        <input id="search" onChange={handleSearchChange} className="border-4 border-transparent border-purple-600 focus:border-teal-400 w-full h-12 mx-auto rounded-md" />
        <SearchResults songName={search}/>
      </label>
    </>
  )

}

export default Search