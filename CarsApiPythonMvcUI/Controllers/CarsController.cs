using CarsApiPythonMvcUI.Models;
using CarsApiPythonMvcUI.Models.Service;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace CarsApiPythonMvcUI.Controllers
{
    public class CarsController : Controller
    {
        CarService _service;

        public CarsController(CarService service)
        {
            _service = service;
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Index(Car car)
        {
            var result = await _service.GetCarList(car);
            if (result != null)
            {
                return GetCarList(result);
            }
            return null;
        }

        [HttpGet]
        public  IActionResult GetCarList(List<Car> result)
        {
            return  View("GetCarList",result);
        }
    }
}
