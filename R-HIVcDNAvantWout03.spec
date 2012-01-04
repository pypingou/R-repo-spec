%global packname  HIVcDNAvantWout03
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          T cell line infections with HIV-1 LAI (BRU)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The expression levels of approximately 4600 cellular RNA transcripts were
assessed in CD4+ T cell lines at different times after infection with
HIV-1BRU using DNA microarrays. This data corresponds to the first block
of a 12 block array image (001030_08_1.GEL) in the first data set
(2000095918 A) in the first experiment (CEM LAI vs HI-LAI 24hr). There are
two data sets, which are part of a dye-swap experiment with replicates,
representing the Cy3 (green) absorption intensities for channel 1
(hiv1raw) and the Cy5 (red) absorption intensities for channel 2

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/HIVcDNAvantWout03/DESCRIPTION
%doc %{rlibdir}/HIVcDNAvantWout03/doc
%doc %{rlibdir}/HIVcDNAvantWout03/html
%{rlibdir}/HIVcDNAvantWout03/INDEX
%{rlibdir}/HIVcDNAvantWout03/data
%{rlibdir}/HIVcDNAvantWout03/help
%{rlibdir}/HIVcDNAvantWout03/NAMESPACE
%{rlibdir}/HIVcDNAvantWout03/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.5-1
- initial package for Fedora