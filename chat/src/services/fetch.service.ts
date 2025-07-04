import { showError } from "./errors.service";

const debug = true;

const API_URL = process.env.NEXT_PUBLIC_API_URL;

if (!API_URL) {
  throw new Error("BASE_URL environment variable is not set");
}

export const appFetch = async (pathWithSlashAthBeggning: string, options?: RequestInit): Promise<Response | null> => {
    if (debug) {
      console.log("Fetch URL:", `${API_URL}${pathWithSlashAthBeggning}`);
      console.log("Fetch Options:", options);
    }

  try {
    const response = await fetch(`${API_URL}${pathWithSlashAthBeggning}`, options);


    const body = await response.json();

    return body;
  } catch (error) {
    showError("Error fetching data:", error);

    return null;
  }
}
