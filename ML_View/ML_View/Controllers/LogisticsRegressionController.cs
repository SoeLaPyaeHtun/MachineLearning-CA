using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json.Linq;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace ML_View.Controllers
{
    public class LogisticsRegressionController : Controller
    {
        public static string result;
        // GET: /<controller>/
        Uri baseAddress = new Uri("http://127.0.0.1:5000/");
        public IActionResult Index(string x1, string x2, string y1, string y2)
        {
            if (x1 != null && x2 != null && y1 != null && y2 != null)
            {
                string nextUrl = $"model1?x1={x1}&x2={x2}&y1={y1}&y2={y2}";
               
               
                HttpClient client = new HttpClient();
                client.BaseAddress = baseAddress;

                string fullurl = $"{client.BaseAddress}{nextUrl}";
                HttpResponseMessage respone = client.GetAsync(fullurl).Result;

                if (respone.IsSuccessStatusCode)
                {
                    string data = respone.Content.ReadAsStringAsync().Result;
                    var details = JObject.Parse(data);


                    ViewData["message"] = Convert.ToString(details["message"]);
                    ViewData["result"] = Convert.ToString(details["result"]);
                   
                }
            }

            return View();
        }
    }
}

