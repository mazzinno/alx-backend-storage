-- Rank the
country origins of bands, ordered by the number of (non-unique) fans
SELECT
  origin,
  SUM(fans) nb_fans
FROM
  metal_bands
GROUP BY
  origin
ORDER BY
  nb_fans DESC
