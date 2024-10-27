import { useState, useEffect } from 'react';


export const useGeolocation = (): [number[] | null, boolean, string | null] => {
  const [location, setLocation] = useState<number[] | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        ({ coords }) => {
          setLocation([coords.latitude, coords.longitude]);
          setIsLoading(false);
        },
        (error) => {
          setError(`Geolocation error: ${error.message}`);
          setIsLoading(false);
        }
      );
    } else {
      setError('Geolocation is not supported by this browser.');
      setIsLoading(false);
    }
  }, []);

  return [location, isLoading, error];
};


export async function getLatLongFromApi(): Promise<[number, number][]> {
  const apiUrl = `https://anirban9293.pythonanywhere.com/api/routes`;

  try {
      // Make the GET request to the API
      const response = await fetch(apiUrl);
      if (!response.ok) {
          throw new Error(`Failed to fetch data from the API. Status: ${response.status}`);
      }

      // Parse the JSON response
      const data = await response.json();

      // console.log(data);

      // Extract latitudes and longitudes from the response
      const latLngList: [number, number][] = [];
      for (const route of data) {
          for (const solution of route.result[0].solutions) {
              for (const vehicle of solution.vehicles) {
                  for (const stop of vehicle.route) {
                      const lat = stop.stop.location.lat;
                      const lng = stop.stop.location.lon;
                      latLngList.push([lat, lng]);
                  }
              }
          }
      }

      return latLngList;
  } catch (error) {
      // Handle HTTP errors or connection errors
      console.error(`Error: ${error}`);
      return [];
  }
}
