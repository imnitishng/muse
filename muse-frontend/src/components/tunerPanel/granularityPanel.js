import React, { useState, useSelector } from 'react'
import { useDispatch } from 'react-redux'

import RangeSlider  from '../helpers/rangeSlider'
import { getRecommendationWithSeeds } from '../../services/BackendService'
import { addSpotifyRecommendations } from '../../reducers/infoReducers'

const GranularitySlider = () => {
  // The steps for respective properties are calculated as per the API values
  // A step of 0.1 means minval = 0*0.1 = 0 and maxval = 10*0.1 = 1
  // The steps of `Tempo` are based on the respective API values i.e. minval=50 and maxval=208

  const dispatch = useDispatch()
  const selectedTrack = useSelector(state => state.search.userSelection)

  const [trackFeatures, setTrackFeatures] = useState({
    Popularity: null,
    Energy: null,
    Acousticness: null,
    Tempo: null,
    Danceability: null,
    Instrumentalness: null,
    Speechiness: null,
  })

  const getNewRecommendations = async (propertyName, newVal) => {
    setTrackFeatures({
      ...trackFeatures,
      [propertyName]: newVal
    })
    const response = await getRecommendationWithSeeds(selectedTrack, setTrackFeatures)
    dispatch(addSpotifyRecommendations(response.data))
  }

  return (
    <div className="border-gray-200 border rounded-md grid grid-flow-row gap-7 shadow-lg p-4" >
      <RangeSlider trackProperty="Popularity" step={10} sliderFn={getNewRecommendations} />
      <RangeSlider trackProperty="Energy" step={0.1} sliderFn={getNewRecommendations} />
      <RangeSlider trackProperty="Acousticness" step={0.1} sliderFn={getNewRecommendations} />
      <RangeSlider trackProperty="Tempo" step={15.8} sliderFn={getNewRecommendations} />
      <RangeSlider trackProperty="Danceability" factor={0.1} sliderFn={getNewRecommendations} />
      <RangeSlider trackProperty="Instrumentalness" factor={0.1} sliderFn={getNewRecommendations} />
      <RangeSlider trackProperty="Speechiness" factor={0.1} sliderFn={getNewRecommendations} />
    </div>
  )
}

export default GranularitySlider
