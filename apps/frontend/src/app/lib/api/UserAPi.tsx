import axios from "axios";
import { UserData, UserDataAuth } from "../types/users";
import { getCachedManagementApiToken } from "../utils/auth";

const base_url = process.env.NEXT_PUBLIC_BASE_URL

export const fetchUserDataAndCreate = async (email: string, userDetail: UserDataAuth, attemptedCreate: boolean) => {
    try {
        const token = await getCachedManagementApiToken()
        const response = await axios.get(`${base_url}/api/users/?email=${encodeURI(email)}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data;
    } catch (error: any) {
        if (error.response?.status === 404 && !attemptedCreate) {
            const response = await CreateUser(userDetail);
            return response;
          } else {
            console.error("Error fetching user details", error);
        };
    }
};

export const fetchUserData = async (email: string ) => {
    try {
        const token = await getCachedManagementApiToken()
        const response = await axios.get(`${base_url}/api/users/?email=${encodeURI(email)}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data;
    } catch (error: any) {
        console.error("User details not fetched: ", error)
    }
};


export const fetchUserGreenImpact = async (user_id: string) => {
    try {
        const token = await getCachedManagementApiToken();
        const response = await axios.get(`${base_url}/api/users/${encodeURIComponent(user_id)}/green-impact/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error fetching green impact details:", error);
    }
};

export const fetchUserRide = async (user_id: string) => {
    try {
        const token = await getCachedManagementApiToken();
        // Using axios to make the GET request
        const response = await axios.get(`${base_url}/api/users/${encodeURIComponent(user_id)}/driver/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        
        // Assuming setRideData is a function to update the state with the fetched data
        return response.data;
    } catch (error) {
        console.error("Error fetching ride details:", error);
    }
};

export const CreateUser = async (user: UserDataAuth):Promise<UserData | null> => {
    try {
        const token = await getCachedManagementApiToken();
        const response = await axios.post(`${base_url}/api/users/`, user, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        });
        return response.data as UserData;
    } catch (error) {
        console.error("Error creating user", error)
        return null;
    }
}