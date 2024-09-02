protected override void OnParametersSet()
{
    // Check if we're in edit mode or adding a new region
    if (IsEditMode)
    {
        // Editing existing region, so populate TempRegion with existing values
        TempRegion = new Region
        {
            Code = Region.Code,
            Name = Region.Name,
            ShortDescription = Region.ShortDescription,
            Description = Region.Description,
            Status = Region.Status
        };

        // Set selectedValue based on existing status
        selectedValue = TempRegion.Status;
    }
    else
    {
        // Adding a new region, so initialize with default values
        TempRegion = new Region();
        
        // Default status should be 'Active'
        selectedValue = "Active";
        TempRegion.Status = selectedValue;
    }
}

private void Save()
{
    // Ensure TempRegion.Status is updated with the selected value
    TempRegion.Status = selectedValue;

    // Copy TempRegion's data back to Region
    Region.Code = TempRegion.Code;
    Region.Name = TempRegion.Name;
    Region.ShortDescription = TempRegion.ShortDescription;
    Region.Description = TempRegion.Description;
    Region.Status = TempRegion.Status;

    MudDialog.Close(DialogResult.Ok(Region));
}
