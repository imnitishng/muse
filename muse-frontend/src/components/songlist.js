import React, { useState, useEffect } from 'react'
import spotifyService from '../services/SpotifyService'

const SongList = ({songName}) => {
  const [songs, setSongs] = useState(null)

  console.log('before sf')
  const songReturned = spotifyService.searchSong(songName)
  console.log(songReturned)
  if(songReturned) 
    setSongs(songReturned.tracks)
  console.log('after sf')

  return (
    <>
    songs found
    </>
  )
}

export default SongList