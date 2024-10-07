2. Service Layer for CRUD Operations
Create a service to handle CRUD operations, either in-memory or connected to a database.

csharp
Copy code
public class CountryService
{
    private List<Country> Countries = new List<Country>();

    public List<Country> GetCountries() => Countries;

    public void AddCountry(Country country)
    {
        if (!Countries.Any(c => c.CountryCode == country.CountryCode))
        {
            Countries.Add(country);
        }
    }

    public void UpdateCountry(Country country)
    {
        var existingCountry = Countries.FirstOrDefault(c => c.CountryCode == country.CountryCode);
        if (existingCountry != null)
        {
            existingCountry.CountryShortName = country.CountryShortName;
            existingCountry.CountryName = country.CountryName;
            existingCountry.Region = country.Region;
            existingCountry.Currency = country.Currency;
            existingCountry.Status = country.Status;
        }
    }

    public void DeleteCountry(string countryCode)
    {
        var country = Countries.FirstOrDefault(c => c.CountryCode == countryCode);
        if (country != null)
        {
            Countries.Remove(country);
        }
    }
}
3. Create the Razor Component
Create a new Razor component called ManageCountry.razor for the UI. This will have input fields and buttons to perform CRUD operations.

razor
Copy code
@page "/manage-country"

@inject CountryService CountryService

<h3>Manage Country Information</h3>

<div>
    <h4>Add / Edit Country</h4>

    <label>Country Code:</label>
    <input type="text" @bind="@newCountry.CountryCode" /><br/>

    <label>Country Short Name:</label>
    <input type="text" @bind="@newCountry.CountryShortName" /><br/>

    <label>Country Name:</label>
    <input type="text" @bind="@newCountry.CountryName" /><br/>

    <label>Region:</label>
    <select @bind="@newCountry.Region">
        <option value="Asia Pacific">Asia Pacific</option>
        <option value="Europe, Middle East and Africa">Europe, Middle East and Africa</option>
        <!-- More regions from Region table -->
    </select><br/>

    <label>Currency:</label>
    <select @bind="@newCountry.Currency">
        <option value="AUD">AUD</option>
        <option value="EUR">EUR</option>
        <!-- More currencies from Currency table -->
    </select><br/>

    <label>Status:</label>
    <select @bind="@newCountry.Status">
        <option value="Active">Active</option>
        <option value="Inactive">Inactive</option>
    </select><br/>

    <button @onclick="SaveCountry">Save</button>
</div>

<h4>Country List</h4>
<table>
    <thead>
        <tr>
            <th>Country Code</th>
            <th>Country Short Name</th>
            <th>Country Name</th>
            <th>Region</th>
            <th>Currency</th>
            <th>Status</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        @foreach (var country in CountryService.GetCountries())
        {
            <tr>
                <td>@country.CountryCode</td>
                <td>@country.CountryShortName</td>
                <td>@country.CountryName</td>
                <td>@country.Region</td>
                <td>@country.Currency</td>
                <td>@country.Status</td>
                <td>
                    <button @onclick="() => EditCountry(country)">Edit</button>
                    <button @onclick="() => DeleteCountry(country.CountryCode)">Delete</button>
                </td>
            </tr>
        }
    </tbody>
</table>

@code {
    private Country newCountry = new Country();

    private void SaveCountry()
    {
        if (string.IsNullOrWhiteSpace(newCountry.CountryCode))
        {
            // Error handling: country code must be unique and non-empty
            return;
        }

        if (CountryService.GetCountries().Any(c => c.CountryCode == newCountry.CountryCode))
        {
            CountryService.UpdateCountry(newCountry);
        }
        else
        {
            CountryService.AddCountry(newCountry);
        }

        // Reset the form
        newCountry = new Country();
    }

    private void EditCountry(Country country)
    {
        newCountry = new Country
        {
            CountryCode = country.CountryCode,
            CountryShortName = country.CountryShortName,
            CountryName = country.CountryName,
            Region = country.Region,
            Currency = country.Currency,
            Status = country.Status
        };
    }

    private void DeleteCountry(string countryCode)
    {
        if (confirm("Are you sure you want to delete this record?"))
        {
            CountryService.DeleteCountry(countryCode);
        }
    }

    private bool confirm(string message)
    {
        // You can implement JavaScript confirm or use a Blazor modal dialog
        return true; 
    }
}
4. Add Admin Authorization (Optional)
To enforce admin-only access, use role-based authentication in your Blazor app:

razor
Copy code
@attribute [Authorize(Roles = "Admin")]
This would restrict access to only users with the "Admin" role.