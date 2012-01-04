%global packname  GWASdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.1
Release:          1%{?dist}
Summary:          Data used in the examples and vignettes of the GWASTools package

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Selected Affymetrix and Illlumina SNP data for HapMap subjects.  Data
provided by the Center for Inherited Disease Research at Johns Hopkins
University and the Broad Institute of MIT and Harvard University.

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
%doc %{rlibdir}/GWASdata/DESCRIPTION
%doc %{rlibdir}/GWASdata/html
%{rlibdir}/GWASdata/extdata
%{rlibdir}/GWASdata/NAMESPACE
%{rlibdir}/GWASdata/help
%{rlibdir}/GWASdata/INDEX
%{rlibdir}/GWASdata/data
%{rlibdir}/GWASdata/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.1-1
- initial package for Fedora