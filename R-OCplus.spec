%global packname  OCplus
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Operating characteristics plus sample size and local fdr for microarray experiments

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-akima 
Requires:         R-multtest R-graphics R-grDevices R-stats 

BuildRequires:    R-devel tex(latex) R-akima
BuildRequires:    R-multtest R-graphics R-grDevices R-stats 


%description
This package allows to characterize the operating characteristics of a
microarray experiment, i.e. the trade-off between false discovery rate and
the power to detect truly regulated genes. The package includes tools both
for planned experiments (for sample size assessment) and for already
collected data (identification of differentially expressed genes).

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
%doc %{rlibdir}/OCplus/doc
%doc %{rlibdir}/OCplus/html
%doc %{rlibdir}/OCplus/DESCRIPTION
%{rlibdir}/OCplus/NAMESPACE
%{rlibdir}/OCplus/Meta
%{rlibdir}/OCplus/R
%{rlibdir}/OCplus/INDEX
%{rlibdir}/OCplus/help
RPM build errors:

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora