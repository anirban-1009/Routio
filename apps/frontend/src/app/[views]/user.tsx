`use client`;
import { useUser } from '@auth0/nextjs-auth0/client';
import { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import { LatLngTuple } from 'leaflet';
import 'leaflet/dist/leaflet.css';
import Hamburger from '../components/Hamburger';
import GreenImpact from '../components/GreenImpact';
import { fetchUserData, fetchUserGreenImpact, fetchUserRide } from '../lib/api/UserAPi';
import { UserData, GreenImpactData, RideData } from '../lib/types/users';

// Interface Defining the Type of Data It takes in
interface UserProps {
    userdata: UserData;
}

// Importing Map Component on which we will display out waypoints and markers based on data
const Map = dynamic(() => import('../Map/map'), { ssr: false });

const User: React.FC<UserProps> = ({userdata}) => {
    
    const { user, error, isLoading } = useUser(); // Use useUser hook to get user data, error, and loading state
    const [greenimpact, setGreenImpact] = useState<GreenImpactData | null>(null);
    const [userride, setRideData] = useState<RideData | null>(null);

    // Effect to fetch green impact and ride data when `userdata` changes
    useEffect(() => {
        if (userdata?.user_id) {
            handleFetchUserGreenImpact(userdata.user_id);
            handleFetchUserRide(userdata.user_id);
        }
    }, [userdata])

    // Function to handle fetching user's green impact details
    const handleFetchUserGreenImpact = async (user_id: string) => {
        try {
            // Call fetchUserGreenImpact with the given user_id and await the response
            const data = await fetchUserGreenImpact(user_id);
    
            // Store the fetched data in the state variable greenImpact
            setGreenImpact(data);
        } catch (error) {
            // Log an error message to the console if an error occurs
            console.error("Error in fetching green impact details", error);
        }
    }

    // Function to handle fetching user's ride details
    const handleFetchUserRide = async (user_id: string) => {
        try {
            // Call fetchUserRide with the given user_id and await the response
            const data = await fetchUserRide(user_id);

            // Store the fetched data in the state variable rideData
            setRideData(data);
        } catch (error) {
            // Log an error message to the console if an error occurs
            console.error("Error fetching ride details", error);
        }
    }

    const renderMap = () => {
        // Render a default map if `userride` is not defined
        if (!userride) return (
            <div className="flex flex-col h-screen bg-white justify-center items-center">
                <p className="text-center text-blue-500 border-4 p-10 rounded-lg border-dashed">{userdata.name} you are yet to be assigned to a center...</p>
            </div>
        );
        if (!userride?.driver && userride?.center) return <Map admin={false} location={[userride?.center.lat, userride?.center.long]}/>;
    
        // Define waypoints for the map using latitude and longitude coordinates
        const waypoints: LatLngTuple[] = [
            [userride.driver.lat, userride.driver.long], // Driver's location
            [userride.center.lat, userride.center.long] // Center's location
        ];
    
        // Render the map component with waypoints and driver's location
        return <Map waypoints={waypoints} admin={false} location={[userride.center.lat, userride.center.long]} />;
    };
    
    return (
        <main>
            <div className="flex flex-col h-screen bg-white">
            <div className="flex-1 block h-full">
                {/* This Section is call to render tha map on display */}
                {renderMap()} 
                <div className='px-4'>
                {/* HamBurger menu is called for the mobile view  */}
                <Hamburger />
                {/* This section renders the top island on the Application to show the ETA of the Vehicle */}
                {userride && (
                    <div className='absolute top-20 left-0 right-0 mx-auto bg-[#F5F7FF] h-auto w-60 rounded-lg py-2 px-8 text-black text-center'>
                    <p className='text-2xl leading-normal'>Next PickUp  at</p>
                    <p className='text-sm'>{
                        new Date(userride.center.ETA)
                        .toLocaleString('en-IN', {
                            timeZone: 'Asia/Kolkata',
                        })
                    }</p>
                </div>
                )}
                <a className='absolute top-4 right-4 h-12 w-12'>
                    <img src={user?.picture || 'profile.svg'} alt='user image' className='rounded-full'/>
                </a>
                {/* In this section the GreenImpact component is rendered if the data is available which shows the live stats of the vehicle */}
                {greenimpact && (
                <GreenImpact
                    distance={greenimpact.driver.distance_travelled}
                    fuel={greenimpact.driver.fuel_consumption}
                    carbon_emission={greenimpact.driver.carbon_emission}
                />
                )}
                </div>
            </div>
            </div>
        </main>
    )
}

export default User;