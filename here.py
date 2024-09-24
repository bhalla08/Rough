private async Task AddNewRegion()
{
    var parameters = new DialogParameters { ["Region"] = new Region() };
    var dialog = DialogService.Show<RegionDialog>("Add New Region", parameters);
    var result = await dialog.Result;

    // Check if result is not null and contains data
    if (result != null && !result.Canceled)
    {
        var newRegion = result.Data as Region;
        if (newRegion != null && !string.IsNullOrEmpty(newRegion.Code) && !string.IsNullOrEmpty(newRegion.Name))
        {
            // Check if a region with the same code already exists
            if (regions.Any(r => r.Code == newRegion.Code))
            {
                // Show error message or handle the duplicate code scenario
                Console.WriteLine("A region with the same code already exists.");
            }
            else
            {
                // Add the new region if no duplicate code is found
                RegionService.AddRegion(newRegion);
                StateHasChanged();
            }
        }
    }
}
