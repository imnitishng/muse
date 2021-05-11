import React, { useState } from 'react'
import spotifyService from '../services/SpotifyService'

const SongList = ({ songName }) => {
  const [songs, setSongs] = useState(null)

  console.log('before sf')
  const songReturned = spotifyService.searchSong(songName)
  console.log(songReturned)
  if(songReturned)
    setSongs(songReturned.tracks)
  console.log('after sf')
  console.log(songs)

  return (
    <>
    songs found
    </>
  )
}

export default SongList