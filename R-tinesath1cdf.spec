%global packname  tinesath1cdf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          tinesath1cdf

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A package containing an environment represeting the
newcdf/tinesATH1.cdf.cdf file.

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
%doc %{rlibdir}/tinesath1cdf/DESCRIPTION
%doc %{rlibdir}/tinesath1cdf/html
%{rlibdir}/tinesath1cdf/data
%{rlibdir}/tinesath1cdf/NAMESPACE
%{rlibdir}/tinesath1cdf/help
%{rlibdir}/tinesath1cdf/R
%{rlibdir}/tinesath1cdf/INDEX
%{rlibdir}/tinesath1cdf/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora