export const showError = (msg: string, error: unknown): void => {
  if (error instanceof Error) {
    console.error(msg, error.message);
  }

  console.error(msg, JSON.stringify(error, null, 2));
}
