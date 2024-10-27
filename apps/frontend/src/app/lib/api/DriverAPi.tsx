import axios from "axios";
import { UserDataAuth } from "../types/users";
import { DriverData } from "../types/drivers";
import { getCachedManagementApiToken } from "../utils/auth";

const base_url = process.env.NEXT_PUBLIC_BASE_URL

export const fetchDriverDataAndCreate = async (email: string, userDetail: UserDataAuth, attemptedCreate: boolean) => {
    try {
        const token = await getCachedManagementApiToken();
        const response = await axios.get(`${base_url}/api/drivers/?email=${encodeURI(email)}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data;
    }catch(error: any) {
        if (error.response?.status === 404 && !attemptedCreate) {
            const response = await CreateDriver(userDetail, 0, 0);
            return response;
          } else {
            console.error("Error fetching driver details", error);
        };
    }
};

export const fetchDriverData = async (email: string) => {
    try {
        const token = await getCachedManagementApiToken();
        const response = await axios.get(`${base_url}/api/drivers/?email=${encodeURI(email)}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data;
    }catch(error: any) {
        console.error("Error in fetching User Detail: ", error);
    }
};

export const fetchDriverGreenImpact = async (driver_id: string) => {
    try {
        const token = await getCachedManagementApiToken();
        const response = await axios.get(`${base_url}/api/drivers/${encodeURIComponent(driver_id)}/green-impact/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data;
    }catch (error) {
        console.error("Error fetching green impact details:", error);
    }
}

export const fetchDriverRoute = async (driver_id: string) => {
    try{
        const token = await getCachedManagementApiToken();
        const response = await axios.get(`${base_url}/api/drivers/${encodeURI(driver_id)}/navigate/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error fetching navigation details:", error);
    }

}

export const CreateDriver = async (user: UserDataAuth, lat: number, long: number): Promise<DriverData | null> => {
    try {
        const { is_driver, ...userDataWithoutIsDriver } = user;
        const data = { ...userDataWithoutIsDriver, lat, long };
        const token = await getCachedManagementApiToken();
        const response = await axios.post(`${base_url}/api/drivers/`, data, {
            headers: {
                Authorization: `Bearer ${token}`,
            }
        });
        return response.data as DriverData;
    } catch (error) {
        console.error("Error creating user", error);
        return null;
    }
}

export const updateDriverLocation = async (user_id: string, lat: number, long: number) => {
    try{
        const token = await getCachedManagementApiToken();
        const response = await axios.patch(`${base_url}/api/drivers/${user_id}/`, {
            lat: lat,
            long: long
        }, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
        return response.data as DriverData;
    } catch (error){
        console.error("Error in updating location: ", error)
    }
}