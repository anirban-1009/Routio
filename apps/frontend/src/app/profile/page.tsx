"use client"
import { useUser } from "@auth0/nextjs-auth0/client";
import { useRouter } from "next/navigation";
import { MdOutlineKeyboardArrowRight } from "react-icons/md";
import { RxCross1 } from "react-icons/rx";
import { IoIosLogOut } from "react-icons/io";
import { useEffect, useState } from "react";
import { fetchUserData } from "../lib/api/UserAPi";
import { fetchDriverData } from "../lib/api/DriverAPi";

const Profile = () => {
  const { user, error, isLoading } = useUser();
  const [userEmail, setUserEmail] = useState<string>('');
  const [userdata, setUserData] = useState(null);

  const renderData = () => {
    if (!userdata) return null;

    const data = [
      {'Name': user?.name},
      {'Email': user?.email},
      userdata['driver_id'] ? { 'Registration ID': userdata['registration_id'] } : { 'Address': userdata['address'] }
    ];

    return (
      <div className="flex flex-col gap-8">
        {data.map((item, index) => {
          const label = Object.keys(item)[0]; // Extracting the label
          const value = Object.values(item)[0]; // Extracting the value
          return (
            <div key={index} className="h-28 w-88 bg-[#3E60FF4D] rounded-3xl py-4 px-6">
              <div className="flex justify-between items-center w-full h-full">
                <div className="flex h-full text-wrap flex-col">
                  <u className="text-xl items-start">{label}</u>
                  <p className="text-3xl max-w-64 truncate text-wrap">{value}</p>
                </div>
                <div className="flex h-full items-center">
                  <MdOutlineKeyboardArrowRight className="flex h-14 w-14"/>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    )
  }

  const router = useRouter();

  useEffect(() => {
    if (!isLoading && !error && user?.email) {
      setUserEmail(user.email);
    }
  }, [user, error, isLoading]);

  useEffect(() => {
    if (userEmail !== null && userEmail !== "") {
      handlefetchUserData(userEmail);
    }
  }, [userEmail]);

  const handlefetchUserData = async (email: string) => {
    try {
      const userdata = await fetchUserData(email);
      setUserData(userdata);
    } catch (error) {
      try {
        const driverData = await fetchDriverData(email);
        setUserData(driverData);
      } catch (innerError: any) {
        console.error("Error fetching user details:", innerError.message);
      }
    }
  };

  return (
      <div className="h-screen w-screen bg-white px-8 pt-20 text-black">
          <IoIosLogOut className="absolute left-0 top-0  h-10 w-10 mt-8 ml-8" onClick={() => router.push('/api/auth/logout')}/>
          <RxCross1 className="absolute right-0 top-0  h-10 w-10 mt-8 mr-8" onClick={() => router.push('/')}/>
          {user?.picture ? (
              <img src={user?.picture} alt="user-image" className="rounded-full h-40 w-40 m-auto"/>
          ) : (
              <img src='profile.svg' alt='user-imgae' className="rounded-full h-40 w-40 m-auto" />
          )}
          <p className="pl-8 text-xl pt-12 pb-4 ">Basic Info</p>
          {renderData()}
      </div>
  );
};

export default Profile;