2. Create the Country Model
Define your Country model:

csharp
Copy code
namespace TarrWebApp.Models
{
    public class Country
    {
        public string CountryCode { get; set; }
        public string CountryShortName { get; set; }
        public string CountryName { get; set; }
        public string Region { get; set; }
        public string Currency { get; set; }
        public string Status { get; set; }  // Active/Inactive
    }
}
3. Create the Country Service
This service will handle CRUD operations in-memory for now, but you can later integrate it with a database.

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
4. Build the MudBlazor Form in ManageCountry.razor
Here’s a MudBlazor form with inputs and a table for managing countries:

razor
Copy code
@page "/manage-country"
@inject CountryService CountryService
@using TarrWebApp.Models

<MudText Typo="Typo.h3">Manage Country Information</MudText>

<MudForm @ref="form" Valid="isValid">
    <MudGrid>
        <MudItem xs="12" sm="6">
            <MudTextField @bind-Value="newCountry.CountryCode" Label="Country Code" Required="true" />
        </MudItem>
        <MudItem xs="12" sm="6">
            <MudTextField @bind-Value="newCountry.CountryShortName" Label="Country Short Name" Required="true" />
        </MudItem>
        <MudItem xs="12">
            <MudTextField @bind-Value="newCountry.CountryName" Label="Country Name" Required="true" />
        </MudItem>
        <MudItem xs="12" sm="6">
            <MudSelect @bind-Value="newCountry.Region" Label="Region" Required="true">
                <MudSelectItem Value="Asia Pacific">Asia Pacific</MudSelectItem>
                <MudSelectItem Value="Europe, Middle East and Africa">Europe, Middle East and Africa</MudSelectItem>
                <!-- Add more regions here -->
            </MudSelect>
        </MudItem>
        <MudItem xs="12" sm="6">
            <MudSelect @bind-Value="newCountry.Currency" Label="Currency" Required="true">
                <MudSelectItem Value="AUD">AUD</MudSelectItem>
                <MudSelectItem Value="EUR">EUR</MudSelectItem>
                <!-- Add more currencies here -->
            </MudSelect>
        </MudItem>
        <MudItem xs="12" sm="6">
            <MudSelect @bind-Value="newCountry.Status" Label="Status" Required="true">
                <MudSelectItem Value="Active">Active</MudSelectItem>
                <MudSelectItem Value="Inactive">Inactive</MudSelectItem>
            </MudSelect>
        </MudItem>
    </MudGrid>

    <MudButton OnClick="SaveCountry" Disabled="!isValid" Variant="Filled" Color="Color.Primary">Save</MudButton>
</MudForm>

<MudTable Items="@CountryService.GetCountries()" Striped="true">
    <HeaderContent>
        <MudTh>Country Code</MudTh>
        <MudTh>Country Short Name</MudTh>
        <MudTh>Country Name</MudTh>
        <MudTh>Region</MudTh>
        <MudTh>Currency</MudTh>
        <MudTh>Status</MudTh>
        <MudTh>Actions</MudTh>
    </HeaderContent>
    <RowTemplate>
        <MudTd>@context.CountryCode</MudTd>
        <MudTd>@context.CountryShortName</MudTd>
        <MudTd>@context.CountryName</MudTd>
        <MudTd>@context.Region</MudTd>
        <MudTd>@context.Currency</MudTd>
        <MudTd>@context.Status</MudTd>
        <MudTd>
            <MudButton OnClick="@(() => EditCountry(context))" Color="Color.Primary">Edit</MudButton>
            <MudButton OnClick="@(() => DeleteCountry(context.CountryCode))" Color="Color.Error">Delete</MudButton>
        </MudTd>
    </RowTemplate>
</MudTable>

@code {
    private Country newCountry = new Country();
    private MudForm form;
    private bool isValid;

    private void SaveCountry()
    {
        if (CountryService.GetCountries().Any(c => c.CountryCode == newCountry.CountryCode))
        {
            CountryService.UpdateCountry(newCountry);
        }
        else
        {
            CountryService.AddCountry(newCountry);
        }

        newCountry = new Country();  // Reset form after saving
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
        CountryService.DeleteCountry(countryCode);
    }
}
5. Summary of Features
MudForm: For form validation.
MudTextField and MudSelect: To handle user input with validation.
MudTable: To display the list of countries.
Edit/Delete functionality: Buttons to modify or delete countries from the list.
Let me know if you encounter any issues during the implementation!