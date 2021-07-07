var _ = require('lodash')

const initialState = {
  query_id: null,
  recommendations: null
}

export const infoReducer = (state = initialState, action) => {

  const toTrackObj = (track) => ({
    rank: null,
    id: track[0],
    nameToShow: `${track[1].title} - ${track[1].main_artist}`,
    info: track[1],
  })

  switch(action.type) {

  case 'ADD_SPOTIFY_RCMDS': {
    const combinedArr = _.zip(
      action.data.recommended_track_ids,
      action.data.recommended_tracks
    )
    const recommendations = combinedArr.map(
      (track) => (toTrackObj(track))
    )

    return {
      query_id: action.data.recommendation_id,
      recommendations: recommendations
    }
  }

  case 'ASSIGN_RANKS': {
    const rankIDMap = _.reduce(action.ranks, function (result, value) {
      result[value.id] = [value.score, value.processed_text]
      return result
    }, {})

    const updatedRecommendations = action.recommendationsObj.recommendations.map(
      (track) => ({
        ...track,
        rank: rankIDMap[track.id][0],
        processedLyrics: rankIDMap[track.id][1]
      }))

    const sortedRecommendations = _.sortBy(
      updatedRecommendations,
      [(o) => (o.rank)]
    ).reverse()

    return {
      query_id: action.recommendationsObj.query_id,
      recommendations: sortedRecommendations
    }
  }

  default:
    return state
  }
}

export const addSpotifyRecommendations = (data) => (
  {
    type: 'ADD_SPOTIFY_RCMDS',
    data: data
  }
)

export const assignRanksToTracks = (response, recommendationsObj) => (
  {
    type: 'ASSIGN_RANKS',
    ranks: response.data.ranks,
    recommendationsObj
  }
)
