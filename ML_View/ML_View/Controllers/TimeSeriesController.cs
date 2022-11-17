using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json.Linq;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace ML_View.Controllers
{
    public class TimeSeriesController : Controller
    {
        public static string result;
        // GET: /<controller>/
        Uri baseAddress = new Uri("http://127.0.0.1:5000/");
        public IActionResult Index(string x)
        {
            if (x != null)
            {
                string nextUrl = $"model2?x={x}";
                HttpClient client = new HttpClient();
                client.BaseAddress = baseAddress;
              
               
                string fullurl = $"{client.BaseAddress}{nextUrl}";
                HttpResponseMessage respone = client.GetAsync(fullurl).Result;

                if (respone.IsSuccessStatusCode)
                {
                    string data = respone.Content.ReadAsStringAsync().Result;
                    var details = JObject.Parse(data);
                   
                    ViewData["message"] = Convert.ToString(details["message"]);
                    ViewData["2Days"] = Convert.ToString(details["2**Days"]);
                    ViewData["5Days"] = Convert.ToString(details["5*Days"]);
                    
                }
               
            }
            return View();
        }
    }
}

