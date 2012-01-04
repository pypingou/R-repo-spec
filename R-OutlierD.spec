%global packname  OutlierD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          Outlier detection using quantile regression on the M-A scatterplots of high-throughput data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-quantreg 


BuildRequires:    R-devel tex(latex) R-Biobase R-quantreg



%description
This package detects outliers using quantile regression on the M-A
scatterplots of high-throughput data.

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
%doc %{rlibdir}/OutlierD/doc
%doc %{rlibdir}/OutlierD/DESCRIPTION
%doc %{rlibdir}/OutlierD/html
%{rlibdir}/OutlierD/NAMESPACE
%{rlibdir}/OutlierD/data
%{rlibdir}/OutlierD/INDEX
%{rlibdir}/OutlierD/R
%{rlibdir}/OutlierD/help
%{rlibdir}/OutlierD/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora