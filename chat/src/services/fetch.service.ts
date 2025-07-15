import { showError } from "./errors.service";

const debug = true;


export const appFetch = async (pathWithSlashAthBeggning: string, options?: RequestInit): Promise<string | null> => {
  if (debug) {
    console.log("Fetch URL:", `/api/${pathWithSlashAthBeggning}`);
    console.log("Fetch Options:", options);
  }

  try {
    const response = await fetch(`/api/${pathWithSlashAthBeggning}`, options);


    const body = await response.text();

    return body;
  } catch (error) {
    showError("Error fetching data:", error);

    return null;
  }
}

export const appFetchStream = async (pathWithSlashAthBeggning: string, options?: RequestInit): Promise<Response> => {
  if (debug) {
    console.log("Fetch Stream URL:", `/api/${pathWithSlashAthBeggning}`);
    console.log("Fetch Stream Options:", options);
  }

  try {
    const response = await fetch(`/api/${pathWithSlashAthBeggning}`, options);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response;
  } catch (error) {
    showError("Error fetching stream:", error);
    throw error;
  }
}
