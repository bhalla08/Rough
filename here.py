1. Modify the RegionDialog.razor File
razor
Copy code
@code {
    private RegionModel TempRegion { get; set; }
    private bool IsSaveDisabled => string.IsNullOrWhiteSpace(TempRegion.Code) || string.IsNullOrWhiteSpace(TempRegion.Name);

    protected override void OnParametersSet()
    {
        // Clone the original Region to TempRegion for editing
        TempRegion = new RegionModel
        {
            Code = Region.Code,
            Name = Region.Name,
            ShortDescription = Region.ShortDescription,
            Description = Region.Description,
            Status = Region.Status
        };
    }

    private void Save()
    {
        // Commit the changes from TempRegion back to Region
        Region.Code = TempRegion.Code;
        Region.Name = TempRegion.Name;
        Region.ShortDescription = TempRegion.ShortDescription;
        Region.Description = TempRegion.Description;
        Region.Status = TempRegion.Status;

        MudDialog.Close(DialogResult.Ok(Region));
    }

    private void Cancel()
    {
        MudDialog.Cancel();
    }
}

<MudDialog>
    <DialogContent>
        <MudTextField @bind-Value="TempRegion.Code" Label="Code" Required="true" Disabled="@IsEditMode" />
        <MudTextField @bind-Value="TempRegion.Name" Label="Name" Required="true" />
        <MudTextField @bind-Value="TempRegion.ShortDescription" Label="Short Description" />
        <MudTextField @bind-Value="TempRegion.Description" Label="Description" />
        <MudSelect T="string" @bind-Value="TempRegion.Status" Label="Status">
            <MudSelectItem Value="Active">Active</MudSelectItem>
            <MudSelectItem Value="Inactive">Inactive</MudSelectItem>
        </MudSelect>
    </DialogContent>
    <DialogActions>
        <MudButton Variant="Variant.Filled" Color="Color.Primary" OnClick="Save" Disabled="IsSaveDisabled">
            SAVE
        </MudButton>
        <MudButton Variant="Variant.Text" Color="Color.Secondary" OnClick="Cancel">
            CANCEL
        </MudButton>
    </DialogActions>
</MudDialog>
Explanation:
Cloning for Safe Editing:

When the dialog is opened, the original Region is cloned into a temporary object TempRegion.
This ensures that any changes made while editing are stored in TempRegion and not immediately reflected in the original Region.
Save Logic:

If the user clicks "Save," the changes from TempRegion are committed back to the original Region.
Cancel Logic:

If the user clicks "Cancel," the changes are discarded since Region remains unchanged.
This approach will ensure that your edits are only saved when the "Save" button is clicked, and any changes are discarded if "Cancel" is clicked.      