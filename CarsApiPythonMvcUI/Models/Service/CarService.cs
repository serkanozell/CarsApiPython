using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;

namespace CarsApiPythonMvcUI.Models.Service
{
    public class CarService
    {
        public async Task<List<Car>> GetCarList(Car car)
        {
            HttpResponseMessage responseMessage;
            HttpClient client = new HttpClient();
            client.Timeout = TimeSpan.FromSeconds(600);
            List<Car> cars = new List<Car>();
            string responseBody;
            if (car.Brand != null && car.Color != null && car.Transmission != null && car.Year != null)
            {
                client.BaseAddress = new Uri("http://127.0.0.1:5000");
                responseMessage = await client.GetAsync($"http://127.0.0.1:5000/cars/list?color={car.Color}&trans={car.Transmission}&year={car.Year}&year={car.Year}&brand={car.Brand}");
                responseMessage.EnsureSuccessStatusCode();
                responseBody = await responseMessage.Content.ReadAsStringAsync();
                var carList = JsonConvert.DeserializeObject<dynamic>(responseBody);

                foreach (var item in (IEnumerable<dynamic>)carList.cars)
                {
                    Car car1 = new Car()
                    {
                        Advert = item.advert,
                        Color = item.carColor,
                        Brand = item.brand,
                        Transmission = item.transmission,
                        Year = item.year,
                        Price = item.price
                    };
                    cars.Add(car1);
                }
            }
            return cars;
        }
    }
}
