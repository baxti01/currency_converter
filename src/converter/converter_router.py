import aiohttp
from fastapi import APIRouter, Query, HTTPException, status

from src.settings import settings

API_URL = f'http://data.fixer.io/api/latest?access_key={settings.access_key}'

router = APIRouter(
    prefix='/rates'
)


@router.get('/')
async def currency_convert(
        from_currency: str = Query(alias='from'),
        to_currency: str = Query(alias='to'),
        value: float = Query(alias='value')
):
    params = {
        'symbols': f'{from_currency},{to_currency}'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            data = await response.json()
            rates = data.get('rates', [])
            error = data.get('error', None)
            if error:
                raise HTTPException(
                    detail=error['info'],
                    status_code=status.HTTP_400_BAD_REQUEST
                )

            if len(rates) != 2:
                raise HTTPException(
                    detail='Incorrect rates name',
                    status_code=status.HTTP_400_BAD_REQUEST
                )

            result = (1 / rates[from_currency] * rates[to_currency]) * value

            return {
                'result': round(result, 2)
            }
