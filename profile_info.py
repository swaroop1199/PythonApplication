import asyncio
import aiohttp


async def get_profile(access_token):
    """
    Fetches the user's profile information using the Spotify API.

    :param access_token: Spotify API access token.
    :return: The profile data as a dictionary.
    """
    url = "https://api.spotify.com/v1/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print(f"Failed to fetch profile. Status code: {response.status}")
                print(await response.text())
                return None


# Example usage
async def main():
    # Replace with the actual token retrieval logic
    access_token = "BQD-5yZgBm-7lnIZvTU2Z2HBPbWuyBm5-W05R4pLYH-JB6KL7wyVSF7lfEHBFc8Aj-h8ZHAyjRn99_UCQ3-EA7KFLndo5TNPdhjLP45xzzD1GqeLUsQ"

    profile_data = await get_profile(access_token)
    if profile_data:
        print("Profile Data:", profile_data)


# Run the script
if __name__ == "__main__":
    asyncio.run(main())
