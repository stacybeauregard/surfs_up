# surfs_up
## Module 9 Challenge

### Overview of Analysis

This week we are partnering with a professional surfer to obtain an investment in our surfing and ice cream shop we'd like to open. Our partner, W. Avy, has asked that we get more specific with our analysis of Oahu weather and take a look at June and December data specifically. While we are only looking at those two months, we are analyzing a decade's worth of data. This will be helpful analysis for presenting to any other potential investors as well as determining if this is a sound year-round investment for W. Avy.

### Results

#### June vs. December "Is Surf n' Shake sustainable year-round?" 

* June and December have pretty similar average temps for each month over the last decade. June average is 75 and December's is 71. This makes for consistent weather to enjoy outdoor activities.

* While their average temperatures are very similar, December does get colder than June. December's minimum temperature is 56 and June is 64. Although we see this nearly 10 degree difference in lows, their high temps of 85 for June and 83 for December are promising that we'll all still want ice cream in the winter!

* There may be some slight inconsistencies in the data as June has a collection of 1700 dates and December only has 1517. Since there is a decades worth of data though, I think we can feel good about our analysis.

![June](https://github.com/stacybeauregard/surfs_up/blob/main/Resources/JuneSummary.png)

![Dec](https://github.com/stacybeauregard/surfs_up/blob/main/Resources/DecSummary.png)

### Summary

From this analysis we can gather that the temperatures are similar, although December has more temperature swings. We may want to run off from reduced hours and start at a later time each day in December until the temperatures rise to a more "profitable" degree.

I suggest that queries are ran in regards to precipitation for each month. Do warmer temps in June bring rain? or is is colder in December because of clouds and storms?

June Query: june_results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date ==6).all()

December Query: dec_results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date ==12).all()

