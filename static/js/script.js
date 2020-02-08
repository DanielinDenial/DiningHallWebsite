const ratings = {
  sherman_average_ratings: 2.5,
  usdan_average_ratings: 5;

for (const rating in ratings) {
  const starPercentage = ratings[rating] / 5 * 100;
  const starPercentageRounded = `${Math.round(starPercentage / 10) * 10}%`;
  document.querySelector(`.${rating} .stars-inner`).style.width = starPercentageRounded}
