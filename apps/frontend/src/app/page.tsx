"use client";
import { UserProfile, useUser } from "@auth0/nextjs-auth0/client";
import { redirect } from "next/navigation";
import { useEffect, useState } from "react";
import dynamic from "next/dynamic";
import "leaflet/dist/leaflet.css";
import { useRouter } from "next/navigation";
import User from "./[views]/user";
import Driver from "./[views]/driver";
import { UserData, UserDataAuth } from "./lib/types/users";
import { DriverData } from "./lib/types/drivers";
import {
  CreateDriver,
  fetchDriverData,
  fetchDriverDataAndCreate,
} from "./lib/api/DriverAPi";
import {
  CreateUser,
  fetchUserData,
  fetchUserDataAndCreate,
} from "./lib/api/UserAPi";

const Map = dynamic(() => import("./Map/map"), { ssr: false });

interface Auth0User extends UserProfile {
  "UserInformation/roles"?: string[];
}

const isAuth0User = (user: UserProfile): user is Auth0User => {
  return "UserInformation/roles" in user && "sid" in user;
};

export default function Home() {
  const { user, error, isLoading } = useUser();
  const [userDetail, setUserDetail] = useState<UserDataAuth | null>(null);
  const [driverData, setDriverData] = useState<DriverData | null>(null);
  const [userData, setUserData] = useState<UserData | null>(null);
  const [attemptedCreate, setAttemptedCreate] = useState<boolean>(false);
  const router = useRouter();

  useEffect(() => {
    if (!isLoading && error) {
      redirect("/api/auth/login");
    }
  }, [isLoading, error]);

  useEffect(() => {
    if (user && isAuth0User(user)) {
      const userDataAuth: UserDataAuth = {
        name: user.name ?? "",
        email: user.email ?? "test@mail.com",
        sub: user.sub ?? "",
        is_driver: user["UserInformation/roles"]?.includes("Driver") ?? false,
      };
      setUserDetail(userDataAuth);
    }
  }, [user]);

  useEffect(() => {
    if (userDetail?.email) {
      if (userDetail.is_driver) {
        handleFetchDriverData(userDetail.email);
      } else {
        handleFetchUserData(userDetail.email);
      }
    }
  }, [userDetail]);

  const handleFetchDriverData = async (email: string) => {
    if (userDetail) {
      try {
        setAttemptedCreate(true);
        const data = await fetchDriverDataAndCreate(
          email,
          userDetail,
          attemptedCreate,
        );
        setDriverData(data);
      } catch (error: any) {
        console.error("Error in getting user detail", error);
      }
    }
  };

  const handleFetchUserData = async (email: string) => {
    if (userDetail) {
      try {
        setAttemptedCreate(true);
        const data = await fetchUserDataAndCreate(
          email,
          userDetail,
          attemptedCreate,
        );
        setUserData(data);
      } catch (error: any) {
        console.error("Error in getting user detail", error);
      }
    }
  };

  if (driverData) {
    return <Driver driverData={driverData}></Driver>;
  } else if (userData) {
    return <User userdata={userData}></User>;
  }

  if (isLoading) {
    return (
      <div className="flex flex-col h-screen bg-white justify-center items-center">
        <p className="text-center text-red-500">Loading...</p>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="flex flex-col h-screen bg-white justify-center items-center">
        <p className="text-center text-red-500">
          User not logged in, sorry :'(
        </p>
        <button
          className="h-10 w-20 rounded-md mt-4 bg-blue-600 text-white"
          onClick={() => router.push("/api/auth/login")}
        >
          Login!!
        </button>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-screen bg-white justify-center items-center">
      <p className="text-center text-red-500">{user.email}</p>
    </div>
  );
}
