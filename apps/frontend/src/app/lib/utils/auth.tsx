import axios from "axios";
import NodeCache from "node-cache";
import CryptoJS from "crypto-js";
import { TokenResponse } from "../types/users";

const cache = new NodeCache();

const getManagementApiToken = async (): Promise<TokenResponse> => {
  const base_url = process.env.NEXT_PUBLIC_BASE_URL;
  const secret = process.env.NEXT_PUBLIC_CLIENT_ID;
  var key = process.env.NEXT_PUBLIC_SECRET_KEY;

  try {
    if (secret && key) {
      var encrypt_key = CryptoJS.enc.Utf8.parse(key);
      const encrypted_secret = CryptoJS.AES.encrypt(secret, encrypt_key, {
        mode: CryptoJS.mode.ECB,
      }).toString();
      const response = await axios.post(`${base_url}/api/auth/token/`, {
        key: encrypted_secret,
      });
      return response.data;
    } else {
      throw new Error("Environment variables not configured.");
    }
  } catch (error) {
    console.error("Error fetching management API token:", error);
    throw new Error("Failed to retrieve management API token");
  }
};

export const getCachedManagementApiToken = async (): Promise<string> => {
  let token = cache.get<TokenResponse>("auth_api_token");
  if (!token) {
    token = await getManagementApiToken();
    cache.set("auth_api_token", token, token.expires_in); // Cache the token for 1 hour
  }
  return token.access_token;
};
