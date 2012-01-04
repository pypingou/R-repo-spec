%global packname  hgu2beta7
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          A data package containing annotation data for hgu2beta7

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Annotation data file for hgu2beta7 assembled using data from public data

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
%doc %{rlibdir}/hgu2beta7/html
%doc %{rlibdir}/hgu2beta7/DESCRIPTION
%{rlibdir}/hgu2beta7/INDEX
%{rlibdir}/hgu2beta7/NAMESPACE
%{rlibdir}/hgu2beta7/help
%{rlibdir}/hgu2beta7/data
%{rlibdir}/hgu2beta7/R
%{rlibdir}/hgu2beta7/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.5-1
- initial package for Fedora