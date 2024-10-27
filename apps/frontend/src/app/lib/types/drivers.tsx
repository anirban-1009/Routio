export interface Center {
    center_id: string;
    lat: number;
    long: number;
    date_last_updated: string;
    ETA: string | null;
    in_schedule: boolean;
    quantity: number;
    driver: string;
}

export interface DriverData {
    driver_id: string;
    centers: Center[] | [];
    name: string;
    email: string;
    registration_id: string;
    distance_traveled: string;
    fuel_consumption: string;
    lat: number;
    long: number;
}

export interface NavDetail {
    driver_id: string;
    lat: number;
    long: number;
    centers: {
        center_id: string;
        lat: number;
        long: number;
    }[];
}

export interface GreenImpactData {
    driver_id: string;
    distance_traveled: number;
    fuel_consumption: number;
    carbon_emission: number;
}