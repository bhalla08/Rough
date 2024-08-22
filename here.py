private async Task AddNewRegion()
{
    var parameters = new DialogParameters();
    var dialog = DialogService.Show<RegionDialog>("Add New Region", parameters);
    var result = await dialog.Result;

    if (!result.Cancelled)
    {
        var newRegion = (Region)result.Data;
        if (newRegion != null && !string.IsNullOrEmpty(newRegion.Code) && !string.IsNullOrEmpty(newRegion.Name))
        {
            regions.Add(newRegion);
            StateHasChanged();
        }
    }
}
