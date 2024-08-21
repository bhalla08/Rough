@page "/region"
@using TarrWebApp.Models
@using TarrWebApp.Services
@inject RegionService RegionService

<MudTable Items="regions" Hover="true" Bordered="true" Striped="true">
    <HeaderContent>
        <MudTh>Code</MudTh>
        <MudTh>Name</MudTh>
        <MudTh>Short Description</MudTh>
        <MudTh>Description</MudTh>
        <MudTh>Status</MudTh>
        <MudTh>Actions</MudTh>
    </HeaderContent>
    <RowTemplate>
        <MudTd DataLabel="Code">@context.Code</MudTd>
        <MudTd DataLabel="Name">@context.Name</MudTd>
        <MudTd DataLabel="Short Description">@context.ShortDescription</MudTd>
        <MudTd DataLabel="Description">@context.Description</MudTd>
        <MudTd DataLabel="Status">@context.Status</MudTd>
        <MudTd DataLabel="Actions">
            <MudButton Variant="Variant.Text" Color="Color.Primary" OnClick="@(() => EditRegion(context))">Edit</MudButton>
            <MudButton Variant="Variant.Text" Color="Color.Error" OnClick="@(() => DeleteRegion(context.Code))">Delete</MudButton>
        </MudTd>
    </RowTemplate>
</MudTable>

<MudButton Variant="Variant.Filled" Color="Color.Primary" OnClick="AddNewRegion">New</MudButton>

<MudDialog @bind-IsVisible="showDialog">
    <DialogContent>
        <MudTextField @bind-Value="selectedRegion.Code" Label="Code" />
        <MudTextField @bind-Value="selectedRegion.Name" Label="Name" />
        <MudTextField @bind-Value="selectedRegion.ShortDescription" Label="Short Description" />
        <MudTextField @bind-Value="selectedRegion.Description" Label="Description" />
        <MudCheckBox @bind-Checked="selectedRegion.Status" Label="Active" />
    </DialogContent>
    <DialogActions>
        <MudButton Variant="Variant.Filled" Color="Color.Primary" OnClick="SaveRegion">Save</MudButton>
        <MudButton Variant="Variant.Text" Color="Color.Secondary" OnClick="CancelEdit">Cancel</MudButton>
    </DialogActions>
</MudDialog>

@code {
    private List<Region> regions = new List<Region>();
    private Region selectedRegion = new Region();
    private bool showDialog = false;

    protected override void OnInitialized()
    {
        // Populate the regions list from the service
        regions = RegionService.GetAllRegions();
        Console.WriteLine($"Initialized with {regions.Count} regions."); // Debugging
    }

    private void AddNewRegion()
    {
        selectedRegion = new Region(); // Create a new empty region
        showDialog = true; // Show the dialog for adding a new region
    }

    private void SaveRegion()
    {
        if (regions.Contains(selectedRegion))
        {
            RegionService.UpdateRegion(selectedRegion);
        }
        else
        {
            RegionService.AddRegion(selectedRegion);
            regions.Add(selectedRegion); // Add the new region to the list
        }

        showDialog = false; // Close the dialog
        StateHasChanged(); // Refresh the UI
    }

    private void DeleteRegion(string code)
    {
        RegionService.DeleteRegion(code);
        regions = RegionService.GetAllRegions(); // Refresh the list
        StateHasChanged(); // Refresh the UI
    }

    private void CancelEdit()
    {
        showDialog = false; // Close the dialog without saving
    }
}
