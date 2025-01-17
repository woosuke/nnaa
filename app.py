import streamlit as st
import requests
import pandas as pd

# Streamlit page setup
st.set_page_config(page_title="Real Estate Listings Viewer", layout="wide")
st.title("Real Estate Listings from Pages 1 to 10")
st.markdown("This page fetches and displays real estate listings from pages 1 to 10 using the Naver Real Estate API.")

# Define the cookies and headers as provided
cookies = {
    'NAC': 'EOiSBcwrxJWz',
    'NACT': '1',
    'NNB': '4SAJXCGXVKEWO',
    'SRT30': '1737092325',
    'page_uid': 'iGFWBwqVN8wss5oyvvlssssssaC-127274',
    'ASID': 'dda7dbba0000019472c957530000006d',
    'nid_inf': '3632551',
    'NID_AUT': '2Q8aK3GsswEXfBzyumcB8v7KdwBJvROpLVpHHyIoxtdXfotGHBin/m/e0hLUyNTZ',
    'NID_SES': 'AAABuDlEuYAvPLdtGFB6q+BM+/vgKMcWhadHG+IEZJVltyopnM0xiQJXN7bo5R0l4D99XPKsTcR9u/vl4BaNiN48xNv9zq1Tn1vhrjt/zebNY6Sfr1XxNwU5M91nNIFqGGhIiaEXrpCgHVnw6R4S+7LTizaAlhHJbQOlMQy9HSKQB20SCwQh3/DwmIQlyC5kG2xsURf7eKEkX+fZauPzFq5iindG2v7SEjiHrNdKyccB0cdtXRjfUtKKIHJgOEfdzw3yii7wpBA+yPFk0PqcIL8chmnwCiY24PV0wVdKzsYzeJL30hcCU2IkxKWNjyOKUhjwPQeSSdPsutPbLrJ7405TzXnasQDrm3o0GAehpugkNBEcrIE2bAGiDP0ANagfdcOnFWa65p+id7iY4IVmjSjzICeCqe3ZB32V+FCwW8qxwmHUiggzXqPEabDAI3dCfysDkWWc5/2K1r02tNLpTAbjNjPPhqMwEWzy+UMcyZUYB5D3nUJ86a6zuFhxM7+eE6HUYcitu8iLKYtI4cFeZntV5dywgpGSqXlZnAKXpdIWH1/deZfyKbDhuna1frGtamIiUcyc4ERo8sKB8vLnNzYwNag=',
    'NID_JKL': 'gYT1n2vlze3zKaiIqnJ28VyF7ac23efbTdAbpPuS4xo=',
    '_fwb': '56cMZ2UJkIRUBldl9jdnLj.1737095591432',
    'REALESTATE': 'Fri%20Jan%2017%202025%2015%3A36%3A40%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'RjZqJVvM6GPpZ5FKMTlImpTJT3zKeo_rgYviFOWXNf8=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MzcwOTU4MDAsImV4cCI6MTczNzEwNjYwMH0.2oCygaQP2rYUTfCPMyiI3atuN19jO6wY9oBnX6k5Uo4',
    # 'cookie': 'NAC=EOiSBcwrxJWz; NACT=1; NNB=4SAJXCGXVKEWO; SRT30=1737092325; page_uid=iGFWBwqVN8wss5oyvvlssssssaC-127274; ASID=dda7dbba0000019472c957530000006d; nid_inf=3632551; NID_AUT=2Q8aK3GsswEXfBzyumcB8v7KdwBJvROpLVpHHyIoxtdXfotGHBin/m/e0hLUyNTZ; NID_SES=AAABuDlEuYAvPLdtGFB6q+BM+/vgKMcWhadHG+IEZJVltyopnM0xiQJXN7bo5R0l4D99XPKsTcR9u/vl4BaNiN48xNv9zq1Tn1vhrjt/zebNY6Sfr1XxNwU5M91nNIFqGGhIiaEXrpCgHVnw6R4S+7LTizaAlhHJbQOlMQy9HSKQB20SCwQh3/DwmIQlyC5kG2xsURf7eKEkX+fZauPzFq5iindG2v7SEjiHrNdKyccB0cdtXRjfUtKKIHJgOEfdzw3yii7wpBA+yPFk0PqcIL8chmnwCiY24PV0wVdKzsYzeJL30hcCU2IkxKWNjyOKUhjwPQeSSdPsutPbLrJ7405TzXnasQDrm3o0GAehpugkNBEcrIE2bAGiDP0ANagfdcOnFWa65p+id7iY4IVmjSjzICeCqe3ZB32V+FCwW8qxwmHUiggzXqPEabDAI3dCfysDkWWc5/2K1r02tNLpTAbjNjPPhqMwEWzy+UMcyZUYB5D3nUJ86a6zuFhxM7+eE6HUYcitu8iLKYtI4cFeZntV5dywgpGSqXlZnAKXpdIWH1/deZfyKbDhuna1frGtamIiUcyc4ERo8sKB8vLnNzYwNag=; NID_JKL=gYT1n2vlze3zKaiIqnJ28VyF7ac23efbTdAbpPuS4xo=; _fwb=56cMZ2UJkIRUBldl9jdnLj.1737095591432; REALESTATE=Fri%20Jan%2017%202025%2015%3A36%3A40%20GMT%2B0900%20(Korean%20Standard%20Time); BUC=RjZqJVvM6GPpZ5FKMTlImpTJT3zKeo_rgYviFOWXNf8=',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/111515?ms=37.497624,127.107268,17&a=APT:ABYG:JGC:PRE&e=RETAIL',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


# Function to get data from the API for pages 1 to 10
@st.cache_data
def fetch_all_data():
    all_articles = []
    for page in range(1, 11):
        try:
            # Make the request for the specific page
            url = f'https://new.land.naver.com/api/articles/complex/111515?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={page}&complexNo=111515&buildingNos=&areaNos=&type=list&order=rank'
            response = requests.get(url, cookies=cookies, headers=headers)

            # Verify response is valid JSON
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articleList", [])
                all_articles.extend(articles)
            else:
                st.warning(f"Failed to retrieve data for page {page}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
        except ValueError:
            st.error(f"Non-JSON response for page {page}.")

    return all_articles

# Fetch data for all pages
data = fetch_all_data()

# Transform data into a DataFrame if data is available
if data:
    df = pd.DataFrame(data)
    # Select columns to display
    df_display = df[["articleNo", "articleName", "realEstateTypeName", "tradeTypeName", "floorInfo",
                     "dealOrWarrantPrc", "areaName", "direction", "articleConfirmYmd", "articleFeatureDesc",
                     "tagList", "buildingName", "sameAddrMaxPrc", "sameAddrMinPrc", "realtorName"]]

    # Display the table in Streamlit with a clean, readable layout
    st.write("### Real Estate Listings - Pages 1 to 10")
    st.dataframe(df_display)
else:
    st.write("No data available.")
