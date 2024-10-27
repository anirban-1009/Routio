export interface Center {
  lat: number;
  long: number;
  center_id: string;
  quantity: number;
  ETA: string;
}

export interface Driver {
  driver_id: string;
  lat: number;
  long: number;
}

export interface RideData {
  user_id: string;
  center: Center;
  driver: Driver;
}

export interface UserData {
  user_id: string;
  name: string;
  email: string;
  address: string;
  is_driver: boolean;
  is_admin: boolean;
  center: string;
}

export interface UserDataAuth {
  name: string;
  email: string;
  sub: string;
  is_driver: boolean;
}

export interface Driver_GreenImpact {
  driver_id: string;
  distance_travelled: number;
  fuel_consumption: number;
  carbon_emission: number;
}

export interface GreenImpactData {
  user_id: string;
  center: string;
  driver: Driver_GreenImpact;
}

export interface TokenResponse {
  access_token: string;
  scope: string;
  expires_in: number;
  token_type: string;
}
