%global packname  MsatAllele
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.02
Release:          1%{?dist}
Summary:          Visualizes the scoring and binning of microsatellite fragment sizes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package contains functions to: 1) load ah files from Strand software
and build a R data base; 2) plot different graphical displays of the
fragment sizes obtained for each locus and their bins; 3) interact with
graphs to sort the data base for a given locus and range, allowing to
easily trace back a particular group of samples to its original Strand
file; bin fragment size data into population genetics files.

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
%doc %{rlibdir}/MsatAllele/html
%doc %{rlibdir}/MsatAllele/DESCRIPTION
%{rlibdir}/MsatAllele/NAMESPACE
%{rlibdir}/MsatAllele/Meta
%{rlibdir}/MsatAllele/data
%{rlibdir}/MsatAllele/R
%{rlibdir}/MsatAllele/INDEX
%{rlibdir}/MsatAllele/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.02-1
- initial package for Fedora