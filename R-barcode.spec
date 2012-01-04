%global packname  barcode
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Barcode distribution plots

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid R-lattice 

BuildRequires:    R-devel tex(latex) R-grid R-lattice 

%description
This package includes the function \code{barcode()}, which produces a
histogram-like plot of a distribution that shows granularity in the data.

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
%doc %{rlibdir}/barcode/DESCRIPTION
%doc %{rlibdir}/barcode/html
%{rlibdir}/barcode/INDEX
%{rlibdir}/barcode/R
%{rlibdir}/barcode/data
%{rlibdir}/barcode/NAMESPACE
%{rlibdir}/barcode/Meta
%{rlibdir}/barcode/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora