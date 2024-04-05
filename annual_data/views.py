import sqlite3

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config

# Create your views here.


class AnnualData(APIView):

    def get(self, request):
        well_number = request.GET.get("well")

        # Connect to SQLite database
        conn = sqlite3.connect(config("DB_LOCATION"))
        cursor = conn.cursor()

        # Retrieve data for the given well number
        query = f"SELECT oil, gas, brine FROM annual_production " \
                f"WHERE api_well_number='{well_number}'"
        cursor.execute(query)
        result = cursor.fetchone()

        # Close the connection
        conn.close()

        # Return the result in JSON format
        if result:
            return Response(
                {"oil": result[0], "gas": result[1], "brine": result[2]},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Data not found for the given well number"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
