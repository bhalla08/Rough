@page "/region"
@using TarrWebApp.Models
@using TarrWebApp.Services
@inject RegionService RegionService
@inject MudBlazor.DialogService DialogService

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

@code {
    private List<Region> regions = new List<Region>();

    protected override void OnInitialized()
    {
        regions = RegionService.GetAllRegions();
    }

    private async Task AddNewRegion()
    {
        var parameters = new DialogParameters { ["Region"] = new Region() };
        var dialog = DialogService.Show<RegionDialog>("Add New Region", parameters);
        var result = await dialog.Result;

        // Check if result is not null and contains data
        if (result != null && result.Data != null)
        {
            var newRegion = (Region)result.Data;
            RegionService.AddRegion(newRegion);
            regions = RegionService.GetAllRegions(); // Refresh the list
            StateHasChanged(); // Refresh the UI
        }
    }

    private async Task EditRegion(Region region)
    {
        var parameters = new DialogParameters { ["Region"] = region };
        var dialog = DialogService.Show<RegionDialog>("Edit Region", parameters);
        var result = await dialog.Result;

        // Check if result is not null and contains data
        if (result != null && result.Data != null)
        {
            var updatedRegion = (Region)result.Data;
            RegionService.UpdateRegion(updatedRegion);
            regions = RegionService.GetAllRegions(); // Refresh the list
            StateHasChanged(); // Refresh the UI
        }
    }

    private void DeleteRegion(string code)
    {
        RegionService.DeleteRegion(code);
        regions = RegionService.GetAllRegions(); // Refresh the list
        StateHasChanged(); // Refresh the UI
    }
}
