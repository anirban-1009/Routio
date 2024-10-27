"use client";
import { useUser } from "@auth0/nextjs-auth0/client";
import { LatLngTuple } from "leaflet";
import "leaflet/dist/leaflet.css";
import dynamic from "next/dynamic";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import GreenImpact from "../components/GreenImpact";
import Hamburger from "../components/Hamburger";
import { fetchDriverGreenImpact, fetchDriverRoute } from "../lib/api/DriverAPi";
import { DriverData, GreenImpactData, NavDetail } from "../lib/types/drivers";

const Map = dynamic(() => import("../Map/map"), { ssr: false });

interface DriverProps {
  driverData: DriverData;
}

const Driver: React.FC<DriverProps> = ({ driverData }) => {
  const { user, error, isLoading } = useUser(); // Use useUser hook to get user data, error, and loading state
  const [driverEmail, setDriverEmail] = useState<string>("");
  const [location, setLocation] = useState<number[]>();
  const [greenimpact, setGreenImpact] = useState<GreenImpactData | null>(null);
  const [navdetail, setNavDetail] = useState<NavDetail | null>(null);
  const router = useRouter();

  useEffect(() => {
    if (!isLoading && !error && user?.email) {
      setDriverEmail(user.email);
    }
  }, [user, error, isLoading]);

  useEffect(() => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        ({ coords }) => {
          const { latitude, longitude } = coords;
          setLocation([latitude, longitude]);
          // handleUpdateDriverLocation(driverData.driver_id, latitude, longitude);
        },
        (error) => {
          console.error("Error getting location: ", error);
        },
      );
    } else {
      console.error("Geolocation is not available in this browser.");
    }
  }, []);

  useEffect(() => {
    if (driverData?.driver_id) {
      handleFetchDriverGreenImpact(driverData.driver_id);
      handleFetchDriverRoute(driverData.driver_id);
    }
  }, [driverData]);

  const handleFetchDriverGreenImpact = async (user_id: string) => {
    try {
      const data = await fetchDriverGreenImpact(user_id);
      setGreenImpact(data);
    } catch (error) {
      console.error("Error in fetching green impact details", error);
    }
  };

  const handleFetchDriverRoute = async (driver_id: string) => {
    try {
      const data = await fetchDriverRoute(driver_id);
      setNavDetail(data);
    } catch (error) {
      console.error("Error fetching navigation details", error);
    }
  };

  const renderMap = () => {
    if (!navdetail || !navdetail.centers || location === undefined) return null;
    const path: LatLngTuple[] = [
      [location[0], location[1]], // Add the top-level lat and long
      ...navdetail.centers.map(
        (center) => [center.lat, center.long] as LatLngTuple,
      ), // Spread the array of mapped centers
    ];

    return (
      <Map
        waypoints={path}
        admin={true}
        location={[location[0], location[1]]}
      />
    );
  };

  return (
    <main>
      <div className="flex flex-col h-screen bg-white">
        <div className="flex-1 block h-full">
          {renderMap()}
          <div className="px-4">
            <Hamburger />
            {driverData && driverData.centers[0] ? (
              <div className="absolute top-20 left-0 right-0 mx-auto bg-[#F5F7FF] h-auto w-60 rounded-lg py-2 px-8 text-black text-center">
                <p className="text-xl text-nowrap leading-normal">
                  Upcoming Center
                </p>
                <p className="text-sm">{driverData?.centers[0]?.center_id}</p>
              </div>
            ) : (
              <div className="absolute top-20 left-0 right-0 mx-auto bg-[#F5F7FF] h-auto w-fit rounded-lg py-2 px-8 text-black text-center">
                <p className="text-xl text-nowrap leading-normal">
                  No Upcoming Center
                </p>
              </div>
            )}
            {user?.picture && (
              <a
                className="absolute top-4 right-4 h-12 w-12 p-0.5 rounded-full bg-white"
                href="/profile"
                role="button"
              >
                <img
                  src={user?.picture}
                  alt="user image"
                  className="rounded-full cursor-pointer"
                  onClick={() => {
                    console.log("Image Clicked");
                    router.push("/profile");
                  }}
                />
              </a>
            )}
            {greenimpact && (
              <GreenImpact
                distance={greenimpact.distance_traveled}
                fuel={greenimpact.fuel_consumption}
                carbon_emission={greenimpact["carbon_emission"]}
              />
            )}
          </div>
        </div>
      </div>
    </main>
  );
};

export default Driver;
